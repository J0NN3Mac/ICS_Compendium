# Importing the bootstrap package

**Status:** imported onto review branch `bootstrap/compendium-foundation` on 2026-09-27 after inspecting the live repository (default branch `main`, initial README only). The original preparation note below is retained as import history.

The repository lookup for `J0NN3Mac/ICS_Compendium` returned `404 Not Found`. The connected account listed no accessible repositories under that owner. These observations do not distinguish a private/inaccessible repository from a missing or mistyped repository. Available GitHub actions in this session were read-only.

Use a write-capable GitHub workflow with access to the exact destination. Inspect its files, license, default branch and existing contributions before importing. Preserve existing content. Do not replace an unseen README or license blindly.

## Import sequence

1. Clone or open the accessible destination and inspect its working tree. Start a review branch, such as `bootstrap/compendium-foundation`, from its actual default branch.
2. Merge the prepared files selectively. Reconcile any README, policy, identifier or licensing conflicts. No project-wide license was selected for the owner in this scaffold.
3. Run the local checks from the repository root:

   ```sh
   python3 scripts/generate.py
   python3 scripts/validate.py
   python3 -m unittest discover -s tests -v
   python3 scripts/generate.py --check
   ```

4. Inspect the diff and staged file list. Include catalog metadata, authored documentation, scripts, templates and the two research snapshots—not third-party dataset binaries.
5. Commit the reviewed change set and open a pull request. Do not force-push or merge automatically. After successful publication, update the bootstrap status banner and record the actual commit and pull-request references in a new change note; retain the original import history.

## Suggested commit title

`Initialize ICS compendium catalog, evidence policy, and research baseline`

## Suggested pull-request scope

Import 12 stable resource records, 30 primary references, ten user-nominated seed sources, the original matrix files, reproducible Markdown/CSV views, contribution guidance, local validation and proposed exercise templates. Explicitly state that runtime validation, packet-level auditing, permissions and production-quality event datasets are not completed by this import.
