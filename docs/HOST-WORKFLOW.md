# Catnap Radio host workflow

This general guide records the existing process. The host's local `AGENTS.md`, current inputs and explicit corrections control an actual event.

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

