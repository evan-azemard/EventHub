#!/bin/bash

# Script de création des labels GitHub pour EventHub
# Usage: ./create-labels.sh

REPO="evan-azemard/EventHub"

echo "🏷️  Création des labels pour $REPO"
echo "========================================"

# Labels par rôle utilisateur
echo "📋 Création des labels par rôle..."
gh label create "user" --description "Fonctionnalités utilisateur" --color "0E8A16" --repo $REPO 2>/dev/null || echo "  ✓ user existe déjà"
gh label create "organizer" --description "Fonctionnalités organisateur" --color "1D76DB" --repo $REPO 2>/dev/null || echo "  ✓ organizer existe déjà"
gh label create "admin" --description "Fonctionnalités administrateur" --color "D93F0B" --repo $REPO 2>/dev/null || echo "  ✓ admin existe déjà"

# Labels par domaine fonctionnel
echo ""
echo "🔧 Création des labels par domaine..."
gh label create "authentication" --description "Connexion et inscription" --color "FBCA04" --repo $REPO 2>/dev/null || echo "  ✓ authentication existe déjà"
gh label create "event" --description "Gestion des événements" --color "C5DEF5" --repo $REPO 2>/dev/null || echo "  ✓ event existe déjà"
gh label create "booking" --description "Réservation de billets" --color "BFD4F2" --repo $REPO 2>/dev/null || echo "  ✓ booking existe déjà"
gh label create "payment" --description "Paiement et remboursement" --color "006B75" --repo $REPO 2>/dev/null || echo "  ✓ payment existe déjà"
gh label create "profile" --description "Gestion du profil" --color "C2E0C6" --repo $REPO 2>/dev/null || echo "  ✓ profile existe déjà"
gh label create "category" --description "Gestion des catégories" --color "5319E7" --repo $REPO 2>/dev/null || echo "  ✓ category existe déjà"
gh label create "analytics" --description "Analyses et statistiques" --color "0052CC" --repo $REPO 2>/dev/null || echo "  ✓ analytics existe déjà"
gh label create "notification" --description "Notifications et emails" --color "F9D0C4" --repo $REPO 2>/dev/null || echo "  ✓ notification existe déjà"
gh label create "configuration" --description "Configuration système" --color "5A6269" --repo $REPO 2>/dev/null || echo "  ✓ configuration existe déjà"
gh label create "history" --description "Historique et archives" --color "D4C5F9" --repo $REPO 2>/dev/null || echo "  ✓ history existe déjà"
gh label create "filter" --description "Filtres et recherche" --color "C5DEF5" --repo $REPO 2>/dev/null || echo "  ✓ filter existe déjà"
gh label create "notes" --description "Notes personnelles" --color "BFDADC" --repo $REPO 2>/dev/null || echo "  ✓ notes existe déjà"
gh label create "pricing" --description "Tarification" --color "008672" --repo $REPO 2>/dev/null || echo "  ✓ pricing existe déjà"
gh label create "qrcode" --description "QR Code" --color "000000" --repo $REPO 2>/dev/null || echo "  ✓ qrcode existe déjà"
gh label create "validation" --description "Validation de billets" --color "0E8A16" --repo $REPO 2>/dev/null || echo "  ✓ validation existe déjà"
gh label create "participants" --description "Gestion des participants" --color "BFDADC" --repo $REPO 2>/dev/null || echo "  ✓ participants existe déjà"
gh label create "refund" --description "Remboursements" --color "D93F0B" --repo $REPO 2>/dev/null || echo "  ✓ refund existe déjà"
gh label create "email" --description "Envoi d'emails" --color "FEF2C0" --repo $REPO 2>/dev/null || echo "  ✓ email existe déjà"
gh label create "dashboard" --description "Tableau de bord" --color "0052CC" --repo $REPO 2>/dev/null || echo "  ✓ dashboard existe déjà"
gh label create "labels" --description "Gestion des labels" --color "EDEDED" --repo $REPO 2>/dev/null || echo "  ✓ labels existe déjà"

# Labels par couche technique
echo ""
echo "💻 Création des labels techniques..."
gh label create "frontend" --description "Développement client (React)" --color "61DAFB" --repo $REPO 2>/dev/null || echo "  ✓ frontend existe déjà"
gh label create "backend" --description "Développement serveur (Express)" --color "68A063" --repo $REPO 2>/dev/null || echo "  ✓ backend existe déjà"
gh label create "database" --description "Modèles et schémas de données" --color "336791" --repo $REPO 2>/dev/null || echo "  ✓ database existe déjà"
gh label create "api" --description "Endpoints API" --color "84B6EB" --repo $REPO 2>/dev/null || echo "  ✓ api existe déjà"

# Labels par priorité
echo ""
echo "⚡ Création des labels de priorité..."
gh label create "high-priority" --description "Priorité haute" --color "D93F0B" --repo $REPO 2>/dev/null || echo "  ✓ high-priority existe déjà"
gh label create "medium-priority" --description "Priorité moyenne" --color "FBCA04" --repo $REPO 2>/dev/null || echo "  ✓ medium-priority existe déjà"
gh label create "low-priority" --description "Priorité basse" --color "0E8A16" --repo $REPO 2>/dev/null || echo "  ✓ low-priority existe déjà"

# Labels par statut
echo ""
echo "📊 Création des labels de statut..."
gh label create "user-story" --description "User Story" --color "B60205" --repo $REPO 2>/dev/null || echo "  ✓ user-story existe déjà"
gh label create "ready-for-dev" --description "Prêt pour développement" --color "128A0C" --repo $REPO 2>/dev/null || echo "  ✓ ready-for-dev existe déjà"
gh label create "in-progress" --description "En cours" --color "FEF2C0" --repo $REPO 2>/dev/null || echo "  ✓ in-progress existe déjà"
gh label create "in-review" --description "En code review" --color "FBCA04" --repo $REPO 2>/dev/null || echo "  ✓ in-review existe déjà"
gh label create "done" --description "Terminé" --color "0E8A16" --repo $REPO 2>/dev/null || echo "  ✓ done existe déjà"
gh label create "security" --description "Sécurité" --color "D93F0B" --repo $REPO 2>/dev/null || echo "  ✓ security existe déjà"
gh label create "status" --description "Statut des événements" --color "C5DEF5" --repo $REPO 2>/dev/null || echo "  ✓ status existe déjà"

echo ""
echo "✅ Création des labels terminée!"
echo ""
echo "Pour voir tous les labels:"
echo "  gh label list --repo $REPO"
