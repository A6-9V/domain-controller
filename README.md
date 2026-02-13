# Domain Controller Hub

This repository serves as the central orchestration and management hub for the A6-9V ecosystem. It centralizes multiple projects, automation scripts, and infrastructure configurations.

## 📁 Repository Structure

-   `/apps`: User-facing applications and portals.
    -   `users-portal`: Next.js portal for user management.
    -   `vps-bridge`: Bridge for MQL5 VPS integration.
-   `/automation`: Backend services and automation bots.
    -   `mql5-automation`: MQL5 Google/OneDrive integration and Telegram bot.
-   `/infrastructure`: Shared deployment, CI/CD, and Docker configurations.
-   `/docs`: Centralized knowledge base and ecosystem documentation.
-   `/scripts`: Utility scripts for managing the ecosystem.

## 🌿 Branching Model

We follow a consistent branching model across all repositories in this ecosystem:

1.  **`main`**: Production-ready code. Only stable releases are merged here.
2.  **`develop`**: Integration branch. All features and bug fixes are merged here first for testing.
3.  **Feature Branches**: (`feature/...`, `bugfix/...`) Created from and merged back into `develop`.

## 🛠 Working with Submodules

This hub uses Git submodules to link projects. To initialize all submodules, run:
\`bash
git submodule update --init --recursive
\`

To sync all submodules to their latest `develop` branch:
\`bash
git submodule foreach 'git checkout develop && git fetch origin && git merge origin/develop'
\`

## 📓 Knowledge Base
- **NotebookLM**: [Access here](https://notebooklm.google.com/notebook/e8f4c29d-9aec-4d5f-8f51-2ca168687616)
- **Note**: This notebook contains high-level strategy and context. Agents must consult it before significant architectural changes.
