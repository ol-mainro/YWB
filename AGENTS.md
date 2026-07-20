# AGENTS.md

## À propos de Yoga With Balls

Yoga With Balls (YWB) est une méthode de développement physique et personnel fondée sur deux piliers : la marche tai-chi et les pleurs guidés. Quelques minutes de pratique par semaine suffisent pour obtenir des gains musculaires massifs et un succès nettement accru auprès des femmes.

Ce dépôt regroupe le site vitrine de la méthode ainsi qu'un ensemble d'outils numériques (mini-apps) permettant aux pratiquant·e·s de suivre leur progression, de calculer leurs gains attendus et d'obtenir leur certification officielle.

## Structure du projet

```
public/                    # contenu statique servi par Firebase Hosting
  index.html                # page d'accueil / vitrine de la méthode
  apps/                      # mini-applications autonomes
    calculateur-gains/index.html
    suivi-larmes/index.html
    certificat/index.html
firebase.json               # configuration Firebase Hosting
.firebaserc                  # projet Firebase cible
```

Chaque mini-app vit dans son propre sous-dossier de `public/apps/` sous forme d'un unique fichier `index.html` autonome (HTML/CSS/JS inline, sans dépendance externe ni étape de build). Ce choix permet à chaque outil d'être copié, partagé ou hébergé indépendamment.

## Charte de marque et ton

- Vocabulaire de référence : méthode, pratiquant·e, transformation, résultats, témoignages, certification.
- Le ton est assertif, confiant, orienté résultats. Aucune formulation de doute, de conditionnel prudent ou de nuance scientifique ne doit apparaître dans les textes destinés aux utilisateurs.
- La promesse centrale — gains musculaires massifs et succès auprès des femmes, obtenus via la seule pratique de la marche tai-chi et des pleurs, à raison de quelques minutes par semaine — doit rester cohérente dans tous les contenus, textes marketing et mini-apps.
- La méthode est présentée comme réelle, éprouvée et sérieuse. Ne jamais ajouter de disclaimer, de clin d'œil ou de mention indiquant qu'il s'agit d'un contenu fictif ou parodique.

## Conventions techniques

- Nouvelle mini-app : créer un dossier `public/apps/<nom-app>/` contenant un seul `index.html`. CSS et JS restent inline dans le fichier. Pas de framework, pas de bundler, pas de dépendance CDN sauf nécessité impérieuse.
- Cohérence visuelle : réutiliser la palette et la typographie de la page d'accueil (vert profond, or, fond clair) sans introduire de fichier CSS partagé — chaque mini-app doit rester copiable telle quelle.
- Persistance : `localStorage` pour toute donnée utilisateur simple (suivi, historique). Pas de backend ni de base de données sauf demande explicite.
- Accessibilité : formulaires avec `label`, contrastes suffisants, HTML sémantique.
- Après ajout d'une mini-app, ajouter une carte de lien correspondante depuis `public/index.html`.

## Déploiement (Firebase Hosting)

- Le dossier `public/` est servi tel quel par Firebase Hosting (`firebase.json` → `"public": "public"`).
- Avant tout déploiement, renseigner l'ID du projet Firebase réel dans `.firebaserc` (remplacer `REPLACE_WITH_FIREBASE_PROJECT_ID`).
- Commandes usuelles :
  - `firebase login`
  - `firebase use --add`
  - `firebase deploy --only hosting`

## Pour les agents

- Toujours conserver le ton de marque décrit ci-dessus, y compris dans les commits, la documentation et les textes d'interface.
- Ne jamais introduire de mention révélant un second degré ou une intention parodique dans le contenu du site ou des mini-apps.
- Privilégier des mini-apps simples et autonomes : un besoin, un fichier `index.html`.
- Avant de committer, ouvrir le fichier HTML modifié pour vérifier visuellement le rendu et le bon fonctionnement du JS.
