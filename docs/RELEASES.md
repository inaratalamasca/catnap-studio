# Current versions · November 15, 2026

## Public downloads

| Component | Version / state | Where to start |
| --- | --- | --- |
| Theatre + Inbox | **0.6.4 development preview** — presentation plus optional inbox/playlist and mixed-source show controls | [Preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.6.4-preview) · [Combined ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.6.4-preview/Catnap-Theatre-Inbox-Dev-v0.6.4.zip) |
| Inbox-only | **0.6.4 development preview** — create playlists without Theatre playback or broadcasting | [Same preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.6.4-preview) · [Inbox-only ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.6.4-preview/Catnap-Inbox-Dev-v0.6.4.zip) |
| Older presentation-only Theatre | **0.5.0 early access** | [Older release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) |
| Chrome Web Store beta | **0.5.0 submitted; pending review** | No published Store listing is claimed; use the release's setup instructions |
| Inbox playlist walkthrough | LP/AP agent guide with optional Advanced pings | [Read the guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) |

The preview release contains the two public extension variants and their included desktop setup material. Install only the chosen variant for the intended workflow. Read the package guide and verify its checksum before a deliberate between-show installation; publishing a release does not reload an installed extension.

## Private development and live listener

| Component | Version / state | Availability |
| --- | --- | --- |
| Integrated advanced Theatre | **0.6.4 preview**, shared managed workflow and preserved visual bridge | Private hosting project; prepared source is not live activation |
| Host Controls | **0.4.7 preview**, Managed/Legacy ownership coordination | Private hosting project; configured testing and live rehearsal remain separate |
| Audio listener | **0.1.7 live pilot**, responsive artwork capped at 400 pixels | [Listen during a broadcast](https://listen.catnapradio.com/) |
| Metadata service | **0.2.1** | Private simulcast pilot |
| Full Studio | Design stage | [Roadmap](ROADMAP.md) |

Advanced source/downloads, paired configurations, identity records and runtime keys remain private. Public project overviews describe their purpose without publishing those operational materials.

## Current preview features

- Optional read-only LP/AP Pending inbox intake in FIFO order, preserving source links/preferences, uploader context and warning flags.
- Real YouTube-only entries in a managed mixed-source queue without Suno placeholders; YouTube preference when both links are provided.
- Separate manual Load and Play for LP. AP autoplay is optional; content warnings show on load/advance with an adjustable timeout.
- Copy now playing uses the selected source and a valid numeric inbox uploader ID as a Discord user mention. Its fallback is one `@name` credit or Unavailable; mass mentions are neutralized. No private identity map is consulted, and hosts review/send manually.
- A separate Inbox-only creator; no LLM or advanced bot is required for deterministic playlist operations. The optional Suno connection has its own desktop setup.
- Updated native Play lookup for Suno's current accessible control and track-row structure, while retaining the earlier quiet LP staging correction.

The maintainer reported own-account Suno authorization, playlist creation and clean Suno/HQ audio with **0.6.2**. During the live **0.6.3** trial, LP Load and quiet staging worked, but the later Play action could not locate Suno's current control. The **0.6.4 native Play correction still needs a renewed live rehearsal**. The public 0.6.4 source passed **172 maintained checks**. These results do not establish mixed-source transitions, background/native playback, re-entry/rebinding, AP watching, Discord/HQ coexistence or full-show recovery.

The November 15 housekeeping pass previously consolidated the saved 0.5.0 work. The maintainer's successful standalone 0.5.0 and advanced 0.5.0/controller connection observations remain historical evidence, not acceptance of every newer preview feature. Inherited advanced relay fixture failures remain separately documented; they are not silently marked fixed by presentation parity.

## Package boundaries

A release ZIP contains only the intended extension, public setup/documentation, companion material and license/notices. It contains no publish token, private server pairing, identity correlations, inbox export or event records. First-party noncommercial terms and separate branding rights remain in force. Store review, a wider release and installing a new build are distinct steps.
