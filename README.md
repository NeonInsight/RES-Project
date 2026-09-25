# RES — Relational–Episodic Self

Public website and research documentation for RES, an independent project studying actor-indexed causal mediation and accountable AI delegation.

**Current scientific status:** no model-level CoreRES or StrongRES result is established. The original five-factor capability gate remains failed. The initial neutralization diagnostic did not replicate in the later five-factor comparison. The mechanism assay remains inadequate.

- [Project overview](docs/research.md)
- [Public framework paper](docs/paper.md)
- [Findings and interpretation limits](docs/findings.md)
- [Contamination-resistant delegation](docs/architecture.md)
- [Methods](docs/methods.md)
- [Research resources and evidence](docs/resources.md)
- [Next milestones](docs/roadmap.md)
- [Glossary](docs/glossary.md)
- [Support and contact](docs/support.md)

Contact: [RESelfProject@outlook.com](mailto:RESelfProject@outlook.com). Support: [GoFundMe](https://gofund.me/95781ab95).

## Website

The deployable static website is in `site/`. It requires no model API, database, client-side framework, or runtime secrets. Reading and navigating work without JavaScript. Source text lives in `docs/`, presentation in `assets/site.css`, and shared settings in `site.config.json`.

Build with Node.js 20 or newer:

```sh
node scripts/build.mjs
python3 scripts/check_site.py
```

The Markdown renderer is vendored with its license; no package installation is required. The build emits all pages, printable research documents, report downloads, and a source manifest. No model inference is performed.

To preview locally:

```sh
python3 -m http.server 8080 --directory site
```

Then open `http://localhost:8080` in your own browser.

## Cloudflare deployment

Use the committed `site/` directory as a static Cloudflare Pages site. The deployment guide explains the GitHub integration, custom domain, and optional Workers static-assets route: [DEPLOYMENT.md](DEPLOYMENT.md).

The site has no guessed domain or canonical URL. Set `canonicalOrigin` only after the intended domain is confirmed. The site's GitHub links point to this documentation repository; experiment sources remain pinned to the research repository below.

## Evidence boundary

The original experiments remain in [NeonInsight/evals, res-chat-feasibility](https://github.com/NeonInsight/evals/tree/res-chat-feasibility). Public summaries in this project use immutable research commit `1187ead1fa13a4af76433ca32b8aad30cd3d52ef`. See [evidence/README.md](evidence/README.md).

Archived reports retain historical status text, including planning statements later overtaken by completed runs. The dated findings page and the completed complexity report explain the current interpretation. Do not silently rewrite historical reports.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Independent methodological criticism, fresh fixtures, accessibility fixes, and corrections with source evidence are welcome.

## Rights and attribution

The public website adapts the project’s supplied Muse draft and current research materials. This repository uses the [MIT license](LICENSE) selected by its owner. Archived experiment material retains its upstream MIT license and copyright notice. The vendored Marked renderer has its own MIT license.
