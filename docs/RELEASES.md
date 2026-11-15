# Current versions · November 15, 2026

| Component | Version / state | Where to start |
| --- | --- | --- |
| Standalone Theatre | 0.5.0 early access, including toolbar icons | [Release and download](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) |
| Integrated Theatre | 0.5.0; visual bridge protocol 1.2.0 retained | Private advanced hosting project |
| Host Controls | 0.4.6.2, amber fader icon | Private advanced hosting project; requires host configuration |
| Audio listener | 0.1.6 pilot | [Listen during a broadcast](https://listen.catnapradio.com/) |
| Metadata service | 0.2.1 | Private simulcast pilot |
| Inbox playlist walkthrough | LP/AP agent guide with optional Advanced pings | [Read the guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) |
| Full Studio | Design stage | [Roadmap](ROADMAP.md) |

The November 15 housekeeping pass consolidated the saved implementation changes into main, refreshed overviews/references and established noncommercial terms. Runtime JavaScript and installed profiles were not changed by that pass. The maintainer reported working standalone 0.5.0 use and advanced 0.5.0/controller connection; these observations have narrower scope than every item in the acceptance lists.

Theatre release checks cover maintained unit/DOM tests, JavaScript and manifest references, publication guards and package contents. Hosting retains separately documented inherited relay fixture failures; those are not silently marked fixed. iPhone/background/call/Bluetooth and prolonged full-show recovery work remain explicit open acceptance areas.

A release ZIP has a SHA-256 companion. It includes only the extension, public documentation and license/notices. It does not contain a publish token, server pairing, private identities or inbox records. Browser-store submission is a separate future task.
