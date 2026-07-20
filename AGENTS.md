# AGENTS.md

## À propos de Yoga With Balls

Yoga With Balls (YWB) est une méthode de développement physique et personnel fondée sur deux piliers : la marche tai-chi et les pleurs guidés. Quelques minutes de pratique par semaine suffisent pour obtenir des gains musculaires massifs et un succès nettement accru auprès des femmes.

Ce dépôt regroupe le site vitrine de la méthode ainsi qu'un ensemble d'outils numériques (mini-apps) permettant aux pratiquant·e·s de suivre leur progression, de calculer leurs gains attendus et d'obtenir leur certification officielle.

## Structure du projet

```
public/                    # contenu statique servi par Firebase Hosting
  index.html                # page d'accueil / vitrine de la méthode
  apps/                      # mini-applications autonomes (voir section dédiée ci-dessous)
    calculateur-gains/index.html
    suivi-larmes/index.html
    certificat/index.html
    seminaire-zenith/index.html
firebase.json               # configuration Firebase Hosting
.firebaserc                  # projet Firebase cible
```

Chaque mini-app vit dans son propre sous-dossier de `public/apps/` sous forme d'un unique fichier `index.html` autonome (HTML/CSS/JS inline, sans dépendance externe ni étape de build). Ce choix permet à chaque outil d'être copié, partagé ou hébergé indépendamment.

## Mini-apps : emplacement et règles de création

- **Emplacement** : chaque mini-app est un sous-dossier de `public/apps/`, nommé en minuscules avec tirets (kebab-case), reflétant sa fonction (ex. `calculateur-gains`, `suivi-larmes`, `certificat`, `seminaire-zenith`). L'URL publique correspondante est `/apps/<nom-app>/`.
- **Fichier unique** : le dossier ne contient qu'un seul fichier `index.html`. Pas de fichiers `.css` ou `.js` séparés, pas de dossier `assets/` — tout (styles, scripts, éventuelles données) est inline dans ce fichier.
- **Autonomie totale** : aucune dépendance à un autre fichier du dépôt (pas d'import de `public/index.html`, pas de fichier CSS partagé). Le fichier doit pouvoir être copié isolément et fonctionner tel quel.
- **Pas de build, pas de framework** : HTML/CSS/JS natifs uniquement. Pas de React/Vue/etc., pas d'étape de compilation, pas de dépendance CDN sauf nécessité impérieuse (et dans ce cas, à justifier explicitement).
- **Charte graphique** : reprendre la palette et la typographie de `public/index.html` (vert profond `--ywb-green`, or `--ywb-gold`, fond crème `--ywb-cream`) en redéfinissant les variables/styles directement dans le fichier de la mini-app.
- **Ton et contenu** : respecter strictement la charte de marque décrite ci-dessous (promesse, vocabulaire, absence de disclaimer).
- **Persistance des données** : `localStorage` uniquement pour les données utilisateur (suivi, historique, scores). Pas de backend ni de base de données sauf demande explicite.
- **Accessibilité** : `label` sur tous les champs de formulaire, contrastes suffisants, HTML sémantique.
- **Référencement depuis l'accueil** : après création d'une mini-app, ajouter une carte de lien vers `/apps/<nom-app>/` dans `public/index.html` pour qu'elle soit découvrable.

## Charte de marque et ton

- Vocabulaire de référence : méthode, pratiquant·e, transformation, résultats, témoignages, certification.
- Le ton est assertif, confiant, orienté résultats. Aucune formulation de doute, de conditionnel prudent ou de nuance scientifique ne doit apparaître dans les textes destinés aux utilisateurs.
- La promesse centrale — gains musculaires massifs et succès auprès des femmes, obtenus via la seule pratique de la marche tai-chi et des pleurs, à raison de quelques minutes par semaine — doit rester cohérente dans tous les contenus, textes marketing et mini-apps.
- La méthode est présentée comme réelle, éprouvée et sérieuse. Ne jamais ajouter de disclaimer, de clin d'œil ou de mention indiquant qu'il s'agit d'un contenu fictif ou parodique.

## Conventions techniques

Les règles spécifiques aux mini-apps (emplacement, structure, style, persistance) sont détaillées dans la section « Mini-apps : emplacement et règles de création » ci-dessus. Elles s'appliquent à toute nouvelle mini-app comme aux modifications des mini-apps existantes.

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
