# Catnap Radio · projects and guides

Music tools for AI:Underground listening parties, with Ina & Len.

**[Listen](https://listen.catnapradio.com/) · [CatnapRadio.com](https://catnapradio.com/) · [Try Theatre + Inbox 0.6.6 preview](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.6.6-preview) · [Simple inbox walkthrough](https://github.com/inaratalamasca/aiu-inbox-playlist-guide)**

## Start here

- **Listening?** Open the [web player](https://listen.catnapradio.com/) and tap Play. Live aims for low delay; Radio is buffered for mobile/background listening. In Discord, mute the shared stream's audio and keep individual voices on.
- **Hosting with artwork, lyrics and a managed show?** Try the [Theatre + Inbox 0.6.6 preview](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.6.6-preview). It combines the presentation with optional LP/AP inbox intake, playlist creation and a mixed Suno/YouTube show queue. LP uses separate Load and Play actions; AP autoplay is optional.
- **Just creating an inbox playlist?** Choose the **Inbox-only 0.6.6 preview** on the same release page. It prepares playlists without Theatre playback, streaming or a co-host bot. No LLM is required for the managed playlist workflow; follow the included guide for your own Suno connection.
- **Using an agent instead?** The [simple inbox guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) remains available. Verify tool access, start with one saved addition and use the intended Pending inbox oldest-first during an explicitly requested watch.
- **Developing or reporting a bug?** Use the relevant project's Issues. See the [GitHub guide](docs/GITHUB-GUIDE.md) and [contribution notes](CONTRIBUTING.md).

The 0.6.6 downloads are **development previews** for rehearsal. The maintainer reported own-account Suno authorization, playlist creation and clean Suno/HQ audio in 0.6.2. The 0.6.3 trial staged an LP entry but missed its native Play control. In 0.6.4 the row was found and quiet Load worked, but Play timed out because Suno did not load the selected song. The 0.6.5 retry reported “Target matched, audio not found”. Version 0.6.6 distinguishes the active music player from Suno’s silent helper while retaining bounded muted preparation. The host confirmed the standalone 0.6.6 manual LP sequence: Play song 1, hold at its ending, Load Next paused, then Play song 2. Mixed-source transitions, AP, advanced live integration and Discord/HQ checks remain separate. This is not full-show acceptance. The older [0.5.0 presentation-only release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) remains available. The Chrome Web Store **0.5.0 beta is pending review**; it is not a published Store listing.

## Projects

| Project | What it does | Availability |
| --- | --- | --- |
| [Catnap Theatre + Inbox](https://github.com/inaratalamasca/catnap-theatre) | Presentation, separate controls, overlays, optional audio publishing and a managed LP/AP Suno/YouTube queue | Public source and **0.6.6 preview** downloads for combined Theatre + Inbox or Inbox-only; older 0.5.0 presentation-only release retained |
| [AIU inbox playlist guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) | Minimal agent instructions for LP/AP playlists and optional now-playing assistance | Public guide; actual tool/browser access must be verified |
| Advanced Radio Hosting | Shared Theatre, compatible Host Controls, bot/backend integration and full show preparation | Private **Theatre 0.6.6 / Host Controls 0.4.7 preview**; live rehearsal remains pending |
| Catnap Simulcast | Music-only relay and web player, alongside separate Discord voices | [Listener 0.1.7 available during broadcasts](https://listen.catnapradio.com/); server source remains private during the pilot |
| Catnap Studio | This overview, website, roadmap and future operator/studio design | Public documentation; an all-in-one Studio is planned |

## Managed inbox and show preview

Choose the intended LP or AP inbox and read **Pending entries oldest-first**. Each submission keeps its own identity, Suno/YouTube links, source preference, warning flag and uploader context. Uploader notes remain in the host controls. The preview does not accept, release, delete or clean up inbox entries.

A YouTube-only submission remains a real entry in the managed running order without manufacturing a Suno placeholder. When both source links are supplied, YouTube is preferred internally. A Suno playlist can contain the usable Suno tracks; the mixed show queue also retains its external entries. Missing or unavailable media stays visible rather than silently becoming a different song.

**LP is manual:** load quietly, then press Play separately. **AP autoplay is optional.** A cold Suno player may briefly prepare while forcibly muted after explicit Play; audible playback requires the selected song/source to verify. Pause, a changed selection or timeout cancels preparation. Quiet Load does not prepare or start audio. Requested content warnings appear on load/advance with an adjustable timeout. Copy now playing uses the selected source and the submission uploader's `@credit`. A valid numeric inbox uploader ID becomes a Discord user mention; otherwise the text uses an `@name` credit or Unavailable. Review the intended mention and send the message yourself. The preview neutralizes mass mentions and does not consult a private identity correlation sheet. Clipboard preparation is not automatic Discord posting.

These deterministic queue functions do not require an LLM or the advanced hosting bot. The optional Suno connection and desktop companion have their own setup steps. The preview does not remove the need for host content/rights review or a between-shows rehearsal.

## Advanced hosting

The private advanced preview shares Theatre **0.6.6** and uses compatible **Host Controls 0.4.7**. The host-control extension retains its amber fader icon; Theatre uses the purple/teal headphone cat. Its new default is Managed Inbox. The older bot/backend/Suno-only workflow is retained behind a deliberate Legacy mode, with ownership coordination to keep two queue writers from running the same show. Prepared code and fixture checks do not mean this preview has been installed or live-verified in the maintainer's profile.

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
