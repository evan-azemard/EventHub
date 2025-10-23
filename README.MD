# EventHub

Solution de gestion d'événements et de billetterie avec réservation en ligne.

Le dépôt est organisé en monorepo pnpm avec deux workspaces : `packages/client` (frontend React + Vite) et `packages/server` (backend Express).

## Prérequis

- Node.js 20+
- [pnpm 10](https://pnpm.io/installation)

## Installation

```powershell
pnpm install
pnpm prepare
```

> **Note** : `pnpm prepare` initialise les hooks Git (Husky) pour la validation automatique des commits.

## Configuration des variables d'environnement

1. Copier les fichiers d'exemple :

   ```powershell
   cp packages\server\.env.example packages\server\.env
   cp packages\client\.env.example packages\client\.env
   ```

2. Renseigner les valeurs :

### Variables serveur (`packages/server/.env`)

| Variable     | Description                                    | Exemple               |
| ------------ | ---------------------------------------------- | --------------------- |
| `PORT`       | Port HTTP du backend                           | `3000`                |
| `NODE_ENV`   | Environnement                                  | `dev`         |
| `CORS_ORIGIN`| Origine autorisée pour CORS                    | `http://localhost:5173` |

### Variables client (`packages/client/.env`)

| Variable          | Description                    | Exemple                    |
| ----------------- | ------------------------------ | -------------------------- |
| `VITE_API_URL`    | URL de l'API backend           | `http://localhost:3000`    |

## Scripts disponibles

### À la racine

| Commande              | Description                                    |
| --------------------- | ---------------------------------------------- |
| `pnpm dev`            | Démarre client + serveur en parallèle          |
| `pnpm dev:client`     | Démarre uniquement le frontend                 |
| `pnpm dev:server`     | Démarre uniquement le backend                  |
| `pnpm build`          | Build complet (client puis serveur)            |
| `pnpm build:client`   | Build du frontend                              |
| `pnpm build:server`   | Compilation TypeScript du backend              |

### Scripts frontend (`packages/client`)

```powershell
pnpm --filter client dev          # Dev server Vite
pnpm --filter client build        # Build production
pnpm --filter client preview      # Preview du build
```

### Scripts backend (`packages/server`)

```powershell
pnpm --filter server dev          # Mode développement avec watch
pnpm --filter server build        # Compile en dist/
pnpm --filter server start        # Lance l'API compilée
```

## Arborescence

```
EventHub/
├── packages/
│   ├── client/              # Application React (Vite + TypeScript)
│   │   ├── src/
│   │   ├── public/
│   │   └── package.json
│   └── server/              # API Express (TypeScript)
│       ├── src/
│       │   ├── config/
│       │   ├── routes/
│       │   ├── services/
│       │   ├── middlewares/
│       │   └── server.ts
│       └── package.json
├── pnpm-workspace.yaml
└── package.json
```

## Docker

_(Section à compléter)_

## Workflow Git

### Branches principales

- `main` : Branche de production (code stable et déployé)
- `dev` : Branche de développement (intégration des features)

### Branches de fonctionnalités

Pour chaque user story ou fonctionnalité, créer une branche depuis `dev` :

```powershell
git checkout dev
git pull origin dev
git checkout -b feature/US-XX-nom-feature
```

### Conventions de commit

Utiliser le format suivant :

```
<type>(<scope>): <description>      # exemple: feat(client): add button to homepage
```

**Types de commit :**

- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `chore` : Tâches de maintenance (dépendances, config)
- `docs` : Documentation
- `style` : Formatage du code (sans impact fonctionnel)
- `refactor` : Refactorisation du code
- `test` : Ajout ou modification de tests
- `perf` : Amélioration des performances


### Schéma du workflow

```
  | Création d'un tag  
  ↑
main (production)
  ↑
  | merge via PR après validation
  |
  | review copilot et validation
  ↑
dev (développement)
  ↑
  | merge des features terminées
  |
feature/US-01-creation-evenement
feature/US-02-reservation-billet
feature/US-03-paiement
```

### Processus de développement

1. Créer une branche feature depuis `dev`
2. Développer et commiter avec les conventions
   - **Avant chaque commit** : Husky vérifie automatiquement le code
   - **Lint-staged** : Formate et corrige automatiquement les fichiers modifiés
   - **Commitlint** : Valide le format du message de commit
3. Pousser la branche : `git push origin feature/US-XX-nom-feature`
4. Créer une Pull Request vers `dev`
5. Après review et validation, merger dans `dev`
6. Périodiquement, merger `dev` dans `main` pour déployer en production
8. Créer un tag de version sur `main` après chaque déploiement

## Workflow de développement

1. Installer les dépendances : `pnpm install`
2. Initialiser les hooks Git : `pnpm prepare`
3. Configurer les fichiers `.env`
4. Démarrer le monorepo : `pnpm dev`
5. Accéder au client sur `http://localhost:5173`
6. Accéder à l'API sur `http://localhost:3000`

### Qualité du code

Le projet utilise des hooks Git automatiques :

- **Pre-commit** : Avant chaque commit, le code est automatiquement formaté et vérifié
  - ESLint sur le client (avec correction automatique)
  - Prettier sur le serveur
- **Commit-msg** : Le format du message de commit est validé (conventions de commit)

Si le code ou le message ne respecte pas les règles, le commit est bloqué.

## Support

Pour toute question ou problème :
- Vérifier que les ports 3000 et 5173 sont disponibles
- S'assurer que les variables d'environnement sont correctement configurées
- Vérifier que `pnpm-workspace.yaml` est bien à la racine
