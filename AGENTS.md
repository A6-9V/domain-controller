# Agent Guidelines for Domain Controller

As an AI agent working on this repository, you must adhere to the following rules to maintain the integrity of the ecosystem.

## 🚀 Workflow & Branching

1.  **Always work on `develop`**: Never commit directly to `main` unless performing a production release.
2.  **Verify Submodule State**: Before making changes, ensure submodules are at the correct commit and branch.
3.  **Cross-Project Impact**: If a change in the hub affects a submodule (or vice versa), document the dependency clearly.

## 🧪 Testing & Verification

1.  **Run Submodule Tests**: If you modify code within a submodule, you MUST run its local test suite.
2.  **Deployment Awareness**: Check Render status for affected services after pushes.
3.  **NotebookLM Reflection**: Record significant architectural decisions or changes in the [NotebookLM](https://notebooklm.google.com/notebook/e8f4c29d-9aec-4d5f-8f51-2ca168687616).

## 📂 Structure Maintenance

- Do not add top-level files unless they are global configurations.
- Categorize new projects into `apps/` or `automation/`.
- Keep `infrastructure/` updated with the latest deployment secrets templates and Docker configs.

---
*Note: This repository is the Domain Controller. It is the source of truth for the entire environment.*
