---
description: Modèle de second brain personnel, piloté par un agent IA depuis Obsidian et Copilot App.
created_date: 2026-09-19 20:53:34
---

# Second Brain — modèle prêt à l'emploi

⚠️ [English version](README.en.md)

Un endroit pour capturer ce qui vous passe par la tête, retrouver vos informations et faire avancer
vos projets. **Aucune compétence technique requise** : vous échangez dans la langue indiquée dans
`config.md`, l'agent s'occupe des fichiers.

Deux applications, deux rôles :

- **Obsidian** — lire, naviguer, capturer une idée dans `0_Inbox/`.
- **GitHub Copilot App** — comprendre, organiser, écrire et ranger tout le reste.

Le classement principal suit cinq dossiers IPCRA : `0_Inbox` (capture brute) · `1_Projets` (avec une
fin) · `2_Casquettes` (rôles permanents) · `3_Ressources` (réutilisable) · `4_Archives` (terminé).
La file transverse `5_Rappels/` conserve les rappels durables, classés par thème.

## Démarrer

**➜ [Le tutoriel complet est dans `docs/TUTORIEL.md`](docs/TUTORIEL.md)** — installation, premier
réglage, usage au quotidien et dépannage, avec des prompts prêts à copier-coller.
**[English version: full tutorial](docs/TUTORIEL.en.md)**

Prérequis : un compte GitHub avec accès à Copilot, [Obsidian](https://obsidian.md/download),
GitHub Copilot App et Google Drive pour ordinateur, à installer tous deux depuis **Workspace One** —
le second brain s'installe dans *Mon Drive*, en mode hors connexion, pour être sauvegardé sans
rien changer à vos habitudes. Le tutoriel détaille ce réglage, qui n'est pas optionnel.

## Comment c'est fait

| Fichier | Rôle |
|---|---|
| `config.md` | Vos préférences : identité, casquettes, ton, plafonds, périmètre sensible. |
| `.github/copilot-instructions.md` | Les règles de travail de l'agent ; plafond défini dans `config.md` §5. |
| `_systeme/` | Le fonctionnement du système : journal, routines d'entretien, améliorations. |
| `5_Rappels/` | Les rappels durables et transverses, classés par thème. |
| `docs/` | Tutoriel et exemples remplis — pour vous, volontairement hors du contexte de l'agent. |
| `.agents/skills/` | Compétences optionnelles de l'agent. |
