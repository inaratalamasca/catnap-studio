# Requested scope and project allocation

Source: Ina's ongoing Catnap Theatre/Catnap Studio requests; updated November 15, 2026. This is a scope ledger, not a full acceptance claim. The 0.6.8 public preview adds managed inbox/playlists and mixed-source playback. After 0.6.4 quiet Load succeeded but Play timed out, the 0.6.5 retry reported “Target matched, audio not found”. With the 0.6.6 active-music/silent-helper correction, the host confirmed the standalone sequence Play song 1 → held ending → Load Next paused → Play song 2. That trial exposed missing managed lyrics; the 0.6.7 host retry still showed missing lyrics, with Reload available. The 0.6.8 plain-text/local-panel correction still needs its real host check. Mixed-source, AP, advanced live integration and Discord/HQ checks remain separate. See [current versions](RELEASES.md) for public versus private availability.

| Request | Owner / planned acceptance |
| --- | --- |
| Standalone works without AI/bot/server | Theatre; load unpacked, play native Suno with backend unreachable |
| Minimal two-panel view | Theatre; small header, large contained art, readable lyrics, bottom transport |
| Optional playlist/art/lyrics layout | Theatre; bounded visible playlist, current highlight, no false complete-list claim |
| More layouts later | Theatre; settings/layout abstraction, avoid free-form layout support initially |
| Approximate time-based lyric scroll | Theatre; pause-aware, manual wheel/touch correction, reset on track changes |
| Font size and optional metadata stripping | Theatre; preserve raw text; toggle re-renders without destructive editing |
| Missing/odd-character lyric recovery | Theatre; matching song identity, safe text rendering, bounded retry, explicit unavailable state |
| Maximum non-cropped art and animated Suno art | Theatre; contain sizing, current-song video only, muted and still fallback |
| Art-only presentation | Theatre; selected mode, transport remains reachable |
| Intuitive local storage | Theatre; explain settings vs temporary media, explicit picker and recovery |
| Waiting/pre-show/after-show with AIU radio | Theatre; future lounge mode, deliberate audio-source switch to prevent double audio |
| User playlist instead of radio | Theatre; planned optional lounge source; preserve native account boundary |
| Next listening-party schedule | Theatre/hosting; use verified source, timezone/DST handling, unavailable state |
| Warning/message/intake banners and typed text | Theatre; optional control-panel-operated GIF/banner overlays where feasible, expiry/clear; advanced avatar library/stage is not a standalone requirement |
| Live updating playlist with current marker and selection | Theatre; do not refresh playing page; virtualized list limits disclosed; test native action readback |
| Managed Suno/YouTube playback | Theatre 0.6.8 preview; YouTube-only entries retained without placeholders and preferred when both links are supplied; respect embed/autoplay restrictions; live transitions still need rehearsal |
| YouTube in a physical Suno placeholder | Legacy hosting only; explicit slot mapping and source handoff remain separate from new managed external entries |
| Separate operator controls | Prepared presentation and Inbox/show windows; private advanced Host Controls 0.4.8 coordinates Managed versus deliberately selected Legacy ownership |
| User background/logo customization | Theatre; bounded styling, validated local assets, simple reset |
| AIU + Created by Catnap Radio on every layout | Theatre; AIU branding inclusion approved; preserve attribution on each layout and separate branding rights |
| Private Chrome distribution, Firefox bonus | Theatre; test first, prepare listing/privacy/screenshots; separate Firefox acceptance |
| Uploader warning overlays and broader support banners | Timed warning flags on load/advance in the 0.6.8 managed preview; optional bot chat warnings and verified regional support templates remain advanced work |
| Playlist media/avatar dock, Jah reactions and Ina emotion puppet | Advanced Hosting; substantial stage sized alongside large art/lyrics and 3–5 playlist entries, long-loop instrument/dance library, emotion variants and avatar/GIF zoom; optional Jah selection; live MMD/RP/VRC-style insertion is Studio research |
| Full host and uploader workflow | Managed queue preview is deterministic without an LLM; full advanced hosting additionally prepares playlist artwork and reviewed dark cue PDFs. Supported uploader API/MCP cooperation remains future work |
| Better Discord + web audio | Simulcast research; measured latency/sync, no duplicate listening path |
| OBS-like studio or OBS setup integration | Studio research; favor proven capture/encoding components first |
| Kraesk review after October 25 | Local evidence report; exact history and provenance, no unsupported authorship claims |
| GitHub organization and local cleanup | Public Theatre/overview/guide; private hosting/simulcast source; scoped releases, preserved operating files and private-data guards |

## Not part of setup acceptance

Chrome Store approval (the 0.5.0 beta is pending review), Firefox compatibility, provider streaming acceptance, long-running live watches and a complete new Studio application all need their own acceptance evidence. Do not label roadmap stubs as released products.
