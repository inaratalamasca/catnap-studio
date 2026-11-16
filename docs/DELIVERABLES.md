# Downloads, screenshots and host decisions

## Current public package choices

**Theatre Lite 0.5.0** is the active presentation-only choice for ordinary Suno and non-AIU hosts. Use its [unchanged ZIP](https://github.com/inaratalamasca/catnap-theatre/releases/download/v0.5.0/Catnap-Theatre-v0.5.0.zip) and [original setup/checksum](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.5.0); no Inbox or Suno playlist helper is required.

For the three preview packages, use the [0.8.1 preview release](https://github.com/inaratalamasca/catnap-theatre/releases/tag/v0.8.1-preview) to choose:

- **AIU Theatre + Inbox** — presentation plus optional LP/AP inbox/playlist creation and managed Suno/YouTube show controls.
- **Radio-only** — publish Suno or AIU party audio without Inbox or a desktop helper; can run alongside Theatre Lite.
- **Inbox-only** — playlist creation without Theatre playback, broadcasting or an advanced hosting bot.

All three 0.8.1 packages are development previews with included setup instructions and noncommercial/license notices. The host confirmed working 0.8 Radio broadcasting on November 16; the 0.8.1 fixes, fair rotation, playlist ordering, manual Decline and advanced live verification remain pending. No LLM is required for deterministic managed-queue operations. Suno authorization/playlist creation in the two creators uses the host’s own account and desktop companion setup. Radio publishing itself needs no Suno helper. Keep private pairing, publish keys and inbox records out of packages and screenshots.

The desktop Suno companion is unchanged from 0.8.0. Hosts already using the 0.8.0 companion do not need to reinstall it for 0.8.1. Older companions need the 0.8 package update for managed removal/reordering; OAuth scopes are unchanged. Radio-only needs no companion.

The **0.5.0 Chrome Web Store beta is pending review**; no published Store listing is claimed. Private advanced Theatre 0.8.1 / Host Controls 0.4.8 source and paired downloads are not public deliverables.

The 0.6.2 own-profile authorization, playlist creation and clean Suno/HQ audio reports are useful smoke evidence. The 0.6.3 trial missed the native Play control; 0.6.4 found the row and quiet Load worked, but Play timed out waiting for the selected song. The 0.6.5 host retry reported “Target matched, audio not found”. Version 0.6.6 corrected active-music versus silent-helper selection; the host confirmed the standalone sequence Play song 1 → held ending → Load Next paused → Play song 2. The trial exposed missing managed lyrics; the 0.6.7 host retry still showed missing lyrics even after Reload. On November 16, the host confirmed manual 0.6.10 activation in Dev1, working status indicators and managed lyrics. The repeated-click intake fix and playlist updates remain pending a real check. Version 0.6.9 adds grouped controls, explicit Inbox Show/Suno Playlist labels and prominent Inbox Submissions counts. Mixed-source, AP, advanced live integration and Discord/HQ checks remain separate. Label screenshots from isolated fixtures as fixtures; do not present them as real-show acceptance.

## Evidence and decisions still needed

None of these blocks a clearly labeled development preview. Record real evidence when available; do not fabricate screenshots of working software.

| Needed | Purpose | When |
| --- | --- | --- |
| Radio and compact controls | Extend the confirmed 0.8 Radio broadcast to UI, startup and recovery cases | Radio working November 16; broader cases pending |
| 0.8.1 selection, YouTube and reopen fixes | Confirm song selection keeps order, YouTube has no permanent Catnap button strip, and Theatre reopens during publishing | Host hotfix rehearsal |
| Fair repeats, managed playlist order and manual Decline | Verify real completion releases one repeat at the tail, saved order and exact decline readback/recovery | Real provider rehearsal pending |
| YouTube viewport on Play and quiet Loaded staging | Verify the red source badge, window view, restore and held/manual source transitions | 0.8.1 mixed-source rehearsal |
| Readiness across broader setup/recovery cases | Extend the Dev1 status-indicator confirmation to broader per-step/recovery cases; Lite stays independent | Activation/status indicators confirmed November 16; broader cases pending |
| Repeated-click Inbox intake and playlist updates | Verify the intake fix, saved membership/order and appended updates | Host check pending |
| Presentation and Inbox controls, queue-source heading and submission summary | Verify matching control groups, Inbox Show versus Suno Playlist and Pending/held/read-time context | 0.6.10 interface rehearsal |
| Longer manual LP run and interruption recovery | Extend the confirmed two-song sequence through rebind/reconnect and unavailable media | Between-shows rehearsal |
| Pause or changed selection during preparation; timeout | Cancel the pending start and remain held rather than playing late | Cold-player/cancellation rehearsal |
| Managed Suno → YouTube → Suno with explicit playback | Source identity, one audio owner and native-advance guard | Mixed-source rehearsal |
| AP watching/append with optional autoplay | FIFO append and end-of-track recovery | Explicit test AP |
| Warning overlay, timeout/repeat and private notes | Uploader flag and operator/presentation separation | Managed-show rehearsal |
| Copy now playing with the selected source and uploader `@credit` | Valid inbox ID → user mention; otherwise name credit/Unavailable. Verify credit and review/send manually without a private identity map | Test queue; no unintended Discord post |
| Managed/Legacy controller handoff | One writer, drained pending work and inactive defaults | Private advanced rehearsal |
| Current two-panel Theatre at 1920×1080 | Baseline and Store listing screenshot | Safe between-shows rehearsal |
| Three-panel Theatre with several entries | Demonstrate layout/current-song marker | After native/managed queue acceptance |
| Broader managed-lyrics text/transition/recovery cases | Extend the Dev1 managed-lyrics confirmation to quiet Load Next, delayed details, Reload, reopen and source changes | Managed lyrics confirmed November 16; broader cases pending |
| Square/portrait/animated/missing artwork | Containment and fallback behavior | Member test |
| Lounge/BRB/after-show and local media banners | Explicit audio-source and overlay behavior | Rehearsal |
| Controller separate from shared output | Operator/program separation | Private integration rehearsal |
| Store support/contact, privacy and remaining listing assets | Review and publication readiness | Store beta review follow-up |
| Kai's maintained uploader contract | Stable future API/MCP adapter | Before relying on a new API |
| Target listener count, devices and acceptable delay | Audio pilot scale and mobile behavior | Ongoing measured listening tests |

Capture without account menus, private chats, pairing keys, queue identities or unrelated tabs. Use original synthetic fixtures or authorized test music/art. The supplied Kraesk screenshot remains local reference material, not a Catnap product screenshot.

## Decisions already made

Public Theatre, overview/website and inbox guide; private advanced-hosting/simulcast source during the pilot; PolyForm Noncommercial terms with separate commercial permission; approved AIU branding inclusion with separate branding rights; Chrome/Brave first and Firefox separate; host-owned Suno authorization; deterministic queue operations without an LLM; managed external entries without required Suno placeholders; prefer a proven OBS adapter before a new Studio encoder.

Source, release publication, website deployment, browser activation and live acceptance remain separately recorded steps. See [current versions](RELEASES.md) and [the roadmap](ROADMAP.md).
