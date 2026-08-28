# Development

## First-time setup

```bash
cd projects/template
./scripts/bootstrap.sh
source .venv/bin/activate
```

This creates `.venv`, installs the package plus test tools, and copies `.env.example` to `.env`.

## Everyday commands

```bash
make test      # pytest
make lint      # ruff
make ci        # lint + tests (same as GitHub Actions)
make run       # python -m app
```

## Environment

Edit `.env`. Never commit it. The keys are defined in `.env.example`:

- `APP_ENV` — `development`, `test`, or `production`
- `APP_DEBUG` — `true` or `false`
- `LOG_LEVEL` — `debug`, `info`, `warning`, or `error`
- `SECRET_KEY` — replace `change-me` before any real deployment

## CI on GitHub

Pushes to `main` and pull requests run `.github/workflows/ci.yml`.

To confirm it worked:

1. Open [Actions](https://github.com/NicolasFromBelgium/template/actions)
2. Open the **CI** workflow run
3. Open **Run test suite**
4. Find `test_ci_pipeline_runs_on_github_actions PASSED`

## CD

Push a version tag to build artifacts and create a GitHub Release:

```bash
git tag v0.1.0
git push origin v0.1.0
```
