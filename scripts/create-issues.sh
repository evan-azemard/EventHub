#!/bin/bash

# Script de création automatique des 40 User Stories dans GitHub Issues
# Usage: ./create-issues.sh

REPO="evan-azemard/EventHub"
ISSUE_DIR=".github/issue-bodies"

echo "🎫 Création des 40 User Stories pour $REPO"
echo "=============================================="
echo ""

# Vérifier que gh est installé et authentifié
if ! command -v gh &> /dev/null; then
    echo "❌ Erreur: GitHub CLI (gh) n'est pas installé"
    echo "Installation: https://cli.github.com/"
    exit 1
fi

# Vérifier l'authentification
if ! gh auth status &> /dev/null; then
    echo "❌ Erreur: Vous n'êtes pas authentifié avec GitHub CLI"
    echo "Exécutez: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI installé et authentifié"
echo ""

# Fonction pour créer une issue
create_issue() {
    local us_number=$1
    local title=$2
    local milestone=$3
    local labels=$4
    local body_file="${ISSUE_DIR}/${us_number}.md"
    
    if [ ! -f "$body_file" ]; then
        echo "  ⚠️  Fichier manquant: $body_file"
        return 1
    fi
    
    echo "  📝 Création de $us_number: $title"
    
    gh issue create \
        --repo "$REPO" \
        --title "$us_number: $title" \
        --body-file "$body_file" \
        --label "$labels" \
        --milestone "$milestone" \
        2>&1 | grep -q "https://" && echo "  ✅ Créé" || echo "  ⚠️  Erreur ou déjà existant"
}

# USER - Connexion et Authentification
echo "🔐 USER - Connexion et Authentification"
create_issue "US-001" "Connexion utilisateur" "Sprint 1 - Fondations" "user-story,user,authentication,frontend,backend,high-priority"
create_issue "US-002" "Inscription utilisateur" "Sprint 1 - Fondations" "user-story,user,authentication,frontend,backend,high-priority"

echo ""
echo "📅 USER - Consultation des Événements"
create_issue "US-003" "Voir les événements disponibles" "Sprint 2 - Consultation" "user-story,user,event,frontend,backend,high-priority"
create_issue "US-004" "Consulter l'historique d'événements" "Sprint 7 - Perfectionnement" "user-story,user,event,history,frontend,backend,medium-priority"
create_issue "US-005" "Filtrer les événements par catégorie" "Sprint 2 - Consultation" "user-story,user,event,filter,frontend,backend,medium-priority"

echo ""
echo "🎫 USER - Réservation de Billets"
create_issue "US-006" "Réserver un billet" "Sprint 3 - Réservation" "user-story,user,booking,frontend,backend,high-priority"
create_issue "US-007" "Ajouter une note à la réservation" "Sprint 7 - Perfectionnement" "user-story,user,booking,frontend,backend,low-priority"
create_issue "US-008" "Confirmer la réservation avant paiement" "Sprint 3 - Réservation" "user-story,user,booking,frontend,high-priority"
create_issue "US-009" "Payer pour la réservation" "Sprint 3 - Réservation" "user-story,user,booking,payment,backend,frontend,high-priority"
create_issue "US-010" "Annuler et obtenir remboursement" "Sprint 5 - Avancé" "user-story,user,booking,payment,refund,backend,frontend,medium-priority"

echo ""
echo "👤 USER - Gestion Profil"
create_issue "US-011" "Modifier son mot de passe" "Sprint 7 - Perfectionnement" "user-story,user,profile,security,frontend,backend,medium-priority"
create_issue "US-012" "Changer les informations de compte" "Sprint 7 - Perfectionnement" "user-story,user,profile,frontend,backend,medium-priority"
create_issue "US-013" "Ajouter une note personnelle" "Sprint 7 - Perfectionnement" "user-story,user,profile,notes,frontend,backend,low-priority"
create_issue "US-014" "Modifier une note personnelle" "Sprint 7 - Perfectionnement" "user-story,user,profile,notes,frontend,backend,low-priority"

echo ""
echo "🎭 ORGANIZER - Création d'Événements"
create_issue "US-015" "Créer un nouvel événement" "Sprint 1 - Fondations" "user-story,organizer,event,frontend,backend,high-priority"
create_issue "US-016" "Définir les détails de l'événement" "Sprint 2 - Consultation" "user-story,organizer,event,frontend,backend,high-priority"
create_issue "US-017" "Définir une catégorie" "Sprint 2 - Consultation" "user-story,organizer,event,category,frontend,backend,high-priority"
create_issue "US-018" "Définir les informations de l'édition" "Sprint 7 - Perfectionnement" "user-story,organizer,event,frontend,backend,low-priority"
create_issue "US-019" "Changer le statut de l'événement" "Sprint 4 - Gestion" "user-story,organizer,event,status,backend,frontend,high-priority"
create_issue "US-020" "Modifier les informations de l'événement" "Sprint 4 - Gestion" "user-story,organizer,event,frontend,backend,medium-priority"
create_issue "US-021" "Définir un prix" "Sprint 3 - Réservation" "user-story,organizer,event,pricing,backend,frontend,high-priority"
create_issue "US-022" "Modifier le prix" "Sprint 7 - Perfectionnement" "user-story,organizer,event,pricing,backend,frontend,medium-priority"
create_issue "US-023" "Ajouter des formules/tarifs" "Sprint 5 - Avancé" "user-story,organizer,event,pricing,backend,frontend,medium-priority"
create_issue "US-024" "Supprimer une formule" "Sprint 7 - Perfectionnement" "user-story,organizer,event,pricing,backend,frontend,low-priority"
create_issue "US-025" "Définir un code QR" "Sprint 3 - Réservation" "user-story,organizer,booking,qrcode,backend,high-priority"
create_issue "US-026" "Valider les réservations" "Sprint 4 - Gestion" "user-story,organizer,booking,validation,frontend,backend,high-priority"
create_issue "US-027" "Gérer les participants" "Sprint 4 - Gestion" "user-story,organizer,event,participants,frontend,backend,high-priority"
create_issue "US-028" "Générer un remboursement" "Sprint 5 - Avancé" "user-story,organizer,payment,refund,backend,frontend,medium-priority"
create_issue "US-029" "Envoyer une notification" "Sprint 5 - Avancé" "user-story,organizer,notification,email,backend,frontend,medium-priority"

echo ""
echo "📊 ORGANIZER - Analyses"
create_issue "US-030" "Voir les analyses de performance" "Sprint 6 - Analytics & Admin" "user-story,organizer,analytics,dashboard,frontend,backend,medium-priority"

echo ""
echo "🏷️ ADMIN - Catégories"
create_issue "US-031" "Créer une catégorie" "Sprint 1 - Fondations" "user-story,admin,category,frontend,backend,medium-priority"
create_issue "US-032" "Modifier une catégorie" "Sprint 7 - Perfectionnement" "user-story,admin,category,frontend,backend,low-priority"
create_issue "US-033" "Supprimer une catégorie" "Sprint 7 - Perfectionnement" "user-story,admin,category,backend,frontend,low-priority"

echo ""
echo "👥 ADMIN - Organisateurs"
create_issue "US-034" "Voir la liste des organisateurs" "Sprint 6 - Analytics & Admin" "user-story,admin,organizer,frontend,backend,medium-priority"
create_issue "US-035" "Supprimer un organisateur" "Sprint 7 - Perfectionnement" "user-story,admin,organizer,backend,frontend,low-priority"

echo ""
echo "⚙️ ADMIN - Configuration"
create_issue "US-036" "Accéder à la configuration globale" "Sprint 6 - Analytics & Admin" "user-story,admin,configuration,frontend,backend,medium-priority"
create_issue "US-037" "Voir les analyses globales" "Sprint 6 - Analytics & Admin" "user-story,admin,analytics,dashboard,frontend,backend,low-priority"
create_issue "US-038" "Créer un libellé personnalisé" "Sprint 7 - Perfectionnement" "user-story,admin,labels,frontend,backend,low-priority"
create_issue "US-039" "Modifier un libellé" "Sprint 7 - Perfectionnement" "user-story,admin,labels,frontend,backend,low-priority"
create_issue "US-040" "Supprimer un libellé" "Sprint 7 - Perfectionnement" "user-story,admin,labels,backend,frontend,low-priority"

echo ""
echo "=============================================="
echo "✅ Création des issues terminée!"
echo ""
echo "Pour voir toutes les issues créées:"
echo "  gh issue list --repo $REPO --label user-story"
echo ""
echo "Pour voir les issues par sprint:"
echo "  gh issue list --repo $REPO --milestone 'Sprint 1 - Fondations'"
