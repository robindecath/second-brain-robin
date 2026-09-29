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

### 2026-09-29 — décision — Déclaration des outils Google

Ajout de Gmail, Google Chat et Google Docs à `config.md`. Leur accès est en lecture seule lorsqu'un
connecteur est disponible ; toute écriture nécessite un accord explicite.

### 2026-09-29 — friction — Accès aux outils Google absent

La vérification des emails a été bloquée car aucun connecteur Google ni outil de messagerie n'est
disponible dans cette session ; `config.md` ne mentionne pas encore les outils Google.

### 2026-09-29 — friction — Clarification des droits d’écriture Jira

La portée des droits d’écriture Jira/Confluence a nécessité une question de clarification après
une réponse initiale couvrant lecture et écriture. Le périmètre retenu est Jira BST2 avec accord
explicite et Confluence en lecture seule.

### 2026-09-29 — décision — Personnalisation de config.md

Renseignement de `config.md` avec les préférences d'identité, de rôle, de casquettes, de langue,
de ton, de nommage, de plafonds, de périmètre sensible et les droits déclarés pour les outils
externes.

### 2026-09-29 — décision — Création de la casquette de suivi des externes

Création de la branche `2_Casquettes/suivi-des-externes-equipe/` et qualification de la capture
sur Abdessamade dans cette casquette. Le routage est ajouté au hub parent et aux instructions.

### 2026-09-29 — décision — Création de la casquette Tech lead Datacost

Création de la branche `2_Casquettes/tech-lead-datacost/` et consignation du suivi mensuel avec
Amine MIMOUNI. Le routage est ajouté au hub parent et aux instructions.

### 2026-09-29 — décision — Reclassement du suivi mensuel avec Amine

Après clarification, le compte rendu du suivi mensuel avec Amine MIMOUNI est rattaché à la casquette
`Suivi des externes de l'équipe`. Les fichiers et le routage provisoires de la branche Tech lead
Datacost créés lors du premier classement sont retirés.

### 2026-09-29 — friction — Ouverture inattendue de Chrome pour Google Chat

Pour identifier la conversation directe nécessaire à l'envoi via Google Workspace, l'agent a ouvert
Google Chat dans une fenêtre Chrome sans prévenir. L'envoi a été réalisé via `gws chat +send`, mais
l'ouverture du navigateur a surpris l'utilisateur. L'utilisateur a précisé qu'il fallait rester dans
la skill Google Workspace, sans ouvrir Chrome ; si l'identifiant nécessaire n'est pas accessible
dans ce flux, demander cet identifiant plutôt que passer par l'interface web.

### 2026-09-29 — décision — Annuaire de contacts Google Workspace

Création d'un annuaire dans `3_Ressources/annuaire-contacts/` pour réutiliser les coordonnées
Google Workspace validées lors des demandes de contact. Utiliser la skill Google Workspace sans
ouvrir Chrome ; demander à Robin tout identifiant de conversation manquant plutôt que le chercher
dans l'interface web.

### 2026-09-29 — décision — Préparation des suivis mensuels d'équipe

À chaque demande de préparation d'un suivi mensuel avec une personne de l'équipe, retrouver et
présenter le fichier de son dernier EI, puis lister les tickets Jira qu'elle a effectués entre la
date de cet EI et la date du jour. Si le fichier ou la date de l'EI ne peut pas être retrouvé,
signaler ce qui manque plutôt que supposer la période.

### 2026-09-29 — décision — Période Jira sans EI antérieur

Précision de la règle « Préparation des suivis mensuels d'équipe » : si aucun EI antérieur n'existe,
ne pas chercher de fichier de dernier EI et lister uniquement les tickets Jira effectués au cours
du mois précédent.
