# Catnap Radio host workflow

This general guide records the existing process. The host's local `AGENTS.md`, current inputs and explicit corrections control an actual event.

## Choose the edition

Theatre Lite 0.5.0 remains the active, unchanged presentation-only choice for ordinary Suno and non-AIU hosts. It needs no Inbox or playlist helper; the AIU setup and production steps below do not become Lite requirements.

Radio-only 0.7.0 can publish a Suno or AIU party tab alongside Lite without an Inbox or desktop helper. The two AIU playlist creators still use the host’s own Suno connection and desktop companion. Use one publisher for a show.

The AIU Inbox edition adds optional intake, playlist and managed-show features. Version 0.6.10 shows labeled Suno/Inbox readiness dots and a result for each setup step. In ordinary use of this edition the dots remain grey/inactive. On November 16, the host confirmed manual 0.6.10 activation in Dev1, working status indicators and managed lyrics. Intake retries, playlist updates, AP, YouTube and advanced live acceptance remain separate.

## Simpler managed queue preview

The public AIU Theatre + Inbox and Inbox-only 0.7.0 previews add a deterministic
workflow without an LLM or the advanced bot: Pending FIFO intake, source flags,
uploader notes, own-account playlist creation and a managed mixed-source show.
YouTube-only entries stay in managed order without a Suno placeholder; YouTube
is preferred when both links are supplied. LP Load and Play are separate; AP
autoplay is optional. Notes stay in host controls. Copy now playing uses the selected source and
submission uploader’s `@credit` for manual review/send, without a private identity
map. This preview still needs real-show rehearsal. In 0.6.4, quiet Load worked
but Play timed out waiting for the selected native song; the 0.6.5 retry reported
“Target matched, audio not found”. Version 0.6.6 distinguished active music from
Suno’s silent helper. The host confirmed the standalone 0.6.6 sequence: Play
song 1, hold at its ending, Load Next paused, then Play song 2. That trial exposed
missing managed lyrics. The 0.6.7 host retry still showed missing lyrics after Reload. The November 16 Dev1 0.6.10 check confirmed activation, status indicators
and managed lyrics. The repeated-click intake fix and playlist updates remain
pending a real check. Version 0.6.9 groups matching Presentation/Inbox controls and labels
the displayed list Inbox Show or Suno Playlist; Inbox Submissions shows readable
Pending/held counts and the read time. Mixed-source, AP, advanced live integration and
Discord/HQ checks remain separate. Preparation remains bounded and muted;
Pause, changed selection and timeout cancel it. Load remains separate from Play.

The full LP/AP preparation below remains a larger deliverable contract,
including artwork and dark cue PDF/review. Its historical physical-Suno
placeholder mapping belongs to the deliberately selected legacy workflow;
it is not a requirement to manufacture placeholders for new managed shows.
Keep one intake/playback writer active.

The 0.7.0 preview uses one gear for Presentation controls, with Radio and Inbox buttons in that operator window. Source-only On Air and the green AIU logo reflect actual publishing; the top status also names Inbox versus Suno playlist mode. Managed YouTube Play fills the Theatre viewport with a red badge, while quiet staging is labeled Loaded. The real 0.7.0 host/mixed-source rehearsal remains pending.

## Prepare an LP

1. Confirm host, event date/time/timezone and the intended LP Pending inbox. CSV exports contain historical rows and may omit status; reconcile against current Pending by song ID. Build oldest-first from the uploader's newest-first display. Do not reverse an already supplied Suno playlist.
2. Match identities against the local four-column master: Suno name, Discord General (uploader), Discord AIU Name, Twitch Name. Keep uncertain matches blank. Current event facts and host corrections beat historical aliases; no guessed Twitch names.
3. Use the host's authorized Suno MCP connection for supported playlist creation/list/add/remove operations; save the returned ID and verify full saved order. Native Suno handles unsupported cover uploads and other UI-only operations. Do not use the uploader's legacy Create Suno Playlist button.
4. Keep square playlist cover and wide announcement separate. Use the actual confirmed lineup and date. Do not replace the current master with an event snapshot.
5. Produce the established dark cue PDF: cover, concise clickable index and one cue page per track in saved playlist order. Include Host Introduction, After-Play Comment, Quick Read, Something Nice, prominent uploader note when supplied, current Suno identity, distinct radio opt-in/disclaimer metadata and clickable sources.
6. Keep Discord, Twitch and AIU Radio checks separate. Missing lyrics means NOT CHECKED, not clear. Host not-for-radio choices persist. Lyric/style analysis is not an audio/video/rights review. Render and visually verify the complete PDF before delivery.
7. Configure/post Discord only as part of an authorized production flow, check for an existing post and do not duplicate it. A cue-only request does not request a new announcement.

## Run an AP

APs are spontaneous. Create/adopt the right playlist and AP artwork; no fixed cast list or cue PDF by default. Pending is the active queue. New additions require an explicitly requested active watch and read-back verification. Keep entries Pending during the party. Release slot remains host-manual; Cleanup has broader effects and is not an AP-only shortcut.

## On-air system

Suno plays music. Theatre presents. The host controller operates native UI and reports verified facts. Armin persists session/queue state. The scoped browser watcher is a distinct compatibility path from the official Discord bot. Keep voice/screen sharing in the host's streaming Discord window, isolated from any text-helper tab.

Operator actions should be paced, idempotent and scoped to one session/channel. On ambiguous delivery, reconcile before resend. A saved request is not yet playlist membership; a playlist entry is not proof of advancing playback. Do not restore an old queue backup over current requests during a code rollback.

## Files and continuity

`Catnap/YYYY/YYYY-MM-DD/` and `Guest-Shows/Host-Name/YYYY-MM-DD/` hold Event.txt, Input, Working and Final. Preserve originals, cache metadata once per set, retain prior finals in Working/Revisions and keep a dated verification note. Private data stays on the host's computer/server.

The detailed local handoff, approved templates, current rules and November 1 MCP tests remain under the workspace Reference area. They are references rather than blanket permission to operate a new show.

## Current AIU intake and assisted-development direction

Host update, November 8, 2026: official and semi-official AIU after parties use uploader/inbox submissions. Chat-drop intake remains an explicitly selected emergency or non-AIU option. Announcements/co-host conversation are independent of song-request intake. Existing chat-drop presets and source modes do not establish permission to use them at an AIU event.

Prefer supported, authenticated MCP routes for AI-assisted service operations, including Suno playlist operations; verify capabilities and read back writes. Browser actions remain for missing capabilities or documented fallback. Standalone Theatre remains AI-independent. A supported uploader API/MCP contract is a planned collaboration with its maintainer, not an available interface assumed by the code.

Bot helper/co-host testing depends on verified community permissions. Keep credentials in authorized service connections/browser sessions; dedicated test profiles are preferred when ready. Direct password-manager access and login readiness must be verified separately.


## Ina full hosting package — deliverable contract

The advanced AIU hosting package for Ina produces the following. These are hosting requirements, not requirements for standalone Theatre.

- LP: create the ordered playlist, playlist artwork using the current confirmed artist lineup, and the established dark-mode cue PDF with show artwork/cover, a summary/index page and one cue page per track. Keep square playlist cover and wide announcement outputs distinct under the existing workflow.
- AP: create the ordered playlist and AP artwork without a fixed artist cast list. No cue PDF is required by default unless specifically requested.
- Both LP and AP inbox playlists use FIFO by submission date/time: oldest first, bottom-up in the newest-first inbox, retaining observed bottom-up order for equal timestamps. New arrivals append. A supplied existing playlist is not automatically reversed; any explicitly selected advanced queue mode/host override must be recorded separately from original FIFO intake order.
- In the legacy physical-Suno hosting workflow, YouTube or future external-media submissions without a Suno song require a legitimate placeholder in the Suno playlist at the submission's FIFO position. New managed shows retain external entries directly without placeholders. Keep a unique internal submission/slot identity and explicit external URL/provider mapping. Do not silently skip such entries, manufacture paid placeholder audio or assume one repeated Suno ID supports multiple independent slots. If no usable placeholder exists, report the slot blocked rather than claim the playlist complete.
- When both YouTube and Suno links are supplied, retain both: use Suno for playlist membership/identity and internally mark YouTube as the preferred playback source. This supersedes the older blanket “prefer Suno” rule. Do not autoplay the Suno audio over the preferred external video; implementation must pause native audio/advance, track slot completion and restore playback deliberately. An unavailable external source needs a visible host decision, not a silent source substitution.
- Capture the YouTube alternative from the inbox when CSV omits it. Keep external-media identity, artwork/audio review and clearance distinct from the Suno track's lyric review.

Legacy placeholder lifecycle and the broader full-hosting integration remain separately scoped work. The standalone 0.7.0 preview now owns optional managed inbox/playlist and mixed-source playback; artwork generation and the full cue-PDF/review package remain separate. Preview implementation and fixture checks are not full live acceptance.

