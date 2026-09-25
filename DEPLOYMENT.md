# Deploy RES on Cloudflare

This repository produces a static website in `site/`. Deployment does not need an AI API key or access to the experiment runner.

## Cloudflare Pages with GitHub

In Cloudflare, open **Workers & Pages → Create application → Pages → Import an existing Git repository** and select **NeonInsight/RES-Project**. This repository includes the generated `site/` directory and all build sources.

| Setting | Value |
| --- | --- |
| Framework preset | None |
| Production branch | main |
| Root directory | Repository root |
| Build command | `node scripts/build.mjs` |
| Build output directory | `site` |
| Environment variables | None required |

The renderer is vendored, so the build does not install dependencies. Alternatively, deploy the committed output using `exit 0` as the build command. Each connected branch push can trigger a Pages deployment; review the configured production branch before publishing changes.

## Custom domain

After the initial Pages deployment succeeds, open its **Custom domains** settings and add the exact domain you own. Follow Cloudflare’s domain verification and DNS instructions for that project. Do not replace mail records or unrelated DNS records. Domain registration and website publication are separate steps.

Then set `canonicalOrigin` in `site.config.json` to the confirmed HTTPS origin, without a trailing slash, rebuild, and commit. This adds canonical URLs and a sitemap for the actual domain. Until it is configured, the site omits guessed canonical URLs and the sitemap.

## Cloudflare Workers static assets

If the purchased hosting project is a Workers project instead of Pages, this same `site/` output can be served as static assets. `wrangler.jsonc` declares the assets directory and a real 404 page. Use Cloudflare’s existing project and domain settings; do not create a second production site by accident.

## Direct upload

For a new Pages project created with Direct Upload, upload the **contents of `site/`**, including `index.html` at the top level. Choose the deployment method deliberately: Cloudflare’s project-type switching limitations are described in its documentation.

## Release checks

- Build and run the local link/content validator.
- Confirm the GoFundMe URL and project email.
- Check the deployment URL before attaching the domain.
- Check home, findings, paper, resources, and the missing-page response.
- Confirm the deployed commit and the latest evidence snapshot shown on the site.

## Official documentation

- [Pages Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Static HTML on Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)
- [Pages custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)
- [Workers static assets](https://developers.cloudflare.com/workers/static-assets/)

Settings were prepared against Cloudflare’s documentation on 25 September 2026. No domain has been invented or silently connected by this package.
