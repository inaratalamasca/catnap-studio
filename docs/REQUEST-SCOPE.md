# Requested scope and project allocation

Source: Ina's Catnap Theatre/Catnap Studio request, November 8, 2026. This is a scope ledger, not a completion claim. See each implementation repository for tested status.

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
| Warning/message/intake banners and typed text | Theatre; text and explicitly selected media, expiry and clear controls |
| Live updating playlist with current marker and selection | Theatre; do not refresh playing page; virtualized list limits disclosed; test native action readback |
| YouTube maximum-area playback | Theatre later; pasted URL first, no bypass of embed restrictions |
| YouTube in placeholder song | Hosting later; explicit slot-to-video map, stop native audio/advance deliberately and restore after |
| Separate operator controls | Hosting current; standalone optional future extension control page |
| User background/logo customization | Theatre; bounded styling, validated local assets, simple reset |
| AIU + Created by Catnap Radio on every layout | Theatre; keep attribution; verified logo asset and usage permission needed before release |
| Private Chrome distribution, Firefox bonus | Theatre; test first, prepare listing/privacy/screenshots; separate Firefox acceptance |
| Full host and uploader workflow | Hosting; only host-authorized inbox and existing browser/MCP credentials; Kai cooperation for supported API |
| Better Discord + web audio | Simulcast research; measured latency/sync, no duplicate listening path |
| OBS-like studio or OBS setup integration | Studio research; favor proven capture/encoding components first |
| Kraesk review after October 25 | Local evidence report; exact history and provenance, no unsupported authorship claims |
| GitHub organization and local cleanup | Four private repos, scoped issues/milestones, preserved working files, migration record |

## Not part of setup acceptance

Chrome Store approval, Firefox compatibility, provider streaming acceptance, permanent public hosting, live automation watches and a complete new studio application all need their own acceptance evidence. Do not label roadmap stubs as released products.
