# Project template

This repository is a **template** for new projects.

Use it as a starting point: environment files, gitignore, tests, and GitHub Actions CI/CD are already wired so humans and coding agents work from the same layout.

[![CI](https://github.com/NicolasFromBelgium/template/actions/workflows/ci.yml/badge.svg)](https://github.com/NicolasFromBelgium/template/actions/workflows/ci.yml)

## What you get

- `src/app/` — application code
- `tests/` — pytest suite, including a CI smoke test you can see in GitHub Actions
- `.env.example` — documented environment variables (copy to `.env`)
- `.gitignore` — secrets, virtualenv, caches, build output
- `.github/workflows/ci.yml` — lint and test on every push and pull request
- `.github/workflows/cd.yml` — build and GitHub Release on version tags (`v*`)

Folder names are listed in [docs/directory-map.md](docs/directory-map.md).

## Quick start

```bash
git clone git@github.com:NicolasFromBelgium/template.git
cd template
./scripts/bootstrap.sh
source .venv/bin/activate
make test
```

## Check GitHub Actions

After the first push, open:

**https://github.com/NicolasFromBelgium/template/actions**

1. Click the **CI** workflow
2. Open the latest run → **Run test suite**
3. Confirm `test_ci_pipeline_runs_on_github_actions PASSED`

That test is in `tests/test_ci_pipeline.py`. It always runs in CI. On GitHub it also checks `GITHUB_ACTIONS`, `CI`, and the repository name.

You can start a run by hand with **Actions → CI → Run workflow**.

## Environment

```bash
cp .env.example .env
```

| Variable | Purpose |
| --- | --- |
| `APP_ENV` | `development`, `test`, or `production` |
| `APP_DEBUG` | `true` / `false` |
| `LOG_LEVEL` | `debug`, `info`, `warning`, `error` |
| `SECRET_KEY` | required for any real deployment |

`.env` is gitignored. Never commit secrets.

## CI / CD

| Workflow | Trigger | What it does |
| --- | --- | --- |
| **CI** | push to `main`, pull requests, manual | ruff + pytest + coverage, uploads a JUnit report |
| **CD** | tag `v*`, manual | tests, builds the package, creates a GitHub Release |

Run the same CI checks locally:

```bash
make ci
```

Create a release:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Using this as a template

1. Create a new repo (GitHub → Use this template, or clone and change the remote).
2. Rename the Python package `src/app` if you want a different name.
3. Update `README.md`, `pyproject.toml`, and `LICENSE`.
4. Fill in `.env` from `.env.example`.

## License

MIT. See [LICENSE](LICENSE).
