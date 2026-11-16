# Catnap Radio · projects and guides

Music tools for AI:Underground listening parties, with Ina & Len.

**[Listen](https://listen.catnapradio.com/) · [Theatre Lite 0.5.0](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.5.0/Catnap-Theatre-v0.5.0.zip) · [CatnapRadio.com](https://catnapradio.com/) · [Try AIU Theatre + Inbox 0.8.1 preview](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.1-preview) · [Simple inbox walkthrough](https://github.com/inaratalamasca/aiu-inbox-playlist-guide)**

## Start here

- **Listening?** Open the [web player](https://listen.catnapradio.com/) and tap Play. Live aims for low delay; Radio is buffered for mobile/background listening. In Discord, mute the shared stream's audio and keep individual voices on.
- **Presenting ordinary Suno or hosting without the AIU Inbox?** Choose [Theatre Lite 0.5.0](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.5.0/Catnap-Theatre-v0.5.0.zip). It is the active presentation-only choice, using the unchanged 0.5.0 package. No Inbox setup or Suno playlist helper is required. [Setup and checksum](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0).
- **Hosting with the AIU Inbox and a managed show?** Try the [AIU Theatre + Inbox 0.8.1 preview](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.1-preview). It combines the presentation with optional LP/AP inbox intake, playlist creation and a mixed Suno/YouTube show queue. LP uses separate Load and Play actions; AP autoplay is optional.
- **Just creating an inbox playlist?** Choose the **Inbox-only 0.8.1 preview** on the same release page. It prepares playlists without Theatre playback, streaming or a co-host bot. No LLM is required for the managed playlist workflow; follow the included guide for your own Suno connection.
- **Broadcasting music without Inbox setup?** Choose **Radio-only 0.8.1 preview** from the [preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.1-preview). It publishes a Suno or [AIU party player](https://party.aiu.fm/party) tab without a desktop helper. It can run alongside unchanged Theatre Lite; use one publisher for the show.
- **Using an agent instead?** The [simple inbox guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) remains available. Verify tool access, start with one saved addition and use the intended Pending inbox oldest-first during an explicitly requested watch.
- **Developing or reporting a bug?** Use the relevant project's Issues. See the [GitHub guide](docs/GITHUB-GUIDE.md) and [contribution notes](CONTRIBUTING.md).

Theatre Lite stays separate from the AIU Inbox edition; the new readiness work does not change its files.

The Theatre + Inbox, Inbox-only and Radio-only 0.8.1 downloads are **development previews** for rehearsal. The maintainer reported own-account Suno authorization, playlist creation and clean Suno/HQ audio in 0.6.2. The 0.6.3 trial staged an LP entry but missed its native Play control. In 0.6.4 the row was found and quiet Load worked, but Play timed out because Suno did not load the selected song. The 0.6.5 retry reported “Target matched, audio not found”. Version 0.6.6 distinguishes the active music player from Suno’s silent helper while retaining bounded muted preparation. The host confirmed the standalone 0.6.6 manual LP sequence: Play song 1, hold at its ending, Load Next paused, then Play song 2. That trial exposed missing managed lyrics. The 0.6.7 host retry still showed missing lyrics after Reload. On November 16, the host confirmed manual 0.6.10 activation in Dev1, working status indicators and managed lyrics. The repeated-click intake fix and playlist updates remain pending a real check. The lyrics correction preserves line breaks and prefers the selected song’s own panel. Mixed-source transitions, AP, advanced live integration and Discord/HQ checks remain separate. This is not full-show acceptance. The Chrome Web Store **0.5.0 beta is pending review**; it is not a published Store listing.

Version 0.6.9 groups Presentation and Inbox controls with matching button styles. The list heading identifies **Inbox Show** versus **Suno Playlist**, and **Inbox Submissions** makes Pending/held counts and the read time easier to see. Version 0.6.10 adds labeled Suno/Inbox readiness dots at the top and a result for each setup step. They remain grey/inactive during ordinary use of the Inbox edition; they do not make Inbox setup part of Theatre Lite. The November 16 Dev1 confirmation covers activation, status indicators and managed lyrics; it does not accept the broader intake, playlist-update, AP, YouTube or advanced live workflow.

The 0.8.1 preview retains a source-only On Air indicator and green Theatre AIU logo while live, a single gear opening Presentation controls with Radio/Inbox buttons, and a mode-aware status box that stays non-green while pending or in error. Managed YouTube Play fills the Theatre window with a red YouTube badge; quiet staging is labeled Loaded. Loaded/playing song cards keep artwork, credit and warnings compact; clicking the thumbnail copies its clean public image URL. On a clean install, Theatre + Inbox offers a nonblocking stream-name prompt; upgrades and existing name preferences are not prompted, and Catnap Radio remains the default. Radio can remember a token for the same relay origin across normal updates, with session-only and Forget choices. This is local extension storage, not an encrypted vault; removal or a different profile is not guaranteed to retain it. The host confirmed working 0.8 Radio broadcasting on November 16 after an initial startup timeout; its cause remains unproven. That result does not establish fair rotation, playlist ordering, Decline, the 0.8.1 fixes or advanced live acceptance. Radio needs no Suno helper; playlist creation in the AIU creators still uses the host’s own Suno connection and desktop companion.

## Three fixes in 0.8.1

- Choosing a song keeps it in place in the running order.
- YouTube video fills the Theatre window without a permanent Catnap button strip.
- Reopen Theatre during a live broadcast without stopping the music.

These fixes are ready for rehearsal; real host acceptance remains pending.

## Projects

| Project | What it does | Availability |
| --- | --- | --- |
| [Theatre Lite](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) | Active presentation-only edition for ordinary Suno and non-AIU hosts; no Inbox or playlist helper | Unchanged **0.5.0** download |
| [AIU Theatre + Inbox](https://github.com/inaratalamasca/catnap-theatre) | Presentation, separate controls, overlays, optional audio publishing and a managed LP/AP Suno/YouTube queue | Public source and **0.8.1 preview** downloads for combined Theatre + Inbox or Inbox-only; Theatre Lite remains a separate active edition |
| Radio-only | Audio publishing from Suno or AIU party tabs, independently of Inbox/playlist creation | **0.8.1 preview**; no desktop helper; can accompany Theatre Lite |
| [AIU inbox playlist guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) | Minimal agent instructions for LP/AP playlists and optional now-playing assistance | Public guide; actual tool/browser access must be verified |
| Advanced Radio Hosting | Shared Theatre, compatible Host Controls, bot/backend integration and full show preparation | Private **Theatre 0.8.1 / Host Controls 0.4.8 preview**; live rehearsal remains pending |
| Catnap Simulcast | Music-only relay and web player, alongside separate Discord voices | [Listener 0.1.7 available during broadcasts](https://listen.catnapradio.com/); server source remains private during the pilot |
| Catnap Studio | This overview, website, roadmap and future operator/studio design | Public documentation; an all-in-one Studio is planned |

## AIU Inbox and show preview

Choose the intended LP or AP inbox and read **Pending entries oldest-first**. Each submission keeps its own identity, Suno/YouTube links, source preference, warning flag and uploader context. Uploader notes remain in the host controls. Reading does not change inbox statuses. A separate confirmed Decline sends “Only one song at a time, please.” and verifies the result. Nothing is auto-declined or marked Accepted/Played.

A YouTube-only submission remains a real entry in the managed running order without manufacturing a Suno placeholder. When both source links are supplied, YouTube is preferred internally. A Suno playlist can contain the usable Suno tracks; the mixed show queue also retains its external entries. Missing or unavailable media stays visible rather than silently becoming a different song.

The managed queue preserves host moves and Hold/Release across refreshes. Held songs stay out of its managed Suno playlist. With repeat holding enabled, finishing an uploader's song releases just their next submission at the current tail; a third waits for the second to finish. Explicit manual Release stays released, and Move can arrange an approved multipart chain. Actual played history followed by the intended upcoming order is verified in the managed playlist while current audio and unrelated tracks are protected. Held rows and repeated uploaders have labels/colour. Inbox-only remains the simple FIFO creator. Per-person AP quotas and Accepted-as-Played orchestration remain upstream work.

**LP is manual:** load quietly, then press Play separately. **AP autoplay is optional.** A cold Suno player may briefly prepare while forcibly muted after explicit Play; audible playback requires the selected song/source to verify. Pause, a changed selection or timeout cancels preparation. Quiet Load does not prepare or start audio. Requested content warnings appear on load/advance with an adjustable timeout. Copy now playing uses the selected source and the submission uploader's `@credit`. A valid numeric inbox uploader ID becomes a Discord user mention; otherwise the text uses an `@name` credit or Unavailable. Review the intended mention and send the message yourself. The preview neutralizes mass mentions and does not consult a private identity correlation sheet. Clipboard preparation is not automatic Discord posting.

These deterministic queue functions do not require an LLM or the advanced hosting bot. The optional Suno connection and desktop companion have their own setup steps. Managed removal/reordering needs the companion introduced with 0.8.0, using the existing OAuth scopes. The companion is unchanged in 0.8.1; users already on 0.8.0 do not need to reinstall it. Individual Radio keys are issued by AIU Agents/Admins through the [key manager](https://listen.catnapradio.com/hosts/). The preview does not remove the need for host content/rights review or a between-shows rehearsal.

## Advanced hosting

The private advanced preview shares Theatre **0.8.1** and uses compatible **Host Controls 0.4.8**. Host Controls 0.4.8 leaves lyric collection to Theatre. The host-control extension retains its amber fader icon; Theatre uses the purple/teal headphone cat. Its new default is Managed Inbox. The older bot/backend/Suno-only workflow is retained behind a deliberate Legacy mode, with ownership coordination to keep two queue writers from running the same show. Prepared code and fixture checks do not mean this preview has been installed or live-verified in the maintainer's profile.

Ina's **full hosting package** remains a larger workflow: LP/AP playlists and artwork, LP artwork with the current artist lineup, and a dark LP cue PDF with artwork, summary/index and individual track cues/review. AP artwork normally has no fixed cast list or cue PDF. The simpler managed queue does not automatically generate that artwork/PDF package. Normal AIU intake uses the uploader/inbox; emergency or non-AIU chat intake is an explicit exception.

More complete bot announcements, verified regional support banners, avatar reactions and live-avatar staging remain [roadmap work](docs/REQUEST-SCOPE.md). The new managed queue supersedes the older placeholder approach for its own mixed-source shows; a deliberately selected legacy physical-Suno workflow has separate limitations.

Private hosting/simulcast source, pairing credentials, event records, uploader exports and name correlations are not public downloads.

## Audio listener

The live listener is **0.1.7**, with larger artwork bounded to 400 pixels and responsive to the window. It offers stereo Opus Live audio with a **256 kbps target** and buffered **320 kbps MP3 Radio**. Current artwork/title, last played and upcoming context come from the publishing tab when available. A longer visible-playlist view can show estimates when timing is known; it is not Suno's complete internal queue. Radio audio can lag the displayed host metadata.

The existing listener metadata contract is Suno-based. Managed YouTube playback must not be advertised as a verified Suno now-playing entry. Broader mixed-source listener metadata and playback/HQ coexistence remain rehearsal work.

The host confirmed Android Radio continues through app switching and a short screen-lock test. Other devices, longer sessions, calls and Bluetooth still need their own checks. Mobile and network behavior vary; no exact universal latency is promised. The listener itself requires no publish key or Suno login.

## Roadmap and references

- [Current versions and release notes](docs/RELEASES.md)
- [Roadmap and remaining acceptance](docs/ROADMAP.md)
- [Complete requested scope](docs/REQUEST-SCOPE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Hosting/cue workflow](docs/HOST-WORKFLOW.md)
- [Downloads, screenshots and evidence](docs/DELIVERABLES.md)
- [November 12 technical update](docs/UPDATES-2026-11-12.md)
- [GitHub, visibility and maintenance](docs/GITHUB-GUIDE.md)

## Use and sharing

First-party Catnap code and documentation use [PolyForm Noncommercial 1.0.0](LICENSE). Commercial use outside its permitted purposes requires separate written permission from Ina. [Branding and third-party rights](LICENSING.md) remain separate. No identity spreadsheet, inbox export, private research or deployment credentials are published here.

This repository's `website/` directory is the source for [CatnapRadio.com](https://catnapradio.com/). A source update and a deployed website are separate recorded steps. The 0.5.0 Store beta is pending review. There is no downloadable all-in-one Studio yet.
