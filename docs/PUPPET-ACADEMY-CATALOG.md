# Puppet Academy catalog

The public galleries are `/puppet-academy/professors/` and `/puppet-academy/songs/`. Every card has its own permanent detail URL. Cards, counts, subject/name indexes, related songs, and the links from the Academy guide come from one catalog.

## Adding a professor or song

1. Put the original artwork in the local Puppet Academy library: `Char sheets/`, `Song Covers/`, or `Reference/`. Keep the original intact.
2. Add an entry to `content/puppet-academy/catalog.json`. Copy a neighbouring entry, choose a unique lowercase hyphenated `id`, and set its library-relative `source` filename. Keep the `id` stable when replacing artwork or revising copy.
3. For professors, fill in `name`, `category`, `subject`, and a short `description`. Use one of the existing categories; `music` may be empty when no style is established. Hosts and musical guests have their own category.
4. For songs, fill in `title`, `professor`, `lesson`, `description`, and the artwork credit. `professor_id` links the song to a catalog profile; use `null` if that profile is not present yet. A recording link is optional: add only a verified HTTPS `listen_url`. A cover alone does not establish a released recording; use `Cover concept` when appropriate.
5. Set `updated` to the catalog revision date. Rebuild using the local library path:

```sh
python3 scripts/build-puppet-academy.py --library "$PUPPET_LIBRARY"
```

The builder needs Python 3.9+ and ImageMagick 7 (`magick`). It exports full-size WebP artwork plus smaller thumbnails, preserving proportions without cropping or changing the original source files. Unchanged artwork is reused by its source hash. To rebuild copy and pages without reimporting artwork:

```sh
python3 scripts/build-puppet-academy.py
```

6. Check the changed pages and run the repository publication guard. Commit the catalog, generated pages, media manifest, and new web artwork together. Deploy the reviewed website files using the existing Catnap website workflow. Adding a file to a local folder does not itself publish it.

## Content and design

- The professor directory groups profiles by subject, with a collapsible name index and permanent section anchors. The songbook groups entries by lecturer. New professors and lecturers are picked up by the builder.
- Existing galleries use lazy-loaded thumbnails, responsive grids, native links, and native expandable details. They work with the site's script-blocking policy; no JavaScript, new account, upload form, or hosting-policy change is needed.
- Every profile and song links back to its gallery. Professor pages also link to their song entries. Missing recording links produce no empty or misleading Play button.
- Current public copy says **Puppet Academy / The Felt Faculty**. Supplied artwork is displayed as supplied. Where corrected duplicates exist, use the corrected revision and record the older file under `alternate_sources` rather than making duplicate cards.
- Keep fictional faculty roles separate from offline biography and real credentials. Do not turn a proposed genre, song idea, or illustrated concept into a claim of a released recording.
- `media-manifest.json` records source filenames and hashes. It must not contain machine-specific home paths, private account data, or credentials. No private primers, event records, or full lyrics belong in the public catalog.
- Generated pages and artwork are not automatically deleted when an entry is removed. Review any intentional archive/removal separately; preserve permanent IDs where possible.

The original gallery set contains 25 distinct faculty/guest profiles and 11 song/cover entries, with three older artwork revisions grouped under their current entry. Counts on the site are generated and grow with the catalog.
