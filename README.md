# Optimisez votre CV en ligne avec React.js — Fernando BILO

Projet réalisé dans le cadre du devoir **« Optimisez votre CV en ligne avec React.js »** (Centre
Européen de Formation). Il se compose de deux parties indépendantes :

1. **`site/`** — le site vitrine / CV en ligne de Fernando BILO, en HTML, CSS et Bootstrap 5.
2. **`react-app/`** — une application React.js qui affiche les informations d'un profil GitHub.

## 1. Aperçu

- **Site statique** : page d'accueil (avec section « À propos »), services, réalisations, blog,
  contact et mentions légales, avec un header et un footer communs à toutes les pages.
- **Application React** : composant principal fonctionnel (`App.jsx`) qui récupère les données
  d'un profil GitHub via l'API publique (`useState`, `useEffect`, `useCallback`), et un composant
  séparé (`GithubProfile.jsx`) dédié uniquement à leur affichage.

## 2. Prérequis

- Un navigateur web récent pour consulter le site statique (aucune installation nécessaire).
- [Node.js](https://nodejs.org/) 18+ et npm pour lancer l'application React.
- (Optionnel) [Visual Studio Code](https://code.visualstudio.com/) ou tout autre éditeur.

## 3. Installation et lancement du site (HTML/CSS/Bootstrap)

Le site est 100 % statique : aucune installation n'est requise.

```bash
cd site
# Ouvrir index.html directement dans le navigateur, ou lancer un petit serveur local :
npx serve .
# puis ouvrir http://localhost:3000
```

### Structure

```
site/
├── index.html            # Accueil + section "À propos"
├── services.html
├── realisations.html
├── blog.html
├── contact.html
├── mentions-legales.html # non indexée (meta robots "noindex, nofollow")
├── css/
│   └── style.css         # charte graphique (couleurs, polices, effets)
├── js/
│   └── script.js         # navigation active, bouton "retour en haut", validation du formulaire
└── images/
    └── favicon.png
```

> Les visuels (photo de profil, portfolio, articles de blog, images de fond) utilisent pour le
> moment des images de démonstration (Unsplash / Picsum) afin que le site soit immédiatement
> fonctionnel. Remplacez-les par vos propres images ou par des images libres de droits Pixabay
> avant la mise en production, en respectant les crédits sur la page « Mentions légales ».

## 4. Installation et lancement de l'application React

```bash
cd react-app
npm install
npm run dev
# puis ouvrir l'URL affichée dans le terminal (http://localhost:5173 par défaut)
```

Autres commandes utiles :

```bash
npm run build     # génère la version de production dans react-app/dist
npm run preview   # sert la version buildée localement
npm run lint       # vérifie la qualité du code (ESLint)
```

### Fonctionnement

- Par défaut, l'application interroge `https://api.github.com/users/github-john-doe`, le profil
  GitHub suggéré par le brief. Un champ de recherche permet aussi de tester l'application avec
  n'importe quel autre identifiant GitHub réel (par exemple `octocat`).
- `App.jsx` est le composant fonctionnel principal : il gère l'état (`useState`), l'appel réseau
  (`useEffect` + `useCallback`) et les cas de chargement / erreur.
- `src/components/GithubProfile.jsx` est le composant séparé chargé uniquement de l'affichage des
  informations reçues en props (avatar, nom, bio, statistiques, localisation, etc.).

### Structure

```
react-app/
├── index.html
├── package.json
├── vite.config.js
├── .eslintrc.cjs
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── index.css
    └── components/
        └── GithubProfile.jsx
```

## 5. Hébergement

- Le site statique (`site/`) peut être hébergé gratuitement sur **GitHub Pages**, Netlify ou
  Vercel.
- L'application React (`react-app/`) peut être hébergée sur **CodeSandbox**, StackBlitz, Netlify
  ou Vercel (l'hébergement d'une application React chez un hébergeur statique classique et
  gratuit étant plus limité).

## 6. Validation W3C

Avant la livraison finale, chaque page HTML du dossier `site/` doit être vérifiée avec le
validateur du W3C : <https://validator.w3.org/> (onglet « Validate by File Upload » ou « Validate
by Direct Input »), et une capture d'écran du résultat doit être fournie pour chaque page dans le
rendu final.

## 7. Auteur

Projet réalisé par **Fernando BILO** dans le cadre de la formation développeur web du Centre Européen de
Formation (CEF).
