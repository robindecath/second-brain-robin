---
description: Configuration personnelle du second brain — à remplir après clonage.
created_date: 2026-09-19 20:53:34
---

# Configuration

> Ce fichier isole tout ce qui est propre à toi, pour que le reste du dépôt reste générique.
> Lu par l'agent en début de session, avant toute autre chose.

## 1. Identité & usage

- **Prénom** : `Robin` — comment l'agent te désigne.
- **Rôle** : `dev`.
- **Contexte** : `professionnel` — influence le ton et les exemples que l'agent choisit.

## 2. Casquettes principales

Rôles permanents (sans date de fin), 2 à 4 maximum. Chacun devient un dossier dans
`2_Casquettes/`.

- `Tech lead Datacost`
- `Suivi des externes de l'équipe`

## 3. Ton et langue

- **Langue** : `français`.
- **Ton** : `concis, pédagogique et informel`.

## 4. Conventions

Ces deux choix ne portent que sur les **noms de notes libres** (notes atomiques, ressources). Trois
règles sont structurelles et ne se configurent pas : un dossier et sa note de contexte portent le
même nom (`Projet_X/Projet_X.md`), un hub porte le nom de son dossier, une capture d'Inbox est
datée (`AAAA-MM-JJ-nom-court.md`).

- **Casse des noms de fichiers** : `kebab-case`.
- **Format de date** : `AAAA-MM-JJ`.

## 5. Plafonds

**Source de vérité unique** : le socle lit ces valeurs ici et ne les répète pas. Le socle dit *quand*
un plafond s'applique ; cette table dit *combien*. Modifiables, à condition de rester des nombres.

| Fichier | Plafond |
|---|---|
| `.github/copilot-instructions.md` | < 150 lignes |
| `config.md` (ce fichier), `README.md` | < 80 lignes |
| Hub, note de contexte, procédure | < 80 lignes |
| Note atomique, capture d'`0_Inbox/` | < 150 lignes |
| Journaux, tables, files d'attente | aucun plafond — leur croissance est bornée autrement |

## 6. Périmètre sensible

Ce qui ne doit **jamais** être écrit dans le vault, quelle que soit la source — y compris si tu le
dictes toi-même à l'agent :

- Aucune catégorie spécifique déclarée.

## 7. Outils externes branchés

| Outil | Ce qu'il peut lire | Action directe, sans demander | Accord obligatoire |
|---|---|---|---|
| GitHub | Tout DKTUnited ; mes dépôts concernés sont liés à Datacost. | Lecture seulement. | Toute écriture nécessite ton accord. |
| Jira | Tout. | Lecture seulement. | Écriture dans le projet BST2 uniquement, après ton accord ; toute autre écriture n'est pas autorisée. |
| Confluence | Tout. | Lecture seulement. | Aucune écriture autorisée. |
| Datadog | Les informations du projet Datacost. | Lecture seulement. | Aucune autre action autorisée. |
| SMAX | Les tickets de support de l’application Datacost. | Lecture seulement. | Aucune autre action autorisée. |
