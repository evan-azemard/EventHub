# Guide de Création des Issues GitHub pour EventHub

Ce guide explique comment créer les 40 User Stories dans GitHub Issues pour le projet EventHub.

## Méthode 1: Utilisation du GitHub CLI (gh)

### Prérequis
- GitHub CLI installé et authentifié
- Accès en écriture au repository evan-azemard/EventHub

### Script de création automatique

Un script est fourni dans `scripts/create-issues.sh` pour créer toutes les issues automatiquement.

```bash
cd /home/runner/work/EventHub/EventHub
chmod +x scripts/create-issues.sh
./scripts/create-issues.sh
```

### Création manuelle avec gh

Pour créer une issue individuellement:

```bash
gh issue create \
  --title "US-001: Connexion utilisateur" \
  --body-file .github/issue-bodies/US-001.md \
  --label "user-story,user,authentication,frontend,backend,high-priority" \
  --assignee @me
```

## Méthode 2: Interface Web GitHub

1. Aller sur https://github.com/evan-azemard/EventHub/issues/new/choose
2. Sélectionner le template "User Story"
3. Remplir le formulaire avec les informations de la user story
4. Cliquer sur "Submit new issue"

## Méthode 3: API GitHub

Utiliser l'API REST GitHub pour créer les issues programmatiquement.

Voir le script Python dans `scripts/create-issues.py` pour un exemple.

## Organisation des Issues

### Labels à utiliser

#### Par rôle utilisateur
- `user` - Fonctionnalités utilisateur
- `organizer` - Fonctionnalités organisateur
- `admin` - Fonctionnalités administrateur

#### Par domaine fonctionnel
- `authentication` - Connexion, inscription
- `event` - Gestion des événements
- `booking` - Réservation de billets
- `payment` - Paiement et remboursement
- `profile` - Gestion du profil
- `category` - Gestion des catégories
- `analytics` - Analyses et statistiques
- `notification` - Notifications et emails
- `configuration` - Configuration système

#### Par couche technique
- `frontend` - Développement client (React)
- `backend` - Développement serveur (Express)
- `database` - Modèles et schémas de données
- `api` - Endpoints API

#### Par priorité
- `high-priority` - Priorité haute
- `medium-priority` - Priorité moyenne
- `low-priority` - Priorité basse

#### Par statut
- `user-story` - User Story
- `ready-for-dev` - Prêt pour développement
- `in-progress` - En cours
- `in-review` - En review
- `done` - Terminé

### Milestones recommandés

- **Sprint 1 - Fondations** (US-001, US-002, US-015, US-031)
- **Sprint 2 - Consultation** (US-003, US-005, US-016, US-017)
- **Sprint 3 - Réservation** (US-006, US-008, US-009, US-021, US-025)
- **Sprint 4 - Gestion** (US-019, US-020, US-026, US-027)
- **Sprint 5 - Avancé** (US-010, US-023, US-028, US-029)
- **Sprint 6 - Analytics** (US-030, US-034, US-036, US-037)
- **Sprint 7 - Perfectionnement** (Toutes les US restantes)

## Project Board (Kanban)

### Création du Project Board

1. Aller sur https://github.com/evan-azemard/EventHub/projects
2. Cliquer sur "New project"
3. Choisir "Board" template
4. Nommer: "EventHub - User Stories"

### Colonnes recommandées

1. **Backlog** - User stories en attente
2. **Ready** - Prêt à développer
3. **In Progress** - En cours de développement
4. **In Review** - En code review
5. **Testing** - En test
6. **Done** - Terminé

### Configuration des automatisations

- Quand une issue est créée → Backlog
- Quand une issue est assignée → Ready
- Quand une PR est créée → In Progress
- Quand une PR est mergée → Done

## Workflow de création complet

### Étape 1: Créer le Project Board

```bash
# Via gh CLI
gh project create --owner evan-azemard --title "EventHub - User Stories" --body "Kanban pour les 40 user stories du projet EventHub"
```

### Étape 2: Créer les labels nécessaires

```bash
# Script de création des labels
./scripts/create-labels.sh
```

### Étape 3: Créer les milestones

```bash
# Script de création des milestones
./scripts/create-milestones.sh
```

### Étape 4: Créer toutes les issues

```bash
# Script de création des issues
./scripts/create-issues.sh
```

### Étape 5: Ajouter les issues au Project Board

```bash
# Script pour ajouter au board
./scripts/add-to-project.sh
```

## Vérification

Après la création, vérifier que:

- [ ] 40 issues sont créées avec les numéros US-001 à US-040
- [ ] Toutes les issues ont les labels appropriés
- [ ] Les issues sont assignées aux bons milestones
- [ ] Le Project Board contient toutes les issues
- [ ] Les critères d'acceptation sont bien formatés en checklists
- [ ] Les estimations sont présentes
- [ ] Les priorités sont définies

## Support

Pour toute question sur la création des issues:
- Consulter la documentation: `USER_STORIES.md`
- Voir les templates: `.github/ISSUE_TEMPLATE/user-story.yml`
- Contacter l'équipe projet

## Ressources

- [Documentation USER_STORIES.md](../USER_STORIES.md) - Détails complets des 40 user stories
- [GitHub Issues](https://github.com/evan-azemard/EventHub/issues)
- [GitHub Projects](https://github.com/evan-azemard/EventHub/projects)
