---
description: Socle de règles de travail de l'agent dans ce second brain — lu à chaque session.
created_date: 2026-09-19 20:53:34
---
# Instructions Copilot — Second Brain

Second brain personnel en 5 dossiers (IPCRA) : `0_Inbox` capture le brut · `1_Projets` a des dates
de fin · `2_Casquettes` sont des rôles permanents · `3_Ressources` est réutilisable et transverse ·
`4_Archives` est terminé ou inactif. `5_Rappels/` accueille les rappels durables et transverses.
`_systeme/` porte le fonctionnement du système ; `docs/` s'adresse à l'humain et sort de ton
contexte, renvoies-y par un chemin seulement.

## 1. Lire `config.md` en premier

En début de session : identité, casquettes, ton, conventions, plafonds, périmètre sensible, outils.

## 2. Routage : hub → registry → cible

Pour toute demande, identifie le dossier IPCRA concerné ou la file transverse `5_Rappels/`, puis lis
son hub homonyme (`X/X.md`) — c'est lui qu'on lit, jamais le dossier. Utilise son **Registry Rapide**
pour trouver le chemin exact, puis va directement à la cible.

Après toute création, qualification, transformation, déplacement, renommage, archivage ou
suppression : mets à jour les Registry Rapide concernés, retire les chemins obsolètes, répare les
wikilinks. Après toute écriture, résume les changements ; pour une réponse fondée sur le vault, cite
la note source. Tout ceci est natif : l'utilisateur n'a pas à le demander dans son prompt.

## 3. Sobriété

Arrête-toi dès que la réponse est déterminable au niveau courant. N'ouvre une source secondaire
qu'en cas de donnée manquante, contradiction, ambiguïté réelle ou demande de recoupement. Aucune
exploration à l'aveugle (`find`/`ls` global) quand un registry existe. Deux exceptions :

- **Régénérer un registry** (revue hebdo) : découvrir ce qui manque suppose de parcourir. Reste dans
  la seule branche concernée et ne lis que le frontmatter, jamais le corps des notes :
  `grep -r -m1 -H '^description:' <branche>/ --include='*.md'`
- **Chemin de registry introuvable** : le registry est périmé. Même parcours, limité à cette
  branche ; corrige la ligne et signale l'écart dans ton résumé.

Un Registry Rapide est un index régénérable, jamais la source de vérité : quand il contredit le
système de fichiers, c'est lui qui a tort.

**Budget : 5 fichiers ouverts au maximum par réponse** — au-delà, dis-le et demande. Cherche avant
d'ouvrir (`grep`) ; sur un fichier de plus de 200 lignes, lis la plage utile, jamais l'intégralité.

## 4. Plafonds

Valeurs dans `config.md §5` — lis-les là, ne les recopie pas ici.

Un plafond protège ton contexte. Il s'impose quand un fichier est **lu en entier** *et* **croît
sans borne propre** : socle, `config.md`, `README.md`, hub, note de contexte, note atomique,
capture, procédure. Il ne s'impose pas dès que l'une des deux conditions manque — un journal ou une
table se consulte par extrait, une file d'attente se lit en entier mais se vide en routine. Ne
signale jamais de dépassement sur ces fichiers-là, et ne compte pas les lignes de table dans le
fichier qui les porte.

Dépassement en prose → extraire le thème dominant en note atomique. Table devenue illisible → ne pas
l'extraire mais la **partitionner** selon son axe naturel (glossaire par initiale, décisions par
année → `Decisions_Log/2026.md`), le parent devenant un hub vers ses partitions. Jamais d'extension
du plafond, ni d'extraction ou de partition sans accord.

## 5. Glossaire

Avant d'interpréter un acronyme, consulte `3_Ressources/Glossaire/Glossaire.md`. Terme absent ou
ambigu → demande, ne devine pas. Après clarification, mets à jour l'entrée.

## 6. Journal système et routines

Toute décision, arbitrage ou évolution sur le **fonctionnement** du second brain (organisation,
règles, workflows, conventions, outils, gouvernance) va dans `_systeme/journal.md` avant de terminer
la conversation. Les décisions **métier** vont dans `3_Ressources/Decisions_Log/`.

Consigne aussi les **frictions**, au moment où elles se produisent et même sans décision à la clé :
une question qu'il a fallu reposer, une consigne répétée, une règle qui a gêné, une erreur de ta
part qui a été corrigée. Une friction non écrite est perdue — or c'est elle qui alimente le comptage
des répétitions (voir « Amélioration continue ») et la rétro mensuelle. Ne la garde pas pour la fin : écris-la quand elle
survient.

Chaque entrée commence par `### AAAA-MM-JJ — <type> — <sujet>`, `<type>` valant `décision`,
`friction`, `revue` ou `incident`. C'est ce qui rend le journal filtrable par les routines.

Les procédures d'entretien sont dans `_systeme/routines.md` — ne les recopie pas ici, renvoie-y.
Revue hebdo ou rétro mensuelle demandée → lis cette note et applique sa checklist complète sans
attendre qu'elle soit recopiée.

## 7. Amélioration continue

Le comptage n'est pas une impression, il se vérifie. Avant de proposer quoi que ce soit, cherche une
friction antérieure sur le même sujet : `grep -n 'friction' _systeme/journal.md`.

- **1re occurrence** → une entrée `friction` dans le journal, rien d'autre.
- **2e occurrence** → une ligne dans `_systeme/ameliorations.md`, avec le nombre d'occurrences et la
  date de la première. Jamais d'ajout au socle à ce stade.
- **3e occurrence réelle** → alors seulement, une règle ou une skill peut s'écrire, après accord.

Jamais par anticipation, jamais au-delà de ce que les occurrences constatées justifient.

## 8. Gouvernance d'écriture

Un *constat* (énoncé en direct, terme relevé, registry régénéré) s'écrit directement. Une
*inférence* (déduite d'un corpus, d'un message, d'un outil externe) passe par
`_systeme/a-valider.md`. Ce que `config.md §6` déclare sensible ne s'écrit **jamais** dans le vault.
En reformulant, conserve frontmatter, dates, faits, sources et wikilinks ; ne change rien d'autre.

Un fait a un seul domicile : ne recopie pas le contenu d'une note dans une autre, mets un wikilink.

Quand l'utilisateur annonce l'installation d'un nouvel outil externe ou MCP, ou que le contexte signale explicitement son ajout au projet, mets à jour `config.md §7` dans la même opération, sans attendre une demande distincte. Ajoute ou complète une ligne avec le nom et les capacités confirmées par les informations disponibles. Ne déduis pas les autorisations de l'utilisateur à partir des capacités techniques : si le périmètre de lecture ou d'action n'est pas précisé, indique `à préciser` dans les champs concernés et demande les précisions. Ne crée pas de doublon ; remplace les mentions `à préciser` après clarification. Les skills seuls ne sont pas des outils externes à inscrire dans ce tableau.

## 9. Inbox et TEMP

Toute capture brute entre par `0_Inbox/` ; `0_Inbox/TEMP/` est jetable, vidé après traitement. Une
capture qualifiée part vers sa branche cible, quitte l'Inbox, et les deux registries sont mis à jour
dans la même opération.

## 10. Archives

`4_Archives/` est exclu de ton contexte par `.copilotignore`, mais ne compte pas dessus : **ne lis
jamais un fichier de `4_Archives/` autre que son hub**. Le hub dit ce qui a été archivé et où, cela
suffit. Tout élément archivé va dans un **sous-dossier**, jamais en fichier isolé à la racine que
l'exclusion ne couvre pas ; il n'en ressort que sur demande explicite, déplacé avant d'être lu.

## 11. Création de note

Aucun gabarit imposé : structure la note comme le sujet l'exige. Une seule contrainte, tout fichier
de contenu commence par un frontmatter — bloc `---` en **première ligne**, rien au-dessus — avec une
`description:` d'une phrase, dont la revue hebdo régénère les registries. Frontmatter minimal
(`description`, `created_date`), wikilinks `[[Nom]]`, lisibilité conservée en Markdown brut.

Une **note de contexte** porte en plus `status:` (`actif`, `en pause`, `clos`), ce qui rend « quels
projets sont actifs ? » répondable par `grep` sans ouvrir les notes. Ne stocke jamais de date de
dernière modification : git la connaît — `git log -1 --format=%ad -- <fichier>`.

Avant toute création de dossier, hub, note de contexte ou note atomique — et avant toute
modification structurelle d'un contenu existant — lis le hub parent et
`3_Ressources/Pattern_Extensibilite/Pattern_Extensibilite.md`, applique le pattern, puis mets à jour
le Registry Rapide concerné. C'est natif : l'utilisateur n'a pas à le demander.

Contrôle de démarrage demandé → diagnostic seul : placeholders de `config.md`, Registry Rapide,
frontmatter, captures d'`0_Inbox/`, contenu temporaire. N'écris qu'après accord explicite.

## 12. Skills

Avant d'improviser une procédure récurrente, regarde les skills disponibles dans `.agents/skills/`.
