---
description: Journal système — décisions et évolutions du fonctionnement du second brain, datées.
created_date: 2026-09-18 15:49:43
---

# Journal système

Consigne toute décision, arbitrage ou évolution concernant le fonctionnement du second brain :
organisation, règles, workflows, conventions, outils, intégrations et gouvernance. Les frictions
d'usage y sont conservées comme signaux d'amélioration, mais elles ne sont pas le seul contenu du
journal. Jamais de contenu métier — pour ça, voir `3_Ressources/Decisions_Log/`.

## Règles

- **Aucun plafond de lignes.** Ce fichier croît par ajout ; sa taille est bornée par la remise à
  zéro mensuelle, jamais par un nombre de lignes. Ne le signale pas en revue hebdo.
- Une entrée par décision ou sujet, ajoutée en fin de fichier, jamais de réécriture rétroactive.
- Une entrée récente peut en amender une ancienne en la référençant explicitement.
- Écriture directe, sans validation préalable : c'est un constat, pas une inférence.
- Au changement de mois, archivage du contenu dans `_systeme/journal/journal-AAAA-MM.md`, ajout de
  la ligne correspondante au registry de `_systeme/_systeme.md`, et remise à zéro de ce fichier.

## Format d'une entrée

`### AAAA-MM-JJ — <type> — <sujet>`, où `<type>` vaut :

- **`décision`** — un arbitrage sur le fonctionnement : la décision, son motif, son effet.
- **`friction`** — un accroc d'usage, écrit **même sans décision à la clé** : ce qui a coincé, dans
  quel contexte. C'est la matière première du comptage des répétitions — une friction non écrite ne
  sera jamais comptée, et la répétition passera inaperçue.
- **`revue`** — trace d'une revue hebdo ou d'une rétro : ce qui a été traité, ce qui reste. Elle
  sert de borne à la revue suivante, qui ne remonte pas au-delà.
- **`incident`** — perte, corruption, synchronisation ratée : ce qui s'est passé, ce qui l'a réparé.

Le type est ce qui rend le journal filtrable : la rétro mensuelle lit les `friction` pour repérer
les répétitions, et la revue hebdo cherche la dernière `revue` pour savoir où s'arrêter.

## Entrées

### 2026-09-29 — friction — Clarification des droits d’écriture Jira

La portée des droits d’écriture Jira/Confluence a nécessité une question de clarification après
une réponse initiale couvrant lecture et écriture. Le périmètre retenu est Jira BST2 avec accord
explicite et Confluence en lecture seule.

### 2026-09-29 — décision — Personnalisation de config.md

Renseignement de `config.md` avec les préférences d'identité, de rôle, de casquettes, de langue,
de ton, de nommage, de plafonds, de périmètre sensible et les droits déclarés pour les outils
externes.

### 2026-09-29 — friction — Clarification de SMAX

La création de la casquette Tech lead Datacost a nécessité de demander ce que signifiait SMAX,
terme absent du glossaire. Robin a précisé qu’il s’agit de l’outil où arrivent les tickets de
support de l’application.

### 2026-09-29 — décision — Création de la casquette Tech lead Datacost

Création de la casquette permanente avec son périmètre de gestion technique de l’application :
suivi de la dette technique, mise en place technique, vérification Datadog et suivi ponctuel des
tickets de support SMAX. Le registry des casquettes, le routage, le glossaire et la configuration
des outils externes sont mis à jour en conséquence.

### 2026-09-29 — décision — Création de la casquette Suivi des externes

Création de la casquette permanente « Suivi des externes de l’équipe », déclarée dans `config.md`.
Le registry des casquettes et le routage sont mis à jour. Le périmètre opérationnel détaillé reste
à préciser.

### 2026-09-29 — friction — Casquette Suivi des externes déjà existante

J’ai interprété à tort la casquette « Suivi des externes de l’équipe », déjà déclarée dans
`config.md`, comme une casquette à créer. Robin a signalé qu’elle existait déjà ; j’ai retiré la
fiche créée en doublon ainsi que ses entrées de registry et de routage. L’état local consulté ne
contenait pas d’autre fiche correspondante.

### 2026-09-29 — friction — Routage inégal des casquettes

J’ai ajouté le renvoi vers Tech lead Datacost dans `.github/copilot-instructions.md` sans vérifier
si le même critère de fréquence était appliqué aux autres casquettes. Robin a relevé cette
incohérence ; le routage devrait suivre un critère explicite et être vérifié de façon cohérente.
