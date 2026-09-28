---
description: English introduction and quick-start guide for the Second Brain template.
created_date: 2026-09-24
---

# Second Brain — ready-to-use template

[Version française](README.md)

A place to capture thoughts, find information, and move projects forward. **No technical skills
required**: work with the agent in the language set in `config.md`; it takes care of the files.

Two apps, two roles:

- **Obsidian** — read, navigate, and capture ideas in `0_Inbox/`.
- **GitHub Copilot App** — understand, organize, write, and file everything else.

The main filing system uses five IPCRA folders: `0_Inbox` (raw captures) · `1_Projets` (projects
with an end date) · `2_Casquettes` (ongoing roles) · `3_Ressources` (reusable knowledge) ·
`4_Archives` (completed or inactive). The cross-cutting `5_Rappels/` queue holds durable reminders
organized by theme.

## Getting started

Follow the [full installation and usage tutorial in English](docs/TUTORIEL.en.md). The
[French version](docs/TUTORIEL.md) is also available.

To use the template in English, set the language in **§3 of `config.md`** to `English`. You can also
ask Copilot:

> Use English as my working language. Set the language in `config.md` to English. Reply to me and
> write new notes in English, but keep folder names, filenames, frontmatter keys, existing content,
> and wikilinks unchanged unless I ask.

Requirements: a GitHub account with Copilot access, Obsidian, GitHub Copilot App, and Google Drive
for desktop. Install the apps through **Workspace One**. The vault must be stored in *My Drive* and
available offline so it is backed up automatically; the tutorial's setup instructions are required.

## How it works

| File or folder | Purpose |
|---|---|
| `config.md` | Your preferences: identity, roles, tone, language, limits, and sensitive topics. |
| `.github/copilot-instructions.md` | The agent's working rules. |
| `_systeme/` | How the system works: journal, maintenance routines, and improvements. |
| `5_Rappels/` | Durable cross-cutting reminders, organized by theme. |
| `docs/` | Human-facing tutorial and examples; kept out of the agent's context. |
| `.agents/skills/` | Optional agent skills. |
