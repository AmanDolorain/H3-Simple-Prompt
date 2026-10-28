# Publish H3 Simple Prompt 1.0.0

Repository: https://github.com/AmanDolorain/H3-Simple-Prompt
Registry node ID: h3-simple-prompt
Publisher ID: amandolorain (taken from the previous H3 Controller metadata; verify this matches your Registry publisher).

1. Upload pyproject.toml to the repository root and publish.yml to .github/workflows/publish.yml. Keep the existing tests.yml. Commit these files to the default branch.
2. At https://registry.comfy.org create/select the publisher amandolorain and obtain a Registry publishing API key.
3. In this GitHub repository: Settings → Secrets and variables → Actions → New repository secret. Name: REGISTRY_ACCESS_TOKEN. Value: the Registry key. The secret is configured separately for each repository.
4. Actions → Publish to Comfy Registry → Run workflow. Select the default branch containing all the node files. The workflow is manual only; uploading the files does not publish automatically.
5. Confirm the workflow succeeded and check the Registry listing/version. GitHub Releases and Registry publishing are separate operations.

Do not paste API keys into code or chat. If your publisher ID differs, edit PublisherId before publishing. After a version is published, increment the version for later code changes. The metadata is ready locally; live Registry validation/publishing has not been run here.

Official instructions: https://docs.comfy.org/registry/publishing
