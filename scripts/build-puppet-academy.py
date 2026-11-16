#!/usr/bin/env python3
"""Build Puppet Academy galleries and detail pages from the curated catalog.

Version 1.0.0. Uses ImageMagick for web-format exports; originals stay untouched.
Pass --library to import/update artwork, or omit it to rebuild existing media.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from hashlib import sha256
from html import escape
import json
from pathlib import Path
import re
import subprocess
import unicodedata
from urllib.parse import urlsplit

SCRIPT_VERSION = '1.0.0'
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'website'
ACADEMY = SITE / 'puppet-academy'
CONTENT = ROOT / 'content' / 'puppet-academy'
BASE = '/puppet-academy'
ORIGIN = 'https://catnapradio.com'
CATEGORIES = ['Science & nature', 'Music & sound', 'Stories & society', 'Hosts & guests']


def esc(value):
    return escape(str(value), quote=True)


def slug(value):
    plain = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', plain).strip('-')


def sort_name(entry):
    name = entry['name']
    for prefix in ['Puppet Professor ', 'Maestro Dr. ', 'Professor ', 'Dr. ']:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    return slug(name)


def validate(data):
    assert data['schema_version'] == 1, 'Unsupported catalog schema'
    date.fromisoformat(data['updated'])
    for collection in ['professors', 'songs']:
        ids = [item['id'] for item in data[collection]]
        assert len(ids) == len(set(ids)), f'Duplicate {collection} IDs'
        assert all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', item) for item in ids)
    ids = {item['id'] for item in data['professors']}
    for item in data['professors']:
        assert item['category'] in CATEGORIES, item['id']
    for item in data['songs']:
        assert item.get('professor_id') is None or item['professor_id'] in ids, item['id']
        if item.get('listen_url'):
            url = urlsplit(item['listen_url'])
            assert url.scheme == 'https' and url.netloc, 'Listening links must be real HTTPS URLs'


def import_media(data, library):
    target = ACADEMY / 'assets' / 'catalog'
    manifest_file = CONTENT / 'media-manifest.json'
    old = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
    jobs = [('ensemble', data['ensemble_source'])]
    for kind in ['professors', 'songs']:
        jobs.extend((kind + '/' + item['id'], item['source']) for item in data[kind])

    def export(job):
        key, source = job
        output = target / key
        full = output.with_name(output.name + '-full.webp')
        thumb = output.with_name(output.name + '-thumb.webp')
        previous = old.get(key)
        if library is None:
            assert previous and full.exists() and thumb.exists(), f'Import media first: {source}'
            return key, previous
        original = (library / source).resolve()
        assert original.is_relative_to(library), f'Artwork must be inside the library: {source}'
        assert original.is_file(), f'Missing artwork: {source}'
        digest = sha256(original.read_bytes()).hexdigest()
        if previous and previous['source_sha256'] == digest and full.exists() and thumb.exists():
            return key, previous
        width, height = map(int, subprocess.check_output(
            ['magick', 'identify', '-format', '%w %h', str(original)], text=True).split())
        full.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['magick', str(original), '-strip', '-quality', '92', str(full)], check=True)
        subprocess.run(['magick', str(original), '-thumbnail', '640x800>', '-strip', '-quality', '85', str(thumb)], check=True)
        tw, th = map(int, subprocess.check_output(
            ['magick', 'identify', '-format', '%w %h', str(thumb)], text=True).split())
        return key, dict(source=source, source_sha256=digest, width=width, height=height,
                         thumb_width=tw, thumb_height=th,
                         full='/' + str(full.relative_to(SITE)), thumb='/' + str(thumb.relative_to(SITE)))

    with ThreadPoolExecutor(max_workers=3) as executor:
        manifest = dict(executor.map(export, jobs))
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return manifest


def header(active):
    links = [('academy', BASE + '/', 'Start here'),
             ('professors', BASE + '/professors/', 'Professors'),
             ('songs', BASE + '/songs/', 'Songs'),
             ('join', BASE + '/#join', 'Join the faculty')]
    nav = ''.join(f'<a href="{url}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>'
                  for key, url, label in links)
    return f'''<header class="masthead">
  <a class="brand" href="{BASE}/"><span class="brand-star" aria-hidden="true">✦</span><span>PUPPET ACADEMY<small>THE FELT FACULTY · CATNAP RADIO</small></span></a>
  <nav class="academy-nav" aria-label="Puppet Academy">{nav}</nav>
</header>'''


def footer():
    return f'''<footer class="catalog-footer"><a href="/">← Catnap Radio</a><nav aria-label="More from the Academy"><a href="{BASE}/">Academy guide</a><a href="{BASE}/professors/">Professors</a><a href="{BASE}/songs/">Songs</a></nav><span>More music. More wonder. More felt.</span></footer>'''


def document(title, description, path, image, active, body):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} · Puppet Academy · Catnap Radio</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#4b2066">
  <meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} · Puppet Academy">
  <meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{ORIGIN}{path}">
  <meta property="og:image" content="{ORIGIN}{image}"><meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{ORIGIN}{path}"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{BASE}/academy.css"><link rel="stylesheet" href="{BASE}/catalog.css?v=1">
</head>
<body class="catalog-page">
<a class="skip" href="#main">Skip to the good stuff</a>
{header(active)}
<main id="main">{body}</main>
{footer()}
</body>
</html>
'''


def image_tag(media, alt, thumb=False, eager=False, css=''):
    url = media['thumb' if thumb else 'full']
    w, h = (media['thumb_width'], media['thumb_height']) if thumb else (media['width'], media['height'])
    return f'<img src="{url}" width="{w}" height="{h}" alt="{esc(alt)}" class="{esc(css)}" loading="{"eager" if eager else "lazy"}" decoding="async">'


def professor_card(item, media):
    path = BASE + '/professors/' + item['id'] + '/'
    return f'''<article class="profile-card" id="{item['id']}">
<a class="profile-image" href="{path}" aria-label="Meet {esc(item['name'])}">{image_tag(media, item['name'] + ' — illustrated Puppet Academy character sheet', True)}</a>
<div class="profile-card-copy"><p class="card-subject">{esc(item['subject'])}</p><h3><a href="{path}">{esc(item['name'])}</a></h3><p>{esc(item['description'])}</p><a class="card-action" href="{path}">Meet the character <span aria-hidden="true">↗</span></a></div>
</article>'''


def song_card(item, media):
    path = BASE + '/songs/' + item['id'] + '/'
    badge = '<span class="concept-badge">Cover concept</span>' if item.get('status') == 'Cover concept' else ''
    return f'''<article class="song-card" id="{item['id']}">
<a class="song-image" href="{path}" aria-label="Explore {esc(item['title'])}">{image_tag(media, 'Cover artwork for ' + item['title'] + ', featuring ' + item['professor'], True)}{badge}</a>
<div class="song-card-copy"><p class="card-subject">{esc(item['professor'])}</p><h3><a href="{path}">{esc(item['title'])}</a></h3><p class="song-subtitle">{esc(item['subtitle'])}</p><p class="lesson-chip">{esc(item['lesson'])}</p><a class="card-action" href="{path}">Cover &amp; lesson <span aria-hidden="true">↗</span></a></div>
</article>'''


def write(path, value):
    output = SITE / path.strip('/') / 'index.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(value)


def galleries(data, media):
    professors = sorted(data['professors'], key=sort_name)
    by_id = {p['id']: p for p in professors}
    ensemble = media['ensemble']
    counts = f'{len(professors)} faculty &amp; friends'
    body = f'''<section class="catalog-hero section-wrap">
<div class="catalog-hero-copy"><p class="eyebrow">PUPPET ACADEMY / THE FELT FACULTY</p><h1>Beautifully odd minds.<br><span>Very memorable lessons.</span></h1><p class="catalog-intro">Meet the professors—and the curious characters who share their stage. Pick a name. Open a sheet. Find your kind of chaos.</p><p class="catalog-count"><span aria-hidden="true">✦</span> {counts} · growing by the lecture</p><div class="catalog-actions"><a class="button purple" href="#directory">Meet the faculty ↓</a><a class="button outline" href="{BASE}/songs/">Explore the songbook ↗</a></div></div>
<figure class="ensemble-art">{image_tag(ensemble, 'The Felt Faculty gathered in a colourful Puppet Academy classroom, with books, instruments, frogs, and musical experiments', True, True)}<figcaption>A few of the beautifully unreasonable minds at work.</figcaption></figure></section>'''
    jumps = ''.join(f'<a href="#{slug(c)}">{esc(c)} <span>{sum(p["category"] == c for p in professors)}</span></a>' for c in CATEGORIES)
    names = ''.join(f'<a href="#{p["id"]}">{esc(p["name"])}</a>' for p in professors)
    body += f'''<section class="directory-tools section-wrap" id="directory"><p class="eyebrow">FIND YOUR KIND OF CURIOUS</p><h2>The faculty directory.</h2><p>Jump to a subject, or find a familiar name.</p><nav class="subject-jumps" aria-label="Jump to a subject">{jumps}</nav><details class="name-index"><summary>Find a name · {len(professors)} profiles</summary><div>{names}</div></details></section>'''
    for category in CATEGORIES:
        group = [p for p in professors if p['category'] == category]
        if not group:
            continue
        body += f'<section class="directory-group section-wrap" id="{slug(category)}"><div class="group-heading"><div><p class="eyebrow">THE FELT FACULTY</p><h2>{esc(category)}</h2></div><span class="group-count">{len(group)} profiles</span></div><div class="profile-grid">'
        body += ''.join(professor_card(p, media['professors/' + p['id']]) for p in group)
        body += '</div><a class="back-to-directory" href="#directory">↑ Back to the directory</a></section>'
    body += grow_cta('A seat at the lectern is waiting.', 'Your character. Your subject. Your own very particular brand of felt chaos.')
    write(BASE + '/professors/', document('Meet the professors', 'Meet the Felt Faculty: illustrated Puppet Academy professors, musical guests, and their wildly individual lessons.', BASE + '/professors/', ensemble['full'], 'professors', body))

    selected = ['everything-rots', 'fuuu-sion', 'the-duck-has-no-honor']
    stack = ''.join(f'<a href="{BASE}/songs/{sid}/" aria-label="Explore {esc(next(s["title"] for s in data["songs"] if s["id"] == sid))}">{image_tag(media["songs/" + sid], next(s["title"] for s in data["songs"] if s["id"] == sid) + ' cover artwork', True, True)}</a>' for sid in selected)
    body = f'''<section class="catalog-hero songbook-hero section-wrap"><div class="catalog-hero-copy"><p class="eyebrow">PUPPET ACADEMY / THE SONGBOOK</p><h1>Real lessons.<br><span>Turned all the way up.</span></h1><p class="catalog-intro">Science, stories, and spectacular classroom disasters. Browse the lessons, meet the voices, and open the cover art.</p><p class="catalog-count"><span aria-hidden="true">♫</span> {len(data['songs'])} song &amp; cover entries · more on the way</p><div class="catalog-actions"><a class="button purple" href="#songbook">Browse the songbook ↓</a><a class="button outline" href="{BASE}/#make">Make a song ↗</a></div></div><div class="cover-stack" aria-label="A taste of the songbook">{stack}</div></section>'''
    group_order = ['runa-rassafrass', 'gowron', 'aurora-vintesang', 'pondscum']
    groups = [(pid, by_id[pid]['name'], [s for s in data['songs'] if s.get('professor_id') == pid]) for pid in group_order]
    # New professors and independent cover concepts are picked up automatically.
    seen = set(group_order)
    for p in professors:
        if p['id'] not in seen:
            group = [s for s in data['songs'] if s.get('professor_id') == p['id']]
            if group:
                groups.append((p['id'], p['name'], group))
    others = sorted({s['professor'] for s in data['songs'] if not s.get('professor_id')})
    groups.extend((slug(name), name, [s for s in data['songs'] if not s.get('professor_id') and s['professor'] == name]) for name in others)
    groups = [group for group in groups if group[2]]
    jumps = ''.join(f'<a href="#songs-{pid}">{esc(name.replace("Professor ", "").replace("Puppet ", ""))} <span>{len(group)}</span></a>' for pid, name, group in groups)
    body += f'<section class="directory-tools section-wrap" id="songbook"><p class="eyebrow">CHOOSE YOUR LECTURER</p><h2>Class begins with a chorus.</h2><p>Each card opens the artwork and a little explanation of the lesson.</p><nav class="subject-jumps" aria-label="Jump to a lecturer">{jumps}</nav></section>'
    for pid, name, group in groups:
        name_html = f'<a href="{BASE}/professors/{pid}/">{esc(name)} ↗</a>' if pid in by_id else esc(name)
        body += f'<section class="directory-group section-wrap" id="songs-{pid}"><div class="group-heading"><div><p class="eyebrow">FROM THE SONGBOOK</p><h2>{name_html}</h2></div><span class="group-count">{len(group)} {"entry" if len(group) == 1 else "entries"}</span></div><div class="song-grid">'
        body += ''.join(song_card(s, media['songs/' + s['id']]) for s in group)
        body += '</div><a class="back-to-directory" href="#songbook">↑ Back to the songbook</a></section>'
    body += grow_cta('What will your professor teach?', 'One clear idea. A hook that sticks. A classroom that may never recover.')
    write(BASE + '/songs/', document('The songbook', 'Browse Puppet Academy songs and cover artwork: real lessons, ridiculous professors, and glorious musical chaos.', BASE + '/songs/', ensemble['full'], 'songs', body))


def grow_cta(title, text):
    return f'<section class="catalog-grow section-wrap"><p class="eyebrow">THE ACADEMY KEEPS GROWING</p><h2>{esc(title)}</h2><p>{esc(text)}</p><a class="button purple" href="{BASE}/#join">Join the Felt Faculty ↗</a></section>'


def detail_pages(data, media):
    for p in data['professors']:
        m = media['professors/' + p['id']]
        related = [s for s in data['songs'] if s.get('professor_id') == p['id']]
        music = f'<div class="detail-note"><h2>Musical flavour</h2><p>{esc(p["music"])}</p></div>' if p.get('music') else ''
        body = f'''<section class="detail-page section-wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="{BASE}/">Puppet Academy</a><span aria-hidden="true">/</span><a href="{BASE}/professors/">Professors</a></nav><div class="detail-layout"><div class="detail-copy"><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['name'])}</h1><p class="detail-subject">{esc(p['subject'])}</p><p class="detail-description">{esc(p['description'])}</p>{music}<div class="detail-actions"><a class="button purple" href="{m['full']}">Open full character sheet ↗</a><a class="text-link" href="{BASE}/professors/">← All professors</a></div><p class="small">An illustrated character in the world of Puppet Academy. Faculty titles and departments are part of the creative setting.</p></div><figure class="detail-art"><a href="{m['full']}" aria-label="Open the full character sheet for {esc(p['name'])}">{image_tag(m, p['name'] + ' illustrated character sheet', eager=True)}</a><figcaption>Character sheet · tap to open the full artwork.</figcaption></figure></div></section>'''
        if related:
            body += '<section class="related-work section-wrap"><p class="eyebrow">FROM THE SONGBOOK</p><h2>A few of their lessons.</h2><div class="song-grid">'
            body += ''.join(song_card(s, media['songs/' + s['id']]) for s in related)
            body += '</div></section>'
        else:
            body += f'<section class="related-work quiet-section section-wrap"><p class="eyebrow">MORE LESSONS ARE ON THE WAY</p><h2>There’s always another class.</h2><p>Browse the growing songbook—or bring an idea of your own.</p><a class="button outline" href="{BASE}/songs/">Explore the songbook ↗</a></section>'
        path = BASE + '/professors/' + p['id'] + '/'
        write(path, document(p['name'], p['subject'] + '. ' + p['description'], path, m['full'], 'professors', body))

    by_id = {p['id']: p for p in data['professors']}
    for s in data['songs']:
        m = media['songs/' + s['id']]
        pid = s.get('professor_id')
        professor = f'<a href="{BASE}/professors/{pid}/">{esc(s["professor"])} ↗</a>' if pid in by_id else esc(s['professor'])
        listen = f'<a class="button teal" href="{esc(s["listen_url"])}">Listen to the song ↗</a>' if s.get('listen_url') else ''
        status = '<p class="concept-note">An illustrated lesson concept from the Academy workshop.</p>' if s.get('status') == 'Cover concept' else ''
        body = f'''<section class="detail-page song-detail section-wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="{BASE}/">Puppet Academy</a><span aria-hidden="true">/</span><a href="{BASE}/songs/">Songbook</a></nav><div class="detail-layout"><div class="detail-copy"><p class="eyebrow">PUPPET ACADEMY / THE SONGBOOK</p><h1>{esc(s['title'])}</h1><p class="detail-subject">{esc(s['subtitle'])}</p><p class="detail-teacher">Featuring {professor}</p><div class="detail-note"><h2>The lesson</h2><p class="lesson-chip">{esc(s['lesson'])}</p><p>{esc(s['description'])}</p></div>{status}<p class="detail-credit">Artwork credit: {esc(s['credit'])}</p><div class="detail-actions">{listen}<a class="button purple" href="{m['full']}">Open full cover artwork ↗</a><a class="text-link" href="{BASE}/songs/">← All songs &amp; covers</a></div></div><figure class="detail-art cover-detail"><a href="{m['full']}" aria-label="Open full cover artwork for {esc(s['title'])}">{image_tag(m, 'Cover artwork for ' + s['title'], eager=True)}</a><figcaption>Song cover · tap to open the full artwork.</figcaption></figure></div></section>'''
        body += grow_cta('Your lesson belongs here, too.', 'Make an educational Puppet Academy song, or ask Ina & Len for help with an OC and a topic.')
        path = BASE + '/songs/' + s['id'] + '/'
        write(path, document(s['title'], s['professor'] + ': ' + s['description'], path, m['full'], 'songs', body))


def update_guide(data, media):
    path = ACADEMY / 'index.html'
    text = path.read_text()
    css = f'<link rel="stylesheet" href="{BASE}/catalog.css?v=1">'
    if css not in text:
        text = text.replace('</head>', '  ' + css + '\n</head>')
    new_nav = re.search(r'<nav class="academy-nav".*?</nav>', header('academy'), re.S).group()
    text, count = re.subn(r'<nav(?: class="academy-nav")? aria-label="Puppet Academy">.*?</nav>', new_nav, text, flags=re.S)
    assert count == 1, 'Could not locate the guide navigation'
    doors = f'''<!-- BEGIN ACADEMY CATALOG DOORS -->
<section class="catalog-doors section-wrap" aria-label="Explore the Academy">
<a href="{BASE}/professors/">{image_tag(media['ensemble'], 'The Felt Faculty ensemble', True)}<div><span class="eyebrow">{len(data['professors'])} FACULTY &amp; FRIENDS</span><h2>Meet the professors.</h2><p>Find your favourite beautifully odd mind.</p><span class="card-action">Open the directory ↗</span></div></a>
<a href="{BASE}/songs/">{image_tag(media['songs/everything-rots'], 'EVERYTHING ROTS! song cover', True)}<div><span class="eyebrow">{len(data['songs'])} SONG &amp; COVER ENTRIES</span><h2>Explore the songbook.</h2><p>Real lessons with very memorable choruses.</p><span class="card-action">Browse the covers ↗</span></div></a>
</section>
<!-- END ACADEMY CATALOG DOORS -->'''
    if '<!-- BEGIN ACADEMY CATALOG DOORS -->' in text:
        text = re.sub(r'<!-- BEGIN ACADEMY CATALOG DOORS -->.*?<!-- END ACADEMY CATALOG DOORS -->', lambda _: doors, text, flags=re.S)
    else:
        needle = '  <section class="quick section-wrap"'
        assert needle in text
        text = text.replace(needle, doors + '\n\n' + needle, 1)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library', type=Path, help='Local Puppet Academy library with Char sheets/, Song Covers/, and Reference/.')
    args = parser.parse_args()
    data = json.loads((CONTENT / 'catalog.json').read_text())
    validate(data)
    media = import_media(data, args.library.resolve() if args.library else None)
    galleries(data, media)
    detail_pages(data, media)
    update_guide(data, media)
    print(f'Puppet Academy catalog {SCRIPT_VERSION}: {len(data["professors"])} profiles, {len(data["songs"])} songs, galleries and detail pages built.')


if __name__ == '__main__':
    main()
