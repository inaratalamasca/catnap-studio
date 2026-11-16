# Current versions · November 16, 2026

The 0.8.1 host follow-up found that ordinary Suno selections stayed in place, but a paired YouTube entry still reached the top, apparently after completion. The host also could not find the full-window video exit before it ended. The 0.8.2 changes address those remaining cases; their live acceptance is pending.

## Public downloads

| Component | Version / state | Where to start |
| --- | --- | --- |
| Theatre Lite | **0.5.0 active presentation-only edition**, unchanged package for ordinary Suno/non-AIU hosts; no Inbox or playlist helper | [Original release/setup](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0) · [Lite ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.5.0/Catnap-Theatre-v0.5.0.zip) · [SHA256](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.5.0/Catnap-Theatre-v0.5.0.zip.sha256) |
| AIU Theatre + Inbox | **0.8.2 development preview** — presentation plus optional inbox/playlist and mixed-source show controls | [Preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.2-preview) · [Combined ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.8.2-preview/Catnap-Theatre-Inbox-Dev-v0.8.2.zip) |
| Radio-only | **0.8.2 development preview** — publish a Suno or AIU party player tab without Inbox or desktop helper | [Preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.2-preview) · [Radio-only ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.8.2-preview/Catnap-Radio-Dev-v0.8.2.zip) |
| Inbox-only | **0.8.2 development preview** — create playlists without Theatre playback or broadcasting | [Same preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.2-preview) · [Inbox-only ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.8.2-preview/Catnap-Inbox-Dev-v0.8.2.zip) |
| Chrome Web Store beta | **0.5.0 submitted; pending review** | No published Store listing is claimed; use the release's setup instructions |
| Inbox playlist walkthrough | LP/AP agent guide with optional Advanced pings | [Read the guide](https://github.com/inaratalamasca/aiu-inbox-playlist-guide) |

The 0.8.2 preview release contains three packages: Theatre + Inbox, Inbox-only and Radio-only. The two creators include desktop companion setup for Suno playlist operations; Radio-only needs no helper. It can accompany Theatre Lite. Choose either the integrated publisher or Radio-only for the show. Theatre Lite remains the separate, unchanged 0.5.0 release; its original asset name is retained. Install only the chosen variant for the intended workflow. Read the package guide and verify its checksum before a deliberate between-show installation; publishing a release does not reload an installed extension.

## Private development and live listener

| Component | Version / state | Availability |
| --- | --- | --- |
| Integrated advanced Theatre | **0.8.2 preview**, shared managed workflow and preserved visual bridge | Private hosting project; prepared source is not live activation |
| Host Controls | **0.4.8 preview**, Managed/Legacy ownership coordination and Theatre-owned lyrics | Private hosting project; configured testing and live rehearsal remain separate |
| Audio listener | **0.1.7 live pilot**, responsive artwork capped at 400 pixels | [Listen during a broadcast](https://listen.catnapradio.com/) |
| Metadata service | **0.2.1** | Private simulcast pilot |
| Full Studio | Design stage | [Roadmap](ROADMAP.md) |

Advanced source/downloads, paired configurations, identity records and runtime keys remain private. Public project overviews describe their purpose without publishing those operational materials.

## Stable order and an easier video exit in 0.8.2

- Choosing or finishing a song keeps its row in place in Theatre and the control panel.
- Leave full-window video while it is playing using a small, visible Exit video button.
- Reopen Theatre while live without stopping the broadcast.

Playback history is retained separately; an explicitly managed Suno playlist can still reflect actual played order. These changes need a new host rehearsal.

The host confirmed working **0.8 Radio broadcasting on November 16** after an initial startup timeout; its cause remains unproven. Fair rotation, playlist ordering, manual Decline, the 0.8.2 hotfixes and advanced live acceptance still require their own rehearsal.

The desktop Suno companion is unchanged from 0.8.0. Hosts already using the 0.8.0 companion do not need to reinstall it for 0.8.2. Older companions need the 0.8 package update for managed removal/reordering; OAuth scopes are unchanged. Radio-only needs no companion.

## Retained preview features

- Radio supports Suno and the AIU party player. Only the captured source tab shows On Air; Theatre’s AIU logo becomes green while that source is actually live. Starting/reconnecting/error states are not shown as live.
- One gear opens Presentation controls, with separate Radio and Inbox buttons. The top status names Inbox or Suno playlist mode and goes green only for verified readiness without current playback or command errors.
- Managed YouTube Play fills the Theatre viewport, without browser fullscreen. A red YouTube badge and a Loaded label distinguish the source and quiet staging.
- Compact loaded/playing cards place artwork beside title, credit and warnings; click the thumbnail to copy its clean public image URL. Inbox-only does not fetch remote thumbnails.
- Clean-install Theatre + Inbox can offer a nonblocking stream-name prompt; upgrades and existing name preferences are not prompted. Catnap Radio remains the default.
- Radio token remembering is on by default and bound to the chosen relay origin. Explicit Start after permission or an explicit user choice/change saves locally; opening the panel does not migrate an active session key. Session-only and Forget remove the durable copy without stopping an active broadcast. Normal same-ID updates can retain this local storage; removal or profile changes are not guaranteed to do so, and it is not an encrypted vault.
- The source-only Radio result above applies to the host’s 0.8 broadcast. The earlier Dev1 activation/status/managed-lyrics confirmation applies to 0.6.10; broader workflow and recovery checks remain separate.

## Fair queue and AIU Inbox features

- Preserve host moves and Hold/Release across refreshes. Held songs stay out of the managed Suno playlist.
- Real completion releases only the next submission from that uploader at the current ready tail; later repeats keep waiting. Manual Release stays released.
- Theatre and control-panel rows stay in place through selection, replay and completion. The managed Suno playlist can follow separately recorded actual played history and the intended upcoming order when synchronized.
- Manual Decline uses a separate confirmation and verifies the uploader result. Nothing is auto-declined or marked Accepted/Played. An uncertain result stays held until read-only recovery verifies it.
- Labeled Suno/Inbox readiness dots at the top and a status for each setup step. In ordinary use of the Inbox edition the dots are grey/inactive; Theatre Lite has no Inbox/helper setup. The host confirmed Dev1 activation and working status indicators on November 16; broader per-step/recovery cases remain separate.
- Presentation and Inbox controls use matching button styles and clear groups. The displayed list is labeled Inbox Show or Suno Playlist; Inbox Submissions shows Pending/held counts and the read time.
- Optional read-only LP/AP Pending inbox intake in FIFO order, preserving source links/preferences, uploader context and warning flags.
- Real YouTube-only entries in a managed mixed-source queue without Suno placeholders; YouTube preference when both links are provided.
- Separate manual Load and Play for LP. AP autoplay is optional; content warnings show on load/advance with an adjustable timeout.
- Copy now playing uses the selected source and a valid numeric inbox uploader ID as a Discord user mention. Its fallback is one `@name` credit or Unavailable; mass mentions are neutralized. No private identity map is consulted, and hosts review/send manually.
- A separate Inbox-only creator; no LLM or advanced bot is required for deterministic playlist operations. The optional Suno connection has its own desktop setup.
- Managed Suno lyrics keep plain-text line breaks, prefer the selected song’s own details panel and offer Reload. Old lyrics clear on a quiet song change or YouTube selection; managed lyrics were confirmed working in Dev1 on November 16. Broader transition/recovery cases remain separate.
- Active music selection keeps Suno’s silent helper out of playback ownership. Bounded muted preparation after explicit Play is followed by selected-song/source verification before audible playback. Quiet Load does not prepare or start audio. Pause, stop, changed selection and timeout cancel pending preparation.

The maintainer reported own-account Suno authorization, playlist creation and clean Suno/HQ audio with **0.6.2**. In **0.6.3**, quiet staging worked but native Play lookup failed. The **0.6.4** live trial found the row and loaded quietly, then Play timed out because Suno did not load the selected song. The **0.6.5** retry reported “Target matched, audio not found”. Version **0.6.6** distinguished the active music element from Suno’s silent helper. **The host confirmed the standalone 0.6.6 manual LP sequence: Play song 1 → held ending → Load Next paused → Play song 2.** The trial exposed missing managed lyrics. The **0.6.7** host retry still showed missing lyrics after Reload. On **November 16**, the host confirmed manual **0.6.10 activation in Dev1**, working status indicators and managed lyrics. The repeated-click intake fix and playlist updates remain pending a real check. Version **0.6.9** adds the grouped controls, source labels and submission summary described above. Mixed-source transitions, AP, advanced live integration and Discord/HQ checks remain separate.

An isolated Chromium reproduction showed 0.6.7 rejecting plain lyrics when rendered whitespace collapsed their line breaks. The retained 0.6.8 correction preserves raw lyric line breaks and prefers the selected song’s local details panel over unrelated page content. The November 16 Dev1 confirmation adds actual activation/status/managed-lyrics evidence; fixture checks do not establish the remaining real-Suno workflow or full-show acceptance. Mixed-source transitions, re-entry/rebinding, AP watching, Discord/HQ coexistence and full-show recovery still need rehearsal.

The November 15 housekeeping pass previously consolidated the saved 0.5.0 work. The maintainer's successful standalone 0.5.0 and advanced 0.5.0/controller connection observations remain historical evidence, not acceptance of every newer preview feature. Inherited advanced relay fixture failures remain separately documented; they are not silently marked fixed by presentation parity.

The unchanged Theatre Lite ZIP has SHA256 `5464d3cb36cdfa3aa22b5752518847dbe0cfe329d9e26ab15901bdf5c649b9f8`, verified against the existing sidecar. Its upstream filename and manifest remain unchanged; Theatre Lite is the public choice label.

## Package boundaries

A release ZIP contains only the intended extension, public setup/documentation, companion material and license/notices. It contains no publish token, private server pairing, identity correlations, inbox export or event records. First-party noncommercial terms and separate branding rights remain in force. Store review, a wider release and installing a new build are distinct steps.
