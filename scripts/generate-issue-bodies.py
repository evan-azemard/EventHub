#!/usr/bin/env python3
"""
Script pour générer les fichiers de corps d'issues GitHub à partir du fichier USER_STORIES.md
Usage: python3 generate-issue-bodies.py
"""

import re
import os

# Définition des user stories avec toutes les informations
user_stories = [
    {
        "number": "US-001",
        "title": "Connexion utilisateur",
        "user_type": "utilisateur",
        "goal": "me connecter avec mon email et mot de passe",
        "benefit": "accéder à mon compte et mes réservations",
        "criteria": [
            "Formulaire de connexion avec champs email et mot de passe",
            "Validation des champs (email valide, mot de passe non vide)",
            "Message d'erreur en cas d'identifiants incorrects",
            "Redirection vers le tableau de bord après connexion réussie",
            "Option \"Se souvenir de moi\" pour rester connecté",
            "Token JWT généré et stocké en session sécurisée"
        ],
        "estimation": "3",
        "priority": "Haute",
        "labels": "user, authentication, frontend, backend",
        "milestone": "Sprint 1 - Fondations"
    },
    {
        "number": "US-002",
        "title": "Inscription utilisateur",
        "user_type": "visiteur",
        "goal": "créer un compte utilisateur",
        "benefit": "pouvoir réserver des billets et gérer mon profil",
        "criteria": [
            "Formulaire d'inscription avec nom, prénom, email, mot de passe",
            "Validation de la force du mot de passe (min 8 caractères, majuscule, chiffre)",
            "Vérification que l'email n'existe pas déjà",
            "Confirmation du mot de passe",
            "Acceptation des conditions générales d'utilisation",
            "Email de confirmation envoyé après inscription",
            "Compte créé avec rôle \"USER\" par défaut"
        ],
        "estimation": "5",
        "priority": "Haute",
        "labels": "user, authentication, frontend, backend",
        "milestone": "Sprint 1 - Fondations"
    },
    {
        "number": "US-003",
        "title": "Voir les événements disponibles",
        "user_type": "utilisateur",
        "goal": "consulter la liste de tous les événements disponibles",
        "benefit": "découvrir les événements qui m'intéressent",
        "criteria": [
            "Liste paginée des événements actifs (statut: publié)",
            "Affichage des informations essentielles: titre, date, lieu, image",
            "Carte ou grille responsive adaptée mobile/desktop",
            "Tri par défaut: événements à venir en premier",
            "Indication de disponibilité des billets",
            "Navigation vers le détail de l'événement au clic"
        ],
        "estimation": "5",
        "priority": "Haute",
        "labels": "user, event, frontend, backend",
        "milestone": "Sprint 2 - Consultation"
    },
    {
        "number": "US-004",
        "title": "Consulter l'historique d'événements",
        "user_type": "utilisateur connecté",
        "goal": "voir la liste de mes événements passés",
        "benefit": "retrouver mes anciennes réservations et souvenirs",
        "criteria": [
            "Accès via le profil utilisateur",
            "Liste des événements avec réservations confirmées dans le passé",
            "Affichage: nom événement, date, nombre de billets, statut",
            "Tri chronologique inverse (plus récent en premier)",
            "Option de télécharger les billets passés (PDF)",
            "Accès aux détails de chaque réservation"
        ],
        "estimation": "3",
        "priority": "Moyenne",
        "labels": "user, event, history, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-005",
        "title": "Filtrer les événements par catégorie",
        "user_type": "utilisateur",
        "goal": "filtrer les événements par catégorie",
        "benefit": "trouver rapidement les événements qui m'intéressent",
        "criteria": [
            "Menu de filtres avec toutes les catégories disponibles",
            "Possibilité de sélectionner une ou plusieurs catégories",
            "Mise à jour dynamique de la liste sans rechargement de page",
            "Affichage du nombre de résultats pour chaque catégorie",
            "Option pour réinitialiser tous les filtres",
            "URL mise à jour pour permettre le partage des filtres"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "user, event, filter, frontend, backend",
        "milestone": "Sprint 2 - Consultation"
    },
    {
        "number": "US-006",
        "title": "Réserver un billet",
        "user_type": "utilisateur connecté",
        "goal": "réserver un ou plusieurs billets pour un événement",
        "benefit": "participer à cet événement",
        "criteria": [
            "Sélection du nombre de billets disponibles",
            "Vérification de la disponibilité en temps réel",
            "Affichage du prix total calculé automatiquement",
            "Choix de la formule/tarif si applicable (normal, VIP, étudiant)",
            "Validation que l'utilisateur ne dépasse pas la limite par personne",
            "Ajout au panier ou réservation directe",
            "Réservation temporaire avec minuteur (ex: 10 min)"
        ],
        "estimation": "8",
        "priority": "Haute",
        "labels": "user, booking, frontend, backend",
        "milestone": "Sprint 3 - Réservation"
    },
    {
        "number": "US-007",
        "title": "Ajouter une note à la réservation",
        "user_type": "utilisateur",
        "goal": "ajouter une note ou commentaire à ma réservation",
        "benefit": "communiquer des informations spéciales à l'organisateur",
        "criteria": [
            "Champ texte optionnel lors de la réservation",
            "Limitation de caractères (ex: 500 caractères)",
            "Sauvegarde de la note avec la réservation",
            "Visible par l'utilisateur dans les détails de sa réservation",
            "Visible par l'organisateur dans la gestion des participants",
            "Possibilité de modifier la note avant le paiement"
        ],
        "estimation": "2",
        "priority": "Basse",
        "labels": "user, booking, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-008",
        "title": "Confirmer la réservation avant paiement",
        "user_type": "utilisateur",
        "goal": "voir un récapitulatif de ma réservation avant de payer",
        "benefit": "vérifier que toutes les informations sont correctes",
        "criteria": [
            "Page de récapitulatif avec tous les détails: événement, date, billets, prix",
            "Affichage des informations personnelles",
            "Affichage de la note personnelle si ajoutée",
            "Conditions d'annulation et de remboursement visibles",
            "Bouton \"Modifier\" pour retourner à l'étape précédente",
            "Bouton \"Procéder au paiement\" pour continuer",
            "Checkbox de confirmation des CGV"
        ],
        "estimation": "3",
        "priority": "Haute",
        "labels": "user, booking, frontend",
        "milestone": "Sprint 3 - Réservation"
    },
    {
        "number": "US-009",
        "title": "Payer pour la réservation",
        "user_type": "utilisateur",
        "goal": "effectuer le paiement de ma réservation de manière sécurisée",
        "benefit": "confirmer définitivement mes billets",
        "criteria": [
            "Intégration d'une solution de paiement sécurisée (Stripe/PayPal)",
            "Formulaire de paiement avec carte bancaire",
            "Validation et chiffrement des données de paiement",
            "Gestion des erreurs de paiement avec messages clairs",
            "Confirmation immédiate après paiement réussi",
            "Email de confirmation avec billets PDF envoyé",
            "Génération du QR code unique pour chaque billet",
            "Mise à jour du statut de la réservation à \"confirmée\""
        ],
        "estimation": "13",
        "priority": "Haute",
        "labels": "user, booking, payment, backend, frontend",
        "milestone": "Sprint 3 - Réservation"
    },
    {
        "number": "US-010",
        "title": "Annuler et obtenir remboursement",
        "user_type": "utilisateur",
        "goal": "annuler ma réservation et obtenir un remboursement",
        "benefit": "récupérer mon argent si je ne peux pas assister à l'événement",
        "criteria": [
            "Bouton d'annulation dans les détails de la réservation",
            "Vérification des conditions d'annulation (délai minimum avant événement)",
            "Confirmation de l'annulation avec avertissement",
            "Calcul automatique du montant du remboursement (selon politique)",
            "Traitement du remboursement via la plateforme de paiement",
            "Email de confirmation d'annulation et remboursement",
            "Mise à jour du statut à \"annulée\" et \"remboursée\"",
            "Libération des places pour d'autres utilisateurs"
        ],
        "estimation": "8",
        "priority": "Moyenne",
        "labels": "user, booking, payment, refund, backend, frontend",
        "milestone": "Sprint 5 - Avancé"
    },
    {
        "number": "US-011",
        "title": "Modifier son mot de passe",
        "user_type": "utilisateur connecté",
        "goal": "changer mon mot de passe",
        "benefit": "sécuriser mon compte ou mettre à jour mes identifiants",
        "criteria": [
            "Formulaire accessible depuis les paramètres du profil",
            "Demande de l'ancien mot de passe pour vérification",
            "Deux champs pour le nouveau mot de passe (confirmation)",
            "Validation de la force du nouveau mot de passe",
            "Message d'erreur si l'ancien mot de passe est incorrect",
            "Confirmation de succès après modification",
            "Email de notification envoyé pour informer du changement"
        ],
        "estimation": "3",
        "priority": "Moyenne",
        "labels": "user, profile, security, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-012",
        "title": "Changer les informations de compte",
        "user_type": "utilisateur connecté",
        "goal": "modifier mes informations personnelles",
        "benefit": "garder mon profil à jour",
        "criteria": [
            "Formulaire pré-rempli avec les informations actuelles",
            "Modification possible: nom, prénom, email, téléphone, adresse",
            "Validation des champs (email valide, format téléphone)",
            "Vérification que le nouvel email n'est pas déjà utilisé",
            "Confirmation par email si l'email est modifié",
            "Sauvegarde immédiate des modifications",
            "Message de confirmation de mise à jour"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "user, profile, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-013",
        "title": "Ajouter une note personnelle",
        "user_type": "utilisateur connecté",
        "goal": "ajouter des notes personnelles à mes événements favoris",
        "benefit": "me rappeler pourquoi je m'intéresse à cet événement",
        "criteria": [
            "Option \"Ajouter une note\" visible sur la page de détail de l'événement",
            "Zone de texte pour saisir la note (limite: 1000 caractères)",
            "Sauvegarde automatique ou bouton de sauvegarde",
            "Affichage de la note lors des consultations futures",
            "Note privée, visible uniquement par l'utilisateur",
            "Horodatage de création de la note"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "user, profile, notes, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-014",
        "title": "Modifier une note personnelle",
        "user_type": "utilisateur connecté",
        "goal": "modifier ou supprimer mes notes personnelles",
        "benefit": "mettre à jour mes réflexions sur un événement",
        "criteria": [
            "Bouton \"Modifier\" visible sur les notes existantes",
            "Zone de texte éditable avec le contenu actuel",
            "Bouton \"Enregistrer\" pour sauvegarder les modifications",
            "Bouton \"Supprimer\" pour effacer la note",
            "Confirmation avant suppression",
            "Horodatage de dernière modification",
            "Annulation possible avant sauvegarde"
        ],
        "estimation": "2",
        "priority": "Basse",
        "labels": "user, profile, notes, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-015",
        "title": "Créer un nouvel événement",
        "user_type": "organisateur",
        "goal": "créer un nouvel événement",
        "benefit": "promouvoir et vendre des billets pour mon événement",
        "criteria": [
            "Formulaire de création accessible depuis le tableau de bord organisateur",
            "Champs obligatoires: titre, description courte",
            "Workflow guidé en plusieurs étapes (wizard)",
            "Sauvegarde automatique en brouillon",
            "Validation des champs à chaque étape",
            "Création de l'événement avec statut \"brouillon\"",
            "Redirection vers l'édition des détails après création"
        ],
        "estimation": "5",
        "priority": "Haute",
        "labels": "organizer, event, frontend, backend",
        "milestone": "Sprint 1 - Fondations"
    },
    {
        "number": "US-016",
        "title": "Définir les détails de l'événement",
        "user_type": "organisateur",
        "goal": "renseigner tous les détails de mon événement",
        "benefit": "fournir toutes les informations nécessaires aux participants",
        "criteria": [
            "Champs: titre, description complète, date/heure début et fin",
            "Champs: lieu (adresse complète), capacité maximale",
            "Upload d'image principale (bannière)",
            "Upload de galerie d'images additionnelles (max 5)",
            "Éditeur de texte riche pour la description",
            "Aperçu en temps réel de l'affichage public",
            "Validation de la cohérence des dates (fin après début)",
            "Sauvegarde des modifications"
        ],
        "estimation": "8",
        "priority": "Haute",
        "labels": "organizer, event, frontend, backend",
        "milestone": "Sprint 2 - Consultation"
    },
    {
        "number": "US-017",
        "title": "Définir une catégorie",
        "user_type": "organisateur",
        "goal": "assigner une ou plusieurs catégories à mon événement",
        "benefit": "permettre aux utilisateurs de le trouver facilement",
        "criteria": [
            "Liste déroulante des catégories disponibles",
            "Possibilité de sélectionner une catégorie principale",
            "Possibilité d'ajouter des catégories secondaires (max 3)",
            "Affichage des catégories sous forme de tags",
            "Catégories gérées par les administrateurs",
            "Sauvegarde de la sélection"
        ],
        "estimation": "3",
        "priority": "Haute",
        "labels": "organizer, event, category, frontend, backend",
        "milestone": "Sprint 2 - Consultation"
    },
    {
        "number": "US-018",
        "title": "Définir les informations de l'édition",
        "user_type": "organisateur",
        "goal": "préciser les informations spécifiques à cette édition de l'événement",
        "benefit": "distinguer les différentes occurrences d'un événement récurrent",
        "criteria": [
            "Champ numéro d'édition (ex: \"5ème édition\")",
            "Champ année",
            "Champ thème de l'édition (optionnel)",
            "Référence à l'événement parent si récurrent",
            "Historique des éditions précédentes visible",
            "Lien vers les éditions passées si applicable"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "organizer, event, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-019",
        "title": "Changer le statut de l'événement",
        "user_type": "organisateur",
        "goal": "modifier le statut de mon événement (brouillon, publié, annulé, terminé)",
        "benefit": "contrôler sa visibilité et sa disponibilité",
        "criteria": [
            "Statuts disponibles: brouillon, publié, annulé, terminé",
            "Menu déroulant pour changer le statut",
            "Confirmation requise pour passage en \"publié\"",
            "Validation que tous les champs requis sont remplis avant publication",
            "Notification automatique aux utilisateurs intéressés lors de la publication",
            "Email aux participants en cas d'annulation",
            "Historique des changements de statut avec horodatage"
        ],
        "estimation": "5",
        "priority": "Haute",
        "labels": "organizer, event, status, backend, frontend",
        "milestone": "Sprint 4 - Gestion"
    },
    {
        "number": "US-020",
        "title": "Modifier les informations de l'événement",
        "user_type": "organisateur",
        "goal": "modifier les informations d'un événement existant",
        "benefit": "corriger des erreurs ou mettre à jour les détails",
        "criteria": [
            "Accès au formulaire d'édition depuis le tableau de bord",
            "Tous les champs modifiables (sauf ID et dates de création)",
            "Aperçu des modifications avant sauvegarde",
            "Notification automatique aux participants si modifications majeures (date, lieu)",
            "Historique des modifications avec auteur et horodatage",
            "Restrictions sur certaines modifications si billets vendus",
            "Sauvegarde des modifications"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "organizer, event, frontend, backend",
        "milestone": "Sprint 4 - Gestion"
    },
    {
        "number": "US-021",
        "title": "Définir un prix",
        "user_type": "organisateur",
        "goal": "définir le prix des billets pour mon événement",
        "benefit": "générer des revenus",
        "criteria": [
            "Champ prix avec validation (nombre positif, 2 décimales max)",
            "Sélection de la devise (EUR par défaut)",
            "Option \"Événement gratuit\" (prix = 0)",
            "Prix minimum configurable",
            "Affichage du prix TTC et HT si applicable",
            "Calcul des frais de service visible",
            "Sauvegarde du prix"
        ],
        "estimation": "3",
        "priority": "Haute",
        "labels": "organizer, event, pricing, backend, frontend",
        "milestone": "Sprint 3 - Réservation"
    },
    {
        "number": "US-022",
        "title": "Modifier le prix",
        "user_type": "organisateur",
        "goal": "modifier le prix des billets",
        "benefit": "ajuster ma stratégie tarifaire",
        "criteria": [
            "Formulaire de modification du prix accessible",
            "Avertissement si des billets ont déjà été vendus",
            "Option de créer un nouveau tarif plutôt que modifier l'existant",
            "Validation que le nouveau prix est positif",
            "Notification aux utilisateurs ayant ajouté l'événement aux favoris",
            "Historique des changements de prix",
            "Interdiction de modification si paiements en cours"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "organizer, event, pricing, backend, frontend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-023",
        "title": "Ajouter des formules/tarifs",
        "user_type": "organisateur",
        "goal": "créer différentes formules de billets (Normal, VIP, Étudiant)",
        "benefit": "proposer plusieurs options tarifaires",
        "criteria": [
            "Bouton \"Ajouter une formule\"",
            "Champs: nom de la formule, description, prix, quantité disponible",
            "Types prédéfinis: Normal, VIP, Étudiant, Groupe, Early Bird",
            "Possibilité de créer des formules personnalisées",
            "Définition des avantages de chaque formule",
            "Ordre d'affichage configurable",
            "Limitation du nombre de formules (max 5)",
            "Sauvegarde et activation des formules"
        ],
        "estimation": "8",
        "priority": "Moyenne",
        "labels": "organizer, event, pricing, backend, frontend",
        "milestone": "Sprint 5 - Avancé"
    },
    {
        "number": "US-024",
        "title": "Supprimer une formule",
        "user_type": "organisateur",
        "goal": "supprimer une formule de billet",
        "benefit": "retirer une option qui n'est plus pertinente",
        "criteria": [
            "Bouton \"Supprimer\" visible sur chaque formule",
            "Confirmation requise avant suppression",
            "Vérification qu'aucun billet de cette formule n'a été vendu",
            "Si billets vendus: désactivation au lieu de suppression",
            "Message d'erreur clair si suppression impossible",
            "Mise à jour immédiate de l'affichage",
            "Archivage de la formule dans l'historique"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "organizer, event, pricing, backend, frontend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-025",
        "title": "Définir un code QR",
        "user_type": "organisateur",
        "goal": "générer automatiquement des codes QR uniques pour chaque billet",
        "benefit": "faciliter la validation à l'entrée de l'événement",
        "criteria": [
            "Génération automatique de QR code lors de la confirmation de réservation",
            "QR code unique et non duplicable pour chaque billet",
            "Encodage des informations: ID réservation, événement, participant",
            "QR code inclus dans le billet PDF envoyé par email",
            "Format lisible par scanner standard",
            "Stockage sécurisé des codes générés",
            "API de validation du QR code pour l'organisateur"
        ],
        "estimation": "5",
        "priority": "Haute",
        "labels": "organizer, booking, qrcode, backend",
        "milestone": "Sprint 3 - Réservation"
    },
    {
        "number": "US-026",
        "title": "Valider les réservations",
        "user_type": "organisateur",
        "goal": "scanner et valider les billets à l'entrée de l'événement",
        "benefit": "contrôler l'accès",
        "criteria": [
            "Interface de scan accessible depuis mobile/tablette",
            "Scan du QR code via caméra de l'appareil",
            "Validation immédiate: billet valide/invalide/déjà utilisé",
            "Feedback visuel et sonore (vert/rouge, son)",
            "Affichage des informations du participant",
            "Marquage du billet comme \"utilisé\" après validation",
            "Mode hors-ligne avec synchronisation ultérieure",
            "Statistiques en temps réel des entrées"
        ],
        "estimation": "8",
        "priority": "Haute",
        "labels": "organizer, booking, validation, frontend, backend",
        "milestone": "Sprint 4 - Gestion"
    },
    {
        "number": "US-027",
        "title": "Gérer les participants",
        "user_type": "organisateur",
        "goal": "voir et gérer la liste des participants à mon événement",
        "benefit": "suivre les inscriptions et communiquer avec eux",
        "criteria": [
            "Liste complète de tous les participants avec réservations confirmées",
            "Affichage: nom, email, nombre de billets, formule, statut paiement",
            "Recherche et filtres (par formule, statut, date d'achat)",
            "Export de la liste en CSV/Excel",
            "Accès aux notes personnelles de chaque participant",
            "Statistiques: nombre total, répartition par formule",
            "Option d'envoi d'email groupé aux participants"
        ],
        "estimation": "8",
        "priority": "Haute",
        "labels": "organizer, event, participants, frontend, backend",
        "milestone": "Sprint 4 - Gestion"
    },
    {
        "number": "US-028",
        "title": "Générer un remboursement",
        "user_type": "organisateur",
        "goal": "initier un remboursement pour un participant",
        "benefit": "gérer les cas exceptionnels ou annulations",
        "criteria": [
            "Accès depuis la liste des participants ou détails de réservation",
            "Sélection du montant à rembourser (partiel ou total)",
            "Motif du remboursement (champ texte obligatoire)",
            "Confirmation requise avant traitement",
            "Traitement du remboursement via la plateforme de paiement",
            "Email automatique au participant",
            "Mise à jour du statut de la réservation",
            "Historique des remboursements effectués"
        ],
        "estimation": "8",
        "priority": "Moyenne",
        "labels": "organizer, payment, refund, backend, frontend",
        "milestone": "Sprint 5 - Avancé"
    },
    {
        "number": "US-029",
        "title": "Envoyer une notification",
        "user_type": "organisateur",
        "goal": "envoyer des notifications par email aux participants",
        "benefit": "communiquer des informations importantes sur l'événement",
        "criteria": [
            "Interface d'envoi de notification dans la gestion de l'événement",
            "Sélection des destinataires (tous, par formule, personnalisé)",
            "Éditeur de texte pour composer le message",
            "Prévisualisation du message avant envoi",
            "Objet et corps personnalisables",
            "Confirmation avant envoi groupé",
            "Historique des notifications envoyées",
            "Statistiques de lecture (si possible)"
        ],
        "estimation": "8",
        "priority": "Moyenne",
        "labels": "organizer, notification, email, backend, frontend",
        "milestone": "Sprint 5 - Avancé"
    },
    {
        "number": "US-030",
        "title": "Voir les analyses de performance",
        "user_type": "organisateur",
        "goal": "consulter les statistiques et analyses de mes événements",
        "benefit": "mesurer leur succès et optimiser mes futures éditions",
        "criteria": [
            "Tableau de bord avec métriques clés: ventes, revenus, participants",
            "Graphiques d'évolution des ventes dans le temps",
            "Taux de remplissage en temps réel",
            "Répartition des ventes par formule/tarif",
            "Comparaison avec les éditions précédentes",
            "Analyses démographiques (si données disponibles)",
            "Export des données en PDF/Excel",
            "Période personnalisable (jour, semaine, mois)"
        ],
        "estimation": "13",
        "priority": "Moyenne",
        "labels": "organizer, analytics, dashboard, frontend, backend",
        "milestone": "Sprint 6 - Analytics & Admin"
    },
    {
        "number": "US-031",
        "title": "Créer une catégorie",
        "user_type": "administrateur",
        "goal": "créer de nouvelles catégories d'événements",
        "benefit": "permettre une meilleure classification des événements",
        "criteria": [
            "Formulaire de création accessible depuis le panneau admin",
            "Champs: nom, description, couleur, icône",
            "Validation de l'unicité du nom",
            "Slug généré automatiquement pour l'URL",
            "Possibilité d'upload d'une icône personnalisée",
            "Aperçu de l'affichage de la catégorie",
            "Statut actif/inactif",
            "Sauvegarde et activation immédiate"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "admin, category, frontend, backend",
        "milestone": "Sprint 1 - Fondations"
    },
    {
        "number": "US-032",
        "title": "Modifier une catégorie",
        "user_type": "administrateur",
        "goal": "modifier les informations d'une catégorie existante",
        "benefit": "corriger ou améliorer la classification",
        "criteria": [
            "Liste de toutes les catégories avec bouton \"Modifier\"",
            "Formulaire pré-rempli avec les informations actuelles",
            "Modification de tous les champs (nom, description, couleur, icône)",
            "Avertissement si la catégorie est utilisée par des événements",
            "Aperçu des modifications",
            "Sauvegarde et mise à jour immédiate",
            "Historique des modifications"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "admin, category, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-033",
        "title": "Supprimer une catégorie",
        "user_type": "administrateur",
        "goal": "supprimer une catégorie qui n'est plus utilisée",
        "benefit": "maintenir une liste propre et pertinente",
        "criteria": [
            "Bouton \"Supprimer\" visible sur chaque catégorie",
            "Vérification qu'aucun événement n'utilise cette catégorie",
            "Si événements liés: impossibilité de supprimer avec message explicatif",
            "Option de réassigner les événements à une autre catégorie avant suppression",
            "Confirmation requise avec avertissement",
            "Suppression définitive de la base de données",
            "Mise à jour immédiate de la liste"
        ],
        "estimation": "5",
        "priority": "Basse",
        "labels": "admin, category, backend, frontend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-034",
        "title": "Voir la liste des organisateurs",
        "user_type": "administrateur",
        "goal": "consulter la liste de tous les organisateurs inscrits",
        "benefit": "superviser et gérer les comptes organisateurs",
        "criteria": [
            "Liste paginée de tous les comptes avec rôle \"ORGANIZER\"",
            "Affichage: nom, email, date d'inscription, statut, nombre d'événements",
            "Recherche par nom ou email",
            "Filtres: statut (actif/inactif), date d'inscription",
            "Tri par colonne (nom, date, nombre d'événements)",
            "Accès aux détails de chaque organisateur",
            "Statistiques globales: total organisateurs, actifs, inactifs"
        ],
        "estimation": "5",
        "priority": "Moyenne",
        "labels": "admin, organizer, frontend, backend",
        "milestone": "Sprint 6 - Analytics & Admin"
    },
    {
        "number": "US-035",
        "title": "Supprimer un organisateur",
        "user_type": "administrateur",
        "goal": "supprimer le compte d'un organisateur",
        "benefit": "retirer l'accès en cas de violation des conditions d'utilisation",
        "criteria": [
            "Bouton \"Supprimer\" accessible depuis la liste ou le profil",
            "Vérification des événements associés à l'organisateur",
            "Avertissement si événements actifs ou futurs existent",
            "Option de transférer les événements à un autre organisateur",
            "Option de suppression ou d'archivage des événements",
            "Confirmation double avec saisie du nom de l'organisateur",
            "Notification par email à l'organisateur supprimé",
            "Anonymisation des données si requis par RGPD"
        ],
        "estimation": "8",
        "priority": "Basse",
        "labels": "admin, organizer, backend, frontend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-036",
        "title": "Accéder à la configuration globale",
        "user_type": "administrateur",
        "goal": "accéder aux paramètres de configuration de la plateforme",
        "benefit": "personnaliser le fonctionnement de EventHub",
        "criteria": [
            "Panneau de configuration accessible uniquement aux admins",
            "Sections: général, paiement, emails, sécurité, apparence",
            "Paramètres modifiables: nom de la plateforme, logo, couleurs",
            "Configuration des emails (SMTP, templates)",
            "Configuration des paiements (clés API, frais)",
            "Paramètres de sécurité (sessions, mots de passe)",
            "Aperçu des modifications avant application",
            "Sauvegarde et application immédiate des changements"
        ],
        "estimation": "13",
        "priority": "Moyenne",
        "labels": "admin, configuration, frontend, backend",
        "milestone": "Sprint 6 - Analytics & Admin"
    },
    {
        "number": "US-037",
        "title": "Voir les analyses globales",
        "user_type": "administrateur",
        "goal": "consulter les analyses globales de la plateforme",
        "benefit": "suivre l'activité et la croissance de EventHub",
        "criteria": [
            "Tableau de bord avec KPIs: utilisateurs, événements, réservations, revenus",
            "Graphiques d'évolution dans le temps",
            "Métriques de croissance (nouveaux utilisateurs, événements créés)",
            "Top événements par ventes",
            "Top organisateurs par activité",
            "Analyse géographique si données disponibles",
            "Taux de conversion (visiteurs -> inscrits -> acheteurs)",
            "Export des données en CSV/PDF",
            "Période personnalisable (semaine, mois, année)"
        ],
        "estimation": "13",
        "priority": "Basse",
        "labels": "admin, analytics, dashboard, frontend, backend",
        "milestone": "Sprint 6 - Analytics & Admin"
    },
    {
        "number": "US-038",
        "title": "Créer un libellé personnalisé",
        "user_type": "administrateur",
        "goal": "créer des libellés (labels/tags) personnalisés",
        "benefit": "catégoriser et organiser les événements de manière flexible",
        "criteria": [
            "Formulaire de création de libellé",
            "Champs: nom, description, couleur",
            "Validation de l'unicité du nom",
            "Choix de la couleur parmi une palette ou saisie manuelle (hex)",
            "Aperçu du libellé",
            "Option de rendre le libellé public (visible par organisateurs)",
            "Sauvegarde et activation",
            "Possibilité d'assigner aux événements ou utilisateurs"
        ],
        "estimation": "5",
        "priority": "Basse",
        "labels": "admin, labels, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-039",
        "title": "Modifier un libellé",
        "user_type": "administrateur",
        "goal": "modifier les informations d'un libellé existant",
        "benefit": "ajuster la classification ou corriger des erreurs",
        "criteria": [
            "Liste de tous les libellés avec bouton \"Modifier\"",
            "Formulaire pré-rempli avec les informations actuelles",
            "Modification du nom, description, couleur",
            "Aperçu des modifications",
            "Affichage du nombre d'éléments utilisant ce libellé",
            "Sauvegarde et mise à jour immédiate",
            "Mise à jour automatique sur tous les éléments associés"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "admin, labels, frontend, backend",
        "milestone": "Sprint 7 - Perfectionnement"
    },
    {
        "number": "US-040",
        "title": "Supprimer un libellé",
        "user_type": "administrateur",
        "goal": "supprimer un libellé qui n'est plus utilisé",
        "benefit": "maintenir une liste organisée",
        "criteria": [
            "Bouton \"Supprimer\" visible sur chaque libellé",
            "Affichage du nombre d'éléments utilisant le libellé",
            "Confirmation requise avant suppression",
            "Si libellé utilisé: retrait automatique de tous les éléments",
            "Option d'annulation",
            "Suppression définitive",
            "Mise à jour immédiate de la liste"
        ],
        "estimation": "3",
        "priority": "Basse",
        "labels": "admin, labels, backend, frontend",
        "milestone": "Sprint 7 - Perfectionnement"
    }
]

# Créer le répertoire si nécessaire
os.makedirs(".github/issue-bodies", exist_ok=True)

# Générer les fichiers
print("🎫 Génération des fichiers de corps d'issues...")
print("=" * 60)

for story in user_stories:
    filename = f".github/issue-bodies/{story['number']}.md"
    
    # Construire le contenu du fichier
    content = f"""## User Story

**En tant que** {story['user_type']}, **je veux** {story['goal']}, **afin de** {story['benefit']}.

## Critères d'acceptation

"""
    
    for criterion in story['criteria']:
        content += f"- [ ] {criterion}\n"
    
    content += f"""
## Informations additionnelles

- **Estimation:** {story['estimation']} points
- **Priorité:** {story['priority']}
- **Milestone:** {story['milestone']}
- **Labels:** {story['labels']}

## Definition of Done

- [ ] Code développé et testé localement
- [ ] Tests unitaires écrits et passants
- [ ] Tests d'intégration si nécessaire
- [ ] Code review effectué
- [ ] Documentation mise à jour
- [ ] Déployé en environnement de développement
- [ ] Validé par le Product Owner

## Notes techniques

_À compléter pendant le développement_

## Dépendances

_Identifier les user stories prérequises_
"""
    
    # Écrire le fichier
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {story['number']}: {story['title']}")

print("=" * 60)
print(f"✅ {len(user_stories)} fichiers de corps d'issues générés dans .github/issue-bodies/")
print("\nPour créer les issues dans GitHub, exécutez:")
print("  chmod +x scripts/create-issues.sh")
print("  ./scripts/create-issues.sh")
