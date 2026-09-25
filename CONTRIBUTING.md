# Contributing to RES

For methodological review or collaboration, contact [RESelfProject@outlook.com](mailto:RESelfProject@outlook.com), or open a source-supported issue or pull request in this repository.

Useful contributions include independently authored fixtures, stronger rival explanations, checks of paired analysis, raw-response audits, authority-boundary failure cases, and accessible public explanations.

## Evidence changes

1. Identify the source report, model, revision, fixture family, metric, and scope.
2. Distinguish planned, diagnostic, post hoc, confirmatory, replicated, and not-replicated claims.
3. Keep the original failed gate and historical records intact.
4. Preserve paired experimental units and document missing or invalid measurements.
5. Update the dated findings and source manifest when adding new evidence.

Do not include API keys, credentials, private correspondence, participant identifiers, or raw personal data. Use synthetic examples for proposed fixtures unless publication permission is explicit.

## Website changes

Edit Markdown in `docs/`, shared settings in `site.config.json`, or styling in `assets/site.css`. Run `node scripts/build.mjs` and `python3 scripts/check_site.py`, then commit both sources and generated `site/` files. Check narrow screens, keyboard use, and text enlargement when changing layout.

The public website must remain readable without JavaScript. Browser data collection or new external services should be proposed explicitly before adding them.
