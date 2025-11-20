# Guide de Démarrage Rapide - Création des User Stories

Ce guide vous permet de créer rapidement les 40 User Stories dans GitHub Issues.

## ⚡ Démarrage Rapide (3 commandes)

```bash
# 1. Créer les labels
./scripts/create-labels.sh

# 2. Créer les milestones  
./scripts/create-milestones.sh

# 3. Créer les 40 issues
./scripts/create-issues.sh
```

**C'est tout! Les 40 user stories seront créées dans GitHub.**

## 📋 Vérification

Vérifiez que tout a été créé correctement:

```bash
# Voir les issues créées
gh issue list --repo evan-azemard/EventHub --label user-story --limit 50

# Voir les milestones
gh milestone list --repo evan-azemard/EventHub

# Voir les labels
gh label list --repo evan-azemard/EventHub | grep -E "user|organizer|admin"
```

## 🌐 Interface Web

Vous pouvez aussi voir vos issues sur:
- **Issues**: https://github.com/evan-azemard/EventHub/issues
- **Milestones**: https://github.com/evan-azemard/EventHub/milestones
- **Labels**: https://github.com/evan-azemard/EventHub/labels

## 📊 Créer un Project Board (Kanban)

### Via l'interface web:

1. Allez sur https://github.com/evan-azemard/EventHub/projects
2. Cliquez sur "New project"
3. Sélectionnez "Board" comme template
4. Nommez-le "EventHub - User Stories"
5. Ajoutez vos colonnes:
   - **Backlog** - User stories en attente
   - **Ready** - Prêt à développer
   - **In Progress** - En cours
   - **In Review** - En code review
   - **Testing** - En test
   - **Done** - Terminé

### Ajouter les issues au board:

1. Dans le project board, cliquez sur "+"
2. Recherchez vos issues (filtrez par label "user-story")
3. Ajoutez-les à la colonne "Backlog"

**OU** utilisez la commande:

```bash
# Récupérer l'ID du project (remplacer PROJECT_ID)
gh project list --owner evan-azemard

# Ajouter toutes les issues au project
gh issue list --repo evan-azemard/EventHub --label user-story --json number -q '.[].number' | \
  xargs -I {} gh project item-add PROJECT_ID --owner evan-azemard --url https://github.com/evan-azemard/EventHub/issues/{}
```

## 📖 Documentation Complète

Pour plus de détails:
- **User Stories complètes**: [USER_STORIES.md](../USER_STORIES.md)
- **Guide détaillé**: [docs/ISSUES_CREATION_GUIDE.md](../docs/ISSUES_CREATION_GUIDE.md)
- **Scripts**: [scripts/README.md](README.md)

## ✅ Checklist de Création

- [ ] GitHub CLI installé et authentifié (`gh auth status`)
- [ ] Accès en écriture au repository `evan-azemard/EventHub`
- [ ] Scripts rendus exécutables (`chmod +x scripts/*.sh`)
- [ ] Labels créés (`./scripts/create-labels.sh`)
- [ ] Milestones créés (`./scripts/create-milestones.sh`)
- [ ] Issues créées (`./scripts/create-issues.sh`)
- [ ] Project Board créé (optionnel)
- [ ] Issues ajoutées au Project Board (optionnel)

## 🎯 Résultat Attendu

Après l'exécution des scripts, vous aurez:
- ✅ 40 issues GitHub créées (US-001 à US-040)
- ✅ ~30 labels organisés par catégorie
- ✅ 7 milestones (sprints) avec dates d'échéance
- ✅ Toutes les issues avec critères d'acceptation, estimation, priorité
- ✅ Issues organisées par sprint

## 🔄 Workflow de Développement

Une fois les issues créées:

1. **Prioriser**: Triez les issues par priorité et milestone
2. **Assigner**: Assignez les issues aux développeurs
3. **Développer**: Créez une branche feature pour chaque US
   ```bash
   git checkout -b feature/US-001-connexion-utilisateur
   ```
4. **Pull Request**: Créez une PR liée à l'issue
5. **Review & Merge**: Après validation, mergez dans `dev`
6. **Fermer l'issue**: L'issue se ferme automatiquement au merge de la PR

## 💡 Conseils

- Commencez par les issues du **Sprint 1** (haute priorité)
- Utilisez les labels pour filtrer les issues
- Référencez les issues dans vos commits: `feat: implement login (closes #1)`
- Mettez à jour les critères d'acceptation pendant le développement
- Utilisez le Project Board pour suivre l'avancement

## 🆘 Besoin d'aide?

Si vous rencontrez des problèmes:
1. Vérifiez que GitHub CLI est bien authentifié: `gh auth status`
2. Vérifiez les permissions sur le repository
3. Consultez le [guide détaillé](../docs/ISSUES_CREATION_GUIDE.md)
4. Vérifiez les logs des scripts pour les erreurs

---

**Bon développement! 🚀**
