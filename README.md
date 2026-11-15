# Catnap Radio · projects and guides

Music tools for AI:Underground listening parties, with Ina & Len.

**[Listen](https://listen.catnapradio.com/) · [CatnapRadio.com](https://catnapradio.com/) · [Download Theatre 0.5.0](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) · [Simple inbox walkthrough](https://github.com/inaratalamasca/aiu-inbox-playlist-guide)**

## Start here

- **Listening?** Open the [web player](https://listen.catnapradio.com/) and tap Play. Live aims for low delay; Radio is buffered for mobile/background listening. In Discord, mute the shared stream's audio and keep individual voices on.
- **Hosting with Suno?** Start with [standalone Theatre](https://github.com/inaratalamasca/catnap-theatre). It displays artwork, lyrics, visible playlist rows, banners and local media. Its settings open in a separate window. No bot, AI or Catnap server is required for presentation.
- **Keeping an AP/LP playlist updated?** Give your agent the [simple inbox guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide). It starts with one verified addition, uses the intended Pending inbox oldest-first and checks about every five minutes during an active watch.
- **Developing or reporting a bug?** Use the relevant project's Issues. See the [GitHub guide](docs/GITHUB-GUIDE.md) and [contribution notes](CONTRIBUTING.md).

## Projects

| Project | What it does | Availability |
| --- | --- | --- |
| [Catnap Theatre](https://github.com/inaratalamasca/catnap-theatre) | Standalone Suno presentation, separate controls, visual overlays, optional background bars and music publishing | Public source and 0.5.0 early-access download for Chrome/Brave |
| [AIU inbox playlist guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) | Minimal agent instructions for LP/AP playlists and optional now-playing assistance | Public guide; actual tool/browser access must be verified |
| Advanced Radio Hosting | Integrated Theatre, Host Controls, persistent requests and show preparation | Private development; integrated Theatre 0.5.0 and Host Controls 0.4.6.2 loaded/connected in the maintainer's profile |
| Catnap Simulcast | Music-only relay and web player, alongside separate Discord voices | [Listener available during broadcasts](https://listen.catnapradio.com/); server source remains private during the pilot |
| Catnap Studio | This overview, website, roadmap and future operator/studio design | Public documentation; an all-in-one studio is planned |

## Advanced hosting

The advanced suite is separate from standalone Theatre. Its integrated Theatre shares the 0.5.0 presentation and retains the host-controller bridge. The compatible Host Controls version is **0.4.6.2**; the host-control extension has an amber fader icon, while Theatre uses the purple/teal headphone cat.

The full hosting workflow is intended to produce LP/AP playlists and artwork, plus a dark cue PDF with cover and summary for Ina's LP package. Normal AIU intake uses the uploader/inbox. Emergency or non-AIU chat intake is an explicit exception. Requested uploader warnings, external-video placeholders/preferred playback, avatar reactions and live-avatar staging remain [roadmap work](docs/REQUEST-SCOPE.md); presentation parity does not mean every advanced feature is complete.

The source is private while configuration boundaries and full-show behavior are being stabilized. Private operation data, pairing credentials and name correlations are never part of the public tools.

## Audio listener

The listener offers stereo Opus Live audio with a 256 kbps target and buffered 320 kbps MP3 Radio. Current artwork/title, last played and upcoming context come from the publishing tab. A longer visible-playlist view can show estimates when timing is known. It is not Suno's complete internal queue. Radio audio can lag the displayed host metadata.

The host confirmed Android Radio continues through app switching and a short screen-lock test. Other devices, longer sessions, calls and Bluetooth still need their own checks. Mobile and network behavior vary; no exact universal latency is promised. The listener itself requires no publish key or Suno login.

## Roadmap and references

- [Current versions and release notes](docs/RELEASES.md)
- [Roadmap and remaining acceptance](docs/ROADMAP.md)
- [Complete requested scope](docs/REQUEST-SCOPE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Hosting/cue workflow](docs/HOST-WORKFLOW.md)
- [Screenshots and evidence](docs/DELIVERABLES.md)
- [November 12 technical update](docs/UPDATES-2026-11-12.md)
- [GitHub, visibility and maintenance](docs/GITHUB-GUIDE.md)

## Use and sharing

First-party Catnap code and documentation use [PolyForm Noncommercial 1.0.0](LICENSE). Commercial use outside its permitted purposes requires separate written permission from Ina. [Branding and third-party rights](LICENSING.md) remain separate. No identity spreadsheet, inbox export, private research or deployment credentials are published here.

This repository's `website/` directory is the source for [CatnapRadio.com](https://catnapradio.com/). A source update and a deployed website are separate recorded steps. There is no browser-store release or downloadable all-in-one Studio yet.
