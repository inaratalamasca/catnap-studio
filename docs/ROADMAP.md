# Roadmap

Updated November 16, 2026. **Theatre Lite 0.5.0 remains a separate active presentation-only edition with unchanged files and no Inbox/helper requirement.** The public **0.8.1 development preview** continues three packages: AIU Theatre + Inbox, Inbox-only and Radio-only. Radio-only can accompany Lite without Inbox or a desktop helper; the creators retain their own-account Suno companion setup. The **0.5.0 Chrome Web Store beta is pending review**. Advanced Theatre 0.8.1 and compatible Host Controls 0.4.8 are private previews; listener 0.1.7 and metadata 0.2.1 are operational during broadcasts. Prepared code, Store submission, publication, installation and live acceptance are separate states.

The host confirmed working **0.8 Radio broadcasting on November 16** after an initial startup timeout; its cause remains unproven. Fair rotation, playlist ordering, manual Decline, the 0.8.1 hotfixes and advanced live acceptance still require their own rehearsal.

The 0.8.1 fixes keep selection in place, replace artwork cleanly with YouTube video, and allow Theatre reopening while live. The desktop Suno companion is unchanged from 0.8.0. Hosts already using the 0.8.0 companion do not need to reinstall it for 0.8.1. Older companions need the 0.8 package update for managed removal/reordering; OAuth scopes are unchanged. Radio-only needs no companion.

## 0 — Containment and public boundaries

Theatre, this overview/website and the inbox walkthrough are public. Advanced hosting and simulcast source remain private during the pilot. Preserve operating locations, private event/configuration data and original reference research outside Git. Maintain noncommercial first-party terms and separate branding rights.

## 1 — Presentation and member testing

The active Theatre Lite 0.5.0 baseline includes two/three-column and artwork-focus layouts, contained artwork, lyric controls, visible playlist rows, separate settings, banners/local media, a lounge and optional HQ broadcasting/visualizer. Keep checking tagged and plain lyrics, Unicode, missing lyrics/artwork, animated artwork, narrow/1080p layouts, real song changes and native source changes. A successful fixture does not establish all current Suno selectors or full-show behavior.

The 0.5.0 Store beta submission is awaiting review; there is no published Store install link. Continue accessibility/privacy/listing work and real member rehearsals independently. Firefox requires its own port and testing.

## 2 — AIU Inbox and mixed-source preview

The separate AIU Inbox 0.8.1 preview retains labeled top readiness dots and per-step setup status; ordinary use leaves those indicators grey/inactive, and the host confirmed 0.6.10 Dev1 activation, status indicators and managed lyrics on November 16. Broader workflow checks remain separate. It provides an optional deterministic LP/AP workflow: read the intended Pending inbox oldest-first, retain submission identity/context/source flags, create or reconcile a Suno playlist, and keep external entries in the managed running order. The Inbox-only variant creates playlists without presentation playback or publishing. An LLM is not required for these queue operations.

Managed YouTube entries replace the need to manufacture placeholder songs for this workflow. Prefer the supplied YouTube alternative when both links exist. Preserve explicit Load/Play for LP; AP autoplay remains optional. Requested content-warning flags produce timed overlays. Notes stay in host controls. Copy now playing uses the selected source and submission uploader's `@credit` for manual review/send; it does not require a private identity map.

The maintainer reported own-account OAuth, playlist creation and clean Suno/HQ playback in 0.6.2. The 0.6.3 trial exposed a Play-control lookup failure; 0.6.4 found the row and loaded quietly but timed out waiting for the selected native song. The 0.6.5 retry reported “Target matched, audio not found”. Version 0.6.6 distinguishes the active music element from Suno’s silent helper, retains bounded forced-muted preparation only after explicit Play, and verifies the selected song/source before audible playback. Pause, changed selection and timeout cancel the pending start; quiet Load remains silent. **The host confirmed the standalone 0.6.6 manual LP sequence: Play song 1 → held ending → Load Next paused → Play song 2.** That trial exposed missing managed lyrics. The 0.6.7 host retry still showed missing lyrics after Reload. On November 16, the host confirmed manual 0.6.10 activation in Dev1, working status indicators and managed lyrics. The repeated-click intake fix and playlist updates remain pending a real check. Version 0.6.9 groups matching Presentation/Inbox controls, identifies Inbox Show versus Suno Playlist and makes Inbox Submissions counts/read time prominent. Mixed-source, AP, advanced live integration and Discord/HQ checks remain separate. Rehearse manual Load without audio, separate Play, end-of-song behavior, AP autoplay/append, YouTube transitions, blocked embeds/autoplay, warning timeout/repeat, rebind/close/reopen, authorization recovery and Discord/HQ coexistence. Keep one show writer active.

Supported uploader integration still needs a maintained contract with Kai. Pending discovery/read uses the selected signed-in uploader page read-only. A separate confirmed manual Decline is implemented; automatic Decline, Accepted-as-Played and cleanup remain outside that read-only intake.

The 0.8.1 preview retains source-only Radio status for Suno/AIU party pages, green AIU logo treatment, one gear opening the operator controls, explicit mode/error status, and YouTube window view on Play with a red badge/Loaded staging label. The host’s working 0.8 Radio broadcast does not establish the newer hotfix, fair-queue, Decline or advanced checks; the earlier Dev1 status/lyrics confirmation remains specific to 0.6.10.

## 3 — Advanced controller coordination and full hosting

The private advanced 0.8.1 Theatre reuses the managed workflow. Host Controls 0.4.8 leaves lyric collection to Theatre and defaults to Managed Inbox; the older bot/backend/Suno queue remains behind deliberate Legacy mode. The pinned extensions coordinate queue ownership so that mode changes stop new legacy work, drain pending operations and release ownership before the other writer starts. Fixture evidence must be followed by a controlled live rehearsal; old installed versions do not acquire that protection by receiving new shortcuts.

Ina's full LP package still includes a verified ordered playlist, artwork with the current artist lineup, and the dark cue PDF with cover/artwork, summary/index and individual track review/cues. AP normally needs its ordered playlist and artwork without a fixed artist list or cue PDF. The managed queue is not automatic artwork/cue production or a substitute for content, rights and platform review.

Retain the deliberately selected legacy physical-Suno placeholder workflow separately from new managed mixed-source shows. Complete broader bot announcements, support banners using verified regional resources, fair-play/session adapter acceptance, avatar reaction libraries/zoom and possible live avatars without creating a second queue writer.

## 4 — Audio listener and Studio experiments

Listener 0.1.7 uses larger responsive artwork (up to 400 pixels), low-delay stereo Opus Live at a 256 kbps target and buffered 320 kbps MP3 Radio. Continue testing real latency, drift, scale, reconnect, Wi-Fi/cellular and mobile app switching/screen lock/calls/Bluetooth. Suno-based public metadata must not mislabel a YouTube entry; broader mixed-source listener context remains work.

Prototype an operator/program split using the existing Theatre and proven OBS/capture/encoding components. Keep latency, media rights and full-show recovery separate from successful encoding. A hosted multi-user service or all-in-one Studio is not promised by the local audio pilot.
