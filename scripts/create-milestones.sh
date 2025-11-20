#!/bin/bash

# Script de création des milestones GitHub pour EventHub
# Usage: ./create-milestones.sh

REPO="evan-azemard/EventHub"

echo "🎯 Création des milestones pour $REPO"
echo "========================================"

# Sprint 1 - Fondations
echo "📌 Sprint 1 - Fondations"
gh milestone create "Sprint 1 - Fondations" \
  --description "US-001, US-002, US-015, US-031 - Authentification de base, création d'événements simple, système de catégories" \
  --due-date "2025-01-15" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 1 existe déjà"

# Sprint 2 - Consultation et Découverte
echo "📌 Sprint 2 - Consultation"
gh milestone create "Sprint 2 - Consultation" \
  --description "US-003, US-005, US-016, US-017 - Liste et filtres d'événements, détails complets" \
  --due-date "2025-02-01" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 2 existe déjà"

# Sprint 3 - Réservation
echo "📌 Sprint 3 - Réservation"
gh milestone create "Sprint 3 - Réservation" \
  --description "US-006, US-008, US-009, US-021, US-025 - Système de réservation, paiement, génération QR codes" \
  --due-date "2025-02-28" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 3 existe déjà"

# Sprint 4 - Gestion
echo "📌 Sprint 4 - Gestion"
gh milestone create "Sprint 4 - Gestion" \
  --description "US-019, US-020, US-026, US-027 - Gestion des événements, validation des billets, gestion des participants" \
  --due-date "2025-03-15" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 4 existe déjà"

# Sprint 5 - Avancé
echo "📌 Sprint 5 - Avancé"
gh milestone create "Sprint 5 - Avancé" \
  --description "US-010, US-023, US-028, US-029 - Remboursements, formules multiples, notifications" \
  --due-date "2025-04-01" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 5 existe déjà"

# Sprint 6 - Analytics & Admin
echo "📌 Sprint 6 - Analytics"
gh milestone create "Sprint 6 - Analytics & Admin" \
  --description "US-030, US-034, US-036, US-037 - Tableaux de bord, administration" \
  --due-date "2025-04-15" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 6 existe déjà"

# Sprint 7 - Perfectionnement
echo "📌 Sprint 7 - Perfectionnement"
gh milestone create "Sprint 7 - Perfectionnement" \
  --description "User stories restantes - Profil utilisateur, fonctionnalités secondaires" \
  --due-date "2025-05-01" \
  --repo $REPO 2>/dev/null || echo "  ✓ Sprint 7 existe déjà"

echo ""
echo "✅ Création des milestones terminée!"
echo ""
echo "Pour voir tous les milestones:"
echo "  gh milestone list --repo $REPO"
