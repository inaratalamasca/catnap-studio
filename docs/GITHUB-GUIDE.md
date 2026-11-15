# GitHub: where to find things

The projects belong to **inaratalamasca**. The [overview](../README.md) is the front door.

## The few parts that matter

| GitHub area | What it means for Catnap |
| --- | --- |
| README / Code | What this project does and its current source. The main branch is the consolidated starting point. |
| Releases | Named versions and downloads. Use a release ZIP for installation; an early-access release still has documented limits. |
| Issues | Bugs, feature requests and unfinished acceptance. An open issue is not a completed feature. |
| Pull requests | Proposed changes with their review and checks. Changes move into main after verification. |
| Branches | Work in progress. An old development branch is not automatically the newest supported download. |

## Public, private and protected

Theatre, this Studio overview and the simple inbox guide are public. Advanced hosting and simulcast source remain private during development. The web listener is public to listeners independently of its source repository's visibility. See the [project table](../README.md#projects) for current availability.

Public source can be read and copied; repository write access is separately controlled. The [noncommercial license](../LICENSING.md) explains permitted reuse and separate commercial permission. Third-party branding is not granted by that software license.

Branch protection prevents destructive history changes; it does not make code private or screen every file for private data. Public project main branches use basic deletion/force-push protection, with ordinary updates allowed. Private-project protection requires an eligible paid plan; no paid upgrade or transfer was made as part of this cleanup. See [GitHub's plan documentation](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).

## Keeping releases tidy

1. Make changes on a focused branch and describe the resulting behavior in its pull request.
2. Run the project's maintained checks and the tracked-file publication guard. Review code, docs, history and assets before changing visibility.
3. Merge related changes in dependency order, then update the README, change log and linked overview.
4. Tag the exact source revision for a downloadable release. Include license/notices and a checksum. Keep experimental scope and remaining acceptance visible.
5. Install between shows. Publishing code never reloads a running extension or restarts a live stream.

## Things that stay private

Never commit identity masters, Suno/Discord mappings, inbox CSVs, event records, private duration catalogs, tokens, pairing files, browser profiles, third-party private source or operational server data. Keep those in local/server private storage. Ignore rules and `scripts/check-repository.sh` help catch accidental additions; review the actual staged files as well.

The inbox walkthrough uses the submission's Discord uploader name for a verified ping. It does not require the maintainer's private correlation sheet. Automatic Discord posting uses an authorized bot/webhook; the browser-assisted web route prepares messages for human review/send.
