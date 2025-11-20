# Scripts pour la Création des User Stories EventHub

Ce répertoire contient des scripts pour automatiser la création des 40 User Stories dans GitHub.

## 📁 Contenu

### Scripts Shell (.sh)

1. **create-labels.sh** - Crée tous les labels nécessaires dans le repository
2. **create-milestones.sh** - Crée les 7 sprints (milestones) dans le repository  
3. **create-issues.sh** - Crée les 40 issues GitHub avec les user stories

### Scripts Python (.py)

1. **generate-issue-bodies.py** - Génère les fichiers markdown de corps d'issues (déjà exécuté)

## 🚀 Utilisation

### Prérequis

- GitHub CLI (`gh`) installé et authentifié
- Accès en écriture au repository `evan-azemard/EventHub`
- Python 3.6+ (pour regénérer les bodies si nécessaire)

### Authentification GitHub CLI

Si ce n'est pas déjà fait:

```bash
gh auth login
```

### Étape 1: Créer les labels

```bash
./scripts/create-labels.sh
```

Ce script crée environ 30+ labels organisés par:
- Rôle utilisateur (user, organizer, admin)
- Domaine fonctionnel (authentication, event, booking, payment, etc.)
- Couche technique (frontend, backend, database, api)
- Priorité (high-priority, medium-priority, low-priority)
- Statut (user-story, ready-for-dev, in-progress, etc.)

### Étape 2: Créer les milestones

```bash
./scripts/create-milestones.sh
```

Ce script crée 7 milestones correspondant aux sprints:
- Sprint 1 - Fondations (échéance: 2025-01-15)
- Sprint 2 - Consultation (échéance: 2025-02-01)
- Sprint 3 - Réservation (échéance: 2025-02-28)
- Sprint 4 - Gestion (échéance: 2025-03-15)
- Sprint 5 - Avancé (échéance: 2025-04-01)
- Sprint 6 - Analytics & Admin (échéance: 2025-04-15)
- Sprint 7 - Perfectionnement (échéance: 2025-05-01)

### Étape 3: Créer les issues

```bash
./scripts/create-issues.sh
```

Ce script crée les 40 issues GitHub avec:
- Titre formaté (US-XXX: Description)
- Corps complet avec critères d'acceptation
- Labels appropriés
- Milestone assigné
- Definition of Done

### Regénérer les corps d'issues (optionnel)

Si vous devez modifier les user stories et regénérer les fichiers:

```bash
python3 scripts/generate-issue-bodies.py
```

Cela régénérera tous les fichiers dans `.github/issue-bodies/`

## 📊 Vérification

Après l'exécution, vérifiez:

```bash
# Voir tous les labels
gh label list --repo evan-azemard/EventHub

# Voir tous les milestones
gh milestone list --repo evan-azemard/EventHub

# Voir toutes les user stories
gh issue list --repo evan-azemard/EventHub --label user-story

# Voir les issues d'un sprint spécifique
gh issue list --repo evan-azemard/EventHub --milestone "Sprint 1 - Fondations"
```

## 🎯 Ordre d'exécution recommandé

```bash
# 1. Générer les bodies (déjà fait)
python3 scripts/generate-issue-bodies.py

# 2. Créer les labels
./scripts/create-labels.sh

# 3. Créer les milestones
./scripts/create-milestones.sh

# 4. Créer les issues
./scripts/create-issues.sh
```

## 📝 Structure des fichiers générés

```
.github/
├── ISSUE_TEMPLATE/
│   └── user-story.yml          # Template pour créer manuellement des US
└── issue-bodies/
    ├── US-001.md               # Corps de l'issue US-001
    ├── US-002.md               # Corps de l'issue US-002
    └── ...                     # 40 fichiers au total
```

## 🔧 Dépannage

### Erreur: "gh command not found"

Installez GitHub CLI:
- **macOS**: `brew install gh`
- **Ubuntu/Debian**: `sudo apt install gh`
- **Windows**: `winget install --id GitHub.cli`

### Erreur: "authentication required"

Authentifiez-vous:
```bash
gh auth login
```

### Erreur: "permission denied"

Vérifiez que vous avez les permissions d'écriture sur le repository.

### Issues déjà existantes

Les scripts vérifient si les éléments existent déjà. Si une issue existe, elle ne sera pas recréée.

## 📖 Documentation complémentaire

- [USER_STORIES.md](../USER_STORIES.md) - Détails complets des 40 user stories
- [ISSUES_CREATION_GUIDE.md](../docs/ISSUES_CREATION_GUIDE.md) - Guide de création des issues
- [GitHub CLI Documentation](https://cli.github.com/manual/)

## ⚠️ Notes importantes

- Les scripts sont idempotents: vous pouvez les exécuter plusieurs fois sans problème
- Les dates d'échéance des milestones sont indicatives et peuvent être ajustées
- Les labels peuvent être personnalisés selon vos besoins
- Les issue bodies peuvent être modifiés dans `.github/issue-bodies/` avant de créer les issues

## 🤝 Support

Pour toute question ou problème:
1. Vérifiez la [documentation](../docs/ISSUES_CREATION_GUIDE.md)
2. Consultez les [User Stories](../USER_STORIES.md)
3. Ouvrez une issue sur GitHub
