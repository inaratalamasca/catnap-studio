# Roadmap

Updated November 15, 2026. Standalone Theatre 0.5.0 is an early-access release; integrated Theatre 0.5.0/Host Controls 0.4.6.2 have been loaded and connected by the maintainer. The listener 0.1.6 and metadata 0.2.1 pilot are operational during broadcasts. The stages below retain broader acceptance tasks; they do not erase completed implementation or promise dates.

## 0 — Contain and document (this setup)

Create repositories with deliberate public/private boundaries, import selected first-party source, preserve operational locations, inventory live versions, record research and prepare installation/support material. Separate local event/private reference data from Git history.

## 1 — Standalone Theatre alpha

Prepare the smallest independent extension from Catnap's existing Theatre: two-panel view, optional compact playlist, art containment/current-song animation, raw/clean lyric toggle, bounded reload, manual scroll correction, font settings and text/media banners. Local checks are followed by a real Suno smoke test before use on air.

Acceptance includes 10 consecutive track changes; tagged and untagged lyrics; an unusual Unicode title; no-lyrics track; long lyrics; pause/seek/reload; square and portrait artwork; available and failed animation; narrow and 1080p layouts; no backend connection; no music interruption caused by metadata refresh. Test native playlist selection and append/resync without replacing an already playing list.

## 2 — Member pilot and packaging

Test Chrome with a clean member profile and no Catnap server configuration. AIU branding inclusion was approved by the maintainer on November 15, 2026. Icons and original fixture screenshots are prepared. Complete accessibility checks, remaining live acceptance and store-specific privacy declarations. Define preference backup/reset and local-file handling. Pilot Firefox separately. Package a versioned zip; record browser version, source commit and manual results. Only then submit to a private trusted-tester Store channel.

## 3 — Lounge and external video

Add waiting/pre-show/BRB/after-show modes and explicit switching among Suno, AIU Radio and optional user playlists. Integrate the existing preshow source without hardcoding a private host's schedule for everybody. Add YouTube paste/play first; placeholder mapping second. Confirm one active audio source, stopped playlist advance during a video, predictable restoration and a manual-tab fallback.

## 4 — Integrated hosting

Stabilize a versioned session adapter and reuse standalone display code. Keep the legacy installed integration until the replacement passes a full show rehearsal. Supported Uplink API integration needs Kai's cooperation; preserve pending-only LP/AP intake, oldest-first running order, manual release, verified membership and crash recovery. AI assistance remains optional for deterministic queue operations.

## 5 — Simulcast and Studio experiments

The local WebRTC Live / buffered Radio pilot exists; continue measuring delay, devices, scale and recovery. Prototype an operator/program split that works with existing Theatre and OBS. Keep latency and rights tests separate from encoding success. Record costs and support burden before committing to a hosted multi-user service.
