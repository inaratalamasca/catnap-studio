# Catnap Studio

Project website: [catnapradio.com](https://catnapradio.com/). The landing page source lives in [website/](website/), with owner-supplied Catnap artwork and links to AIU Radio, the uploader and merch shop; repositories remain private during development.

**Project hub and future studio design.** This repository organizes Catnap Radio's tools. It is not an OBS replacement you can download today.

Catnap helps a host turn a Suno playlist into a readable, branded listening party, then adds only the integrations that host needs. Standalone Theatre is the first priority.

| Project | Purpose | Current boundary |
| --- | --- | --- |
| [Catnap Theatre](https://github.com/inaratalamasca/catnap-theatre) | Simple standalone Suno presentation extension | No AI, bot, server or copied Suno credentials required |
| [Catnap Radio Hosting](https://github.com/inaratalamasca/catnap-radio-hosting) | Integrated Theatre, host control, durable requests, show preparation | Existing host-authorized sessions and optional Suno MCP; private configuration stays with the host |
| [Catnap Simulcast](https://github.com/inaratalamasca/catnap-simulcast) | Explore better audio alongside Discord visuals | Research; no operational listener service promised |
| Catnap Studio (this repo) | Shared roadmap and potential all-in-one studio | Design only; evaluate OBS integration before building an encoder |

## Why these are repositories, not forks

A repository is a project's source and history. A fork starts from somebody else's repository. Our tools already have their own source and goals, so we create our own repositories. We do not fork or redistribute Kraesk's private Nightwire project. Its ideas can inform requirements; reuse of its code/assets needs an appropriate license or permission.

The three product focuses are standalone Theatre, integrated Theatre and radio hosting. The latter two live together because they share session state and releases. We avoid two independently maintained copies of the new standalone core. The existing integrated Theatre is preserved as a legacy compatibility extension until a tested adapter can use the standalone core.

The hosting repository contains separate installable extensions for integrated Theatre and host control. A separate Jah browser controller is an adjacent existing extension, documented in the inventory; it is not a dependency of standalone Theatre. The Discord posting helper is currently part of host control, not falsely counted as a third standalone install.

## Start here

- [Architecture and boundaries](docs/ARCHITECTURE.md)
- [Roadmap and acceptance gates](docs/ROADMAP.md)
- [Complete requested scope](docs/REQUEST-SCOPE.md)
- [Hosting and cue workflow](docs/HOST-WORKFLOW.md)
- [Screenshots and host decisions](docs/DELIVERABLES.md)
- [GitHub guide](docs/GITHUB-GUIDE.md)
- [Repository maintenance](CONTRIBUTING.md)
- [Private material and reporting](SECURITY.md)

## Status language

**Imported** means existing source is now contained here. **Prepared** means changes exist in source and have the stated checks. **Live verified** requires a dated host/browser/server observation. **Planned** means an issue or specification, not an implemented feature. Passing a local test is not a live Suno or broadcast test.

All repositories begin private while source, artwork rights and host data boundaries are reviewed. Store listing drafts are preparation only. No Chrome Web Store upload, public release, Twitch/YouTube broadcast or live bot deployment is implied by this setup.
