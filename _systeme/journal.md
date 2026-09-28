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

### 2026-09-28 — friction — Destination d'une liste durable de rappels

La demande de créer une liste permanente de rappels catégorisés ne précise pas de projet ou de
casquette. L'Inbox est réservée aux captures datées à qualifier, les ressources excluent les
actions en cours et `_systeme/` n'accueille pas de contenu métier ; il faut convenir d'une destination
valide avant de créer la note.

### 2026-09-28 — décision — Création d'une file transverse de rappels

À la demande de l'utilisateur, création de `5_Rappels/` hors des cinq dossiers IPCRA pour accueillir
une liste durable de rappels généraux, classés automatiquement par thème. Les rappels propres à un
projet ou à une casquette restent dans leur branche de destination.

### 2026-09-28 — friction — Ambiguïté du mot « branche »

Dans l'échange sur la liste de rappels, « branche dédiée » désignait un dossier du vault, mais pouvait
être compris comme une branche Git. La distinction n'a pas été explicitée avant le choix de destination.
