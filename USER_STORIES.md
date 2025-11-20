# User Stories EventHub - Gestion d'événements et billetterie

Ce document contient les 40 User Stories complètes pour le projet EventHub, organisées selon le diagramme de flux et respectant les critères INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).

## Format
**En tant que** [type d'utilisateur], **je veux** [objectif], **afin de** [bénéfice].

---

## 🔐 USER - Connexion et Authentification

### US-001: Connexion utilisateur
**En tant qu'** utilisateur, **je veux** me connecter avec mon email et mot de passe, **afin de** accéder à mon compte et mes réservations.

**Critères d'acceptation:**
- [ ] Formulaire de connexion avec champs email et mot de passe
- [ ] Validation des champs (email valide, mot de passe non vide)
- [ ] Message d'erreur en cas d'identifiants incorrects
- [ ] Redirection vers le tableau de bord après connexion réussie
- [ ] Option "Se souvenir de moi" pour rester connecté
- [ ] Token JWT généré et stocké en session sécurisée

**Estimation:** 3 points  
**Priorité:** Haute  
**Labels:** `user`, `authentication`, `frontend`, `backend`

---

### US-002: Inscription utilisateur
**En tant que** visiteur, **je veux** créer un compte utilisateur, **afin de** pouvoir réserver des billets et gérer mon profil.

**Critères d'acceptation:**
- [ ] Formulaire d'inscription avec nom, prénom, email, mot de passe
- [ ] Validation de la force du mot de passe (min 8 caractères, majuscule, chiffre)
- [ ] Vérification que l'email n'existe pas déjà
- [ ] Confirmation du mot de passe
- [ ] Acceptation des conditions générales d'utilisation
- [ ] Email de confirmation envoyé après inscription
- [ ] Compte créé avec rôle "USER" par défaut

**Estimation:** 5 points  
**Priorité:** Haute  
**Labels:** `user`, `authentication`, `frontend`, `backend`

---

## 📅 USER - Consultation des Événements

### US-003: Voir les événements disponibles
**En tant qu'** utilisateur, **je veux** consulter la liste de tous les événements disponibles, **afin de** découvrir les événements qui m'intéressent.

**Critères d'acceptation:**
- [ ] Liste paginée des événements actifs (statut: publié)
- [ ] Affichage des informations essentielles: titre, date, lieu, image
- [ ] Carte ou grille responsive adaptée mobile/desktop
- [ ] Tri par défaut: événements à venir en premier
- [ ] Indication de disponibilité des billets
- [ ] Navigation vers le détail de l'événement au clic

**Estimation:** 5 points  
**Priorité:** Haute  
**Labels:** `user`, `event`, `frontend`, `backend`

---

### US-004: Consulter l'historique d'événements
**En tant qu'** utilisateur connecté, **je veux** voir la liste de mes événements passés, **afin de** retrouver mes anciennes réservations et souvenirs.

**Critères d'acceptation:**
- [ ] Accès via le profil utilisateur
- [ ] Liste des événements avec réservations confirmées dans le passé
- [ ] Affichage: nom événement, date, nombre de billets, statut
- [ ] Tri chronologique inverse (plus récent en premier)
- [ ] Option de télécharger les billets passés (PDF)
- [ ] Accès aux détails de chaque réservation

**Estimation:** 3 points  
**Priorité:** Moyenne  
**Labels:** `user`, `event`, `history`, `frontend`, `backend`

---

### US-005: Filtrer les événements par catégorie
**En tant qu'** utilisateur, **je veux** filtrer les événements par catégorie, **afin de** trouver rapidement les événements qui m'intéressent.

**Critères d'acceptation:**
- [ ] Menu de filtres avec toutes les catégories disponibles
- [ ] Possibilité de sélectionner une ou plusieurs catégories
- [ ] Mise à jour dynamique de la liste sans rechargement de page
- [ ] Affichage du nombre de résultats pour chaque catégorie
- [ ] Option pour réinitialiser tous les filtres
- [ ] URL mise à jour pour permettre le partage des filtres

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `user`, `event`, `filter`, `frontend`, `backend`

---

## 🎫 USER - Réservation de Billets

### US-006: Réserver un billet
**En tant qu'** utilisateur connecté, **je veux** réserver un ou plusieurs billets pour un événement, **afin de** participer à cet événement.

**Critères d'acceptation:**
- [ ] Sélection du nombre de billets disponibles
- [ ] Vérification de la disponibilité en temps réel
- [ ] Affichage du prix total calculé automatiquement
- [ ] Choix de la formule/tarif si applicable (normal, VIP, étudiant)
- [ ] Validation que l'utilisateur ne dépasse pas la limite par personne
- [ ] Ajout au panier ou réservation directe
- [ ] Réservation temporaire avec minuteur (ex: 10 min)

**Estimation:** 8 points  
**Priorité:** Haute  
**Labels:** `user`, `booking`, `frontend`, `backend`

---

### US-007: Ajouter une note à la réservation
**En tant qu'** utilisateur, **je veux** ajouter une note ou commentaire à ma réservation, **afin de** communiquer des informations spéciales à l'organisateur.

**Critères d'acceptation:**
- [ ] Champ texte optionnel lors de la réservation
- [ ] Limitation de caractères (ex: 500 caractères)
- [ ] Sauvegarde de la note avec la réservation
- [ ] Visible par l'utilisateur dans les détails de sa réservation
- [ ] Visible par l'organisateur dans la gestion des participants
- [ ] Possibilité de modifier la note avant le paiement

**Estimation:** 2 points  
**Priorité:** Basse  
**Labels:** `user`, `booking`, `frontend`, `backend`

---

### US-008: Confirmer la réservation avant paiement
**En tant qu'** utilisateur, **je veux** voir un récapitulatif de ma réservation avant de payer, **afin de** vérifier que toutes les informations sont correctes.

**Critères d'acceptation:**
- [ ] Page de récapitulatif avec tous les détails: événement, date, billets, prix
- [ ] Affichage des informations personnelles
- [ ] Affichage de la note personnelle si ajoutée
- [ ] Conditions d'annulation et de remboursement visibles
- [ ] Bouton "Modifier" pour retourner à l'étape précédente
- [ ] Bouton "Procéder au paiement" pour continuer
- [ ] Checkbox de confirmation des CGV

**Estimation:** 3 points  
**Priorité:** Haute  
**Labels:** `user`, `booking`, `frontend`

---

### US-009: Payer pour la réservation
**En tant qu'** utilisateur, **je veux** effectuer le paiement de ma réservation de manière sécurisée, **afin de** confirmer définitivement mes billets.

**Critères d'acceptation:**
- [ ] Intégration d'une solution de paiement sécurisée (Stripe/PayPal)
- [ ] Formulaire de paiement avec carte bancaire
- [ ] Validation et chiffrement des données de paiement
- [ ] Gestion des erreurs de paiement avec messages clairs
- [ ] Confirmation immédiate après paiement réussi
- [ ] Email de confirmation avec billets PDF envoyé
- [ ] Génération du QR code unique pour chaque billet
- [ ] Mise à jour du statut de la réservation à "confirmée"

**Estimation:** 13 points  
**Priorité:** Haute  
**Labels:** `user`, `booking`, `payment`, `backend`, `frontend`

---

### US-010: Annuler et obtenir remboursement
**En tant qu'** utilisateur, **je veux** annuler ma réservation et obtenir un remboursement, **afin de** récupérer mon argent si je ne peux pas assister à l'événement.

**Critères d'acceptation:**
- [ ] Bouton d'annulation dans les détails de la réservation
- [ ] Vérification des conditions d'annulation (délai minimum avant événement)
- [ ] Confirmation de l'annulation avec avertissement
- [ ] Calcul automatique du montant du remboursement (selon politique)
- [ ] Traitement du remboursement via la plateforme de paiement
- [ ] Email de confirmation d'annulation et remboursement
- [ ] Mise à jour du statut à "annulée" et "remboursée"
- [ ] Libération des places pour d'autres utilisateurs

**Estimation:** 8 points  
**Priorité:** Moyenne  
**Labels:** `user`, `booking`, `payment`, `refund`, `backend`, `frontend`

---

## 👤 USER - Gestion Profil

### US-011: Modifier son mot de passe
**En tant qu'** utilisateur connecté, **je veux** changer mon mot de passe, **afin de** sécuriser mon compte ou mettre à jour mes identifiants.

**Critères d'acceptation:**
- [ ] Formulaire accessible depuis les paramètres du profil
- [ ] Demande de l'ancien mot de passe pour vérification
- [ ] Deux champs pour le nouveau mot de passe (confirmation)
- [ ] Validation de la force du nouveau mot de passe
- [ ] Message d'erreur si l'ancien mot de passe est incorrect
- [ ] Confirmation de succès après modification
- [ ] Email de notification envoyé pour informer du changement

**Estimation:** 3 points  
**Priorité:** Moyenne  
**Labels:** `user`, `profile`, `security`, `frontend`, `backend`

---

### US-012: Changer les informations de compte
**En tant qu'** utilisateur connecté, **je veux** modifier mes informations personnelles, **afin de** garder mon profil à jour.

**Critères d'acceptation:**
- [ ] Formulaire pré-rempli avec les informations actuelles
- [ ] Modification possible: nom, prénom, email, téléphone, adresse
- [ ] Validation des champs (email valide, format téléphone)
- [ ] Vérification que le nouvel email n'est pas déjà utilisé
- [ ] Confirmation par email si l'email est modifié
- [ ] Sauvegarde immédiate des modifications
- [ ] Message de confirmation de mise à jour

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `user`, `profile`, `frontend`, `backend`

---

### US-013: Ajouter une note personnelle
**En tant qu'** utilisateur connecté, **je veux** ajouter des notes personnelles à mes événements favoris, **afin de** me rappeler pourquoi je m'intéresse à cet événement.

**Critères d'acceptation:**
- [ ] Option "Ajouter une note" visible sur la page de détail de l'événement
- [ ] Zone de texte pour saisir la note (limite: 1000 caractères)
- [ ] Sauvegarde automatique ou bouton de sauvegarde
- [ ] Affichage de la note lors des consultations futures
- [ ] Note privée, visible uniquement par l'utilisateur
- [ ] Horodatage de création de la note

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `user`, `profile`, `notes`, `frontend`, `backend`

---

### US-014: Modifier une note personnelle
**En tant qu'** utilisateur connecté, **je veux** modifier ou supprimer mes notes personnelles, **afin de** mettre à jour mes réflexions sur un événement.

**Critères d'acceptation:**
- [ ] Bouton "Modifier" visible sur les notes existantes
- [ ] Zone de texte éditable avec le contenu actuel
- [ ] Bouton "Enregistrer" pour sauvegarder les modifications
- [ ] Bouton "Supprimer" pour effacer la note
- [ ] Confirmation avant suppression
- [ ] Horodatage de dernière modification
- [ ] Annulation possible avant sauvegarde

**Estimation:** 2 points  
**Priorité:** Basse  
**Labels:** `user`, `profile`, `notes`, `frontend`, `backend`

---

## 🎭 ORGANIZER - Création d'Événements

### US-015: Créer un nouvel événement
**En tant qu'** organisateur, **je veux** créer un nouvel événement, **afin de** promouvoir et vendre des billets pour mon événement.

**Critères d'acceptation:**
- [ ] Formulaire de création accessible depuis le tableau de bord organisateur
- [ ] Champs obligatoires: titre, description courte
- [ ] Workflow guidé en plusieurs étapes (wizard)
- [ ] Sauvegarde automatique en brouillon
- [ ] Validation des champs à chaque étape
- [ ] Création de l'événement avec statut "brouillon"
- [ ] Redirection vers l'édition des détails après création

**Estimation:** 5 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `frontend`, `backend`

---

### US-016: Définir les détails de l'événement
**En tant qu'** organisateur, **je veux** renseigner tous les détails de mon événement, **afin de** fournir toutes les informations nécessaires aux participants.

**Critères d'acceptation:**
- [ ] Champs: titre, description complète, date/heure début et fin
- [ ] Champs: lieu (adresse complète), capacité maximale
- [ ] Upload d'image principale (bannière)
- [ ] Upload de galerie d'images additionnelles (max 5)
- [ ] Éditeur de texte riche pour la description
- [ ] Aperçu en temps réel de l'affichage public
- [ ] Validation de la cohérence des dates (fin après début)
- [ ] Sauvegarde des modifications

**Estimation:** 8 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `frontend`, `backend`

---

### US-017: Définir une catégorie
**En tant qu'** organisateur, **je veux** assigner une ou plusieurs catégories à mon événement, **afin de** permettre aux utilisateurs de le trouver facilement.

**Critères d'acceptation:**
- [ ] Liste déroulante des catégories disponibles
- [ ] Possibilité de sélectionner une catégorie principale
- [ ] Possibilité d'ajouter des catégories secondaires (max 3)
- [ ] Affichage des catégories sous forme de tags
- [ ] Catégories gérées par les administrateurs
- [ ] Sauvegarde de la sélection

**Estimation:** 3 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `category`, `frontend`, `backend`

---

### US-018: Définir les informations de l'édition
**En tant qu'** organisateur, **je veux** préciser les informations spécifiques à cette édition de l'événement, **afin de** distinguer les différentes occurrences d'un événement récurrent.

**Critères d'acceptation:**
- [ ] Champ numéro d'édition (ex: "5ème édition")
- [ ] Champ année
- [ ] Champ thème de l'édition (optionnel)
- [ ] Référence à l'événement parent si récurrent
- [ ] Historique des éditions précédentes visible
- [ ] Lien vers les éditions passées si applicable

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `organizer`, `event`, `frontend`, `backend`

---

### US-019: Changer le statut de l'événement
**En tant qu'** organisateur, **je veux** modifier le statut de mon événement (brouillon, publié, annulé, terminé), **afin de** contrôler sa visibilité et sa disponibilité.

**Critères d'acceptation:**
- [ ] Statuts disponibles: brouillon, publié, annulé, terminé
- [ ] Menu déroulant pour changer le statut
- [ ] Confirmation requise pour passage en "publié"
- [ ] Validation que tous les champs requis sont remplis avant publication
- [ ] Notification automatique aux utilisateurs intéressés lors de la publication
- [ ] Email aux participants en cas d'annulation
- [ ] Historique des changements de statut avec horodatage

**Estimation:** 5 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `status`, `backend`, `frontend`

---

### US-020: Modifier les informations de l'événement
**En tant qu'** organisateur, **je veux** modifier les informations d'un événement existant, **afin de** corriger des erreurs ou mettre à jour les détails.

**Critères d'acceptation:**
- [ ] Accès au formulaire d'édition depuis le tableau de bord
- [ ] Tous les champs modifiables (sauf ID et dates de création)
- [ ] Aperçu des modifications avant sauvegarde
- [ ] Notification automatique aux participants si modifications majeures (date, lieu)
- [ ] Historique des modifications avec auteur et horodatage
- [ ] Restrictions sur certaines modifications si billets vendus
- [ ] Sauvegarde des modifications

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `event`, `frontend`, `backend`

---

### US-021: Définir un prix
**En tant qu'** organisateur, **je veux** définir le prix des billets pour mon événement, **afin de** générer des revenus.

**Critères d'acceptation:**
- [ ] Champ prix avec validation (nombre positif, 2 décimales max)
- [ ] Sélection de la devise (EUR par défaut)
- [ ] Option "Événement gratuit" (prix = 0)
- [ ] Prix minimum configurable
- [ ] Affichage du prix TTC et HT si applicable
- [ ] Calcul des frais de service visible
- [ ] Sauvegarde du prix

**Estimation:** 3 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `pricing`, `backend`, `frontend`

---

### US-022: Modifier le prix
**En tant qu'** organisateur, **je veux** modifier le prix des billets, **afin de** ajuster ma stratégie tarifaire.

**Critères d'acceptation:**
- [ ] Formulaire de modification du prix accessible
- [ ] Avertissement si des billets ont déjà été vendus
- [ ] Option de créer un nouveau tarif plutôt que modifier l'existant
- [ ] Validation que le nouveau prix est positif
- [ ] Notification aux utilisateurs ayant ajouté l'événement aux favoris
- [ ] Historique des changements de prix
- [ ] Interdiction de modification si paiements en cours

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `event`, `pricing`, `backend`, `frontend`

---

### US-023: Ajouter des formules/tarifs
**En tant qu'** organisateur, **je veux** créer différentes formules de billets (Normal, VIP, Étudiant), **afin de** proposer plusieurs options tarifaires.

**Critères d'acceptation:**
- [ ] Bouton "Ajouter une formule"
- [ ] Champs: nom de la formule, description, prix, quantité disponible
- [ ] Types prédéfinis: Normal, VIP, Étudiant, Groupe, Early Bird
- [ ] Possibilité de créer des formules personnalisées
- [ ] Définition des avantages de chaque formule
- [ ] Ordre d'affichage configurable
- [ ] Limitation du nombre de formules (max 5)
- [ ] Sauvegarde et activation des formules

**Estimation:** 8 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `event`, `pricing`, `backend`, `frontend`

---

### US-024: Supprimer une formule
**En tant qu'** organisateur, **je veux** supprimer une formule de billet, **afin de** retirer une option qui n'est plus pertinente.

**Critères d'acceptation:**
- [ ] Bouton "Supprimer" visible sur chaque formule
- [ ] Confirmation requise avant suppression
- [ ] Vérification qu'aucun billet de cette formule n'a été vendu
- [ ] Si billets vendus: désactivation au lieu de suppression
- [ ] Message d'erreur clair si suppression impossible
- [ ] Mise à jour immédiate de l'affichage
- [ ] Archivage de la formule dans l'historique

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `organizer`, `event`, `pricing`, `backend`, `frontend`

---

### US-025: Définir un code QR
**En tant qu'** organisateur, **je veux** générer automatiquement des codes QR uniques pour chaque billet, **afin de** faciliter la validation à l'entrée de l'événement.

**Critères d'acceptation:**
- [ ] Génération automatique de QR code lors de la confirmation de réservation
- [ ] QR code unique et non duplicable pour chaque billet
- [ ] Encodage des informations: ID réservation, événement, participant
- [ ] QR code inclus dans le billet PDF envoyé par email
- [ ] Format lisible par scanner standard
- [ ] Stockage sécurisé des codes générés
- [ ] API de validation du QR code pour l'organisateur

**Estimation:** 5 points  
**Priorité:** Haute  
**Labels:** `organizer`, `booking`, `qrcode`, `backend`

---

### US-026: Valider les réservations
**En tant qu'** organisateur, **je veux** scanner et valider les billets à l'entrée de l'événement, **afin de** contrôler l'accès.

**Critères d'acceptation:**
- [ ] Interface de scan accessible depuis mobile/tablette
- [ ] Scan du QR code via caméra de l'appareil
- [ ] Validation immédiate: billet valide/invalide/déjà utilisé
- [ ] Feedback visuel et sonore (vert/rouge, son)
- [ ] Affichage des informations du participant
- [ ] Marquage du billet comme "utilisé" après validation
- [ ] Mode hors-ligne avec synchronisation ultérieure
- [ ] Statistiques en temps réel des entrées

**Estimation:** 8 points  
**Priorité:** Haute  
**Labels:** `organizer`, `booking`, `validation`, `frontend`, `backend`

---

### US-027: Gérer les participants
**En tant qu'** organisateur, **je veux** voir et gérer la liste des participants à mon événement, **afin de** suivre les inscriptions et communiquer avec eux.

**Critères d'acceptation:**
- [ ] Liste complète de tous les participants avec réservations confirmées
- [ ] Affichage: nom, email, nombre de billets, formule, statut paiement
- [ ] Recherche et filtres (par formule, statut, date d'achat)
- [ ] Export de la liste en CSV/Excel
- [ ] Accès aux notes personnelles de chaque participant
- [ ] Statistiques: nombre total, répartition par formule
- [ ] Option d'envoi d'email groupé aux participants

**Estimation:** 8 points  
**Priorité:** Haute  
**Labels:** `organizer`, `event`, `participants`, `frontend`, `backend`

---

### US-028: Générer un remboursement
**En tant qu'** organisateur, **je veux** initier un remboursement pour un participant, **afin de** gérer les cas exceptionnels ou annulations.

**Critères d'acceptation:**
- [ ] Accès depuis la liste des participants ou détails de réservation
- [ ] Sélection du montant à rembourser (partiel ou total)
- [ ] Motif du remboursement (champ texte obligatoire)
- [ ] Confirmation requise avant traitement
- [ ] Traitement du remboursement via la plateforme de paiement
- [ ] Email automatique au participant
- [ ] Mise à jour du statut de la réservation
- [ ] Historique des remboursements effectués

**Estimation:** 8 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `payment`, `refund`, `backend`, `frontend`

---

### US-029: Envoyer une notification
**En tant qu'** organisateur, **je veux** envoyer des notifications par email aux participants, **afin de** communiquer des informations importantes sur l'événement.

**Critères d'acceptation:**
- [ ] Interface d'envoi de notification dans la gestion de l'événement
- [ ] Sélection des destinataires (tous, par formule, personnalisé)
- [ ] Éditeur de texte pour composer le message
- [ ] Prévisualisation du message avant envoi
- [ ] Objet et corps personnalisables
- [ ] Confirmation avant envoi groupé
- [ ] Historique des notifications envoyées
- [ ] Statistiques de lecture (si possible)

**Estimation:** 8 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `notification`, `email`, `backend`, `frontend`

---

## 📊 ORGANIZER - Analyses

### US-030: Voir les analyses de performance
**En tant qu'** organisateur, **je veux** consulter les statistiques et analyses de mes événements, **afin de** mesurer leur succès et optimiser mes futures éditions.

**Critères d'acceptation:**
- [ ] Tableau de bord avec métriques clés: ventes, revenus, participants
- [ ] Graphiques d'évolution des ventes dans le temps
- [ ] Taux de remplissage en temps réel
- [ ] Répartition des ventes par formule/tarif
- [ ] Comparaison avec les éditions précédentes
- [ ] Analyses démographiques (si données disponibles)
- [ ] Export des données en PDF/Excel
- [ ] Période personnalisable (jour, semaine, mois)

**Estimation:** 13 points  
**Priorité:** Moyenne  
**Labels:** `organizer`, `analytics`, `dashboard`, `frontend`, `backend`

---

## 🏷️ ADMIN - Catégories

### US-031: Créer une catégorie
**En tant qu'** administrateur, **je veux** créer de nouvelles catégories d'événements, **afin de** permettre une meilleure classification des événements.

**Critères d'acceptation:**
- [ ] Formulaire de création accessible depuis le panneau admin
- [ ] Champs: nom, description, couleur, icône
- [ ] Validation de l'unicité du nom
- [ ] Slug généré automatiquement pour l'URL
- [ ] Possibilité d'upload d'une icône personnalisée
- [ ] Aperçu de l'affichage de la catégorie
- [ ] Statut actif/inactif
- [ ] Sauvegarde et activation immédiate

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `admin`, `category`, `frontend`, `backend`

---

### US-032: Modifier une catégorie
**En tant qu'** administrateur, **je veux** modifier les informations d'une catégorie existante, **afin de** corriger ou améliorer la classification.

**Critères d'acceptation:**
- [ ] Liste de toutes les catégories avec bouton "Modifier"
- [ ] Formulaire pré-rempli avec les informations actuelles
- [ ] Modification de tous les champs (nom, description, couleur, icône)
- [ ] Avertissement si la catégorie est utilisée par des événements
- [ ] Aperçu des modifications
- [ ] Sauvegarde et mise à jour immédiate
- [ ] Historique des modifications

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `admin`, `category`, `frontend`, `backend`

---

### US-033: Supprimer une catégorie
**En tant qu'** administrateur, **je veux** supprimer une catégorie qui n'est plus utilisée, **afin de** maintenir une liste propre et pertinente.

**Critères d'acceptation:**
- [ ] Bouton "Supprimer" visible sur chaque catégorie
- [ ] Vérification qu'aucun événement n'utilise cette catégorie
- [ ] Si événements liés: impossibilité de supprimer avec message explicatif
- [ ] Option de réassigner les événements à une autre catégorie avant suppression
- [ ] Confirmation requise avec avertissement
- [ ] Suppression définitive de la base de données
- [ ] Mise à jour immédiate de la liste

**Estimation:** 5 points  
**Priorité:** Basse  
**Labels:** `admin`, `category`, `backend`, `frontend`

---

## 👥 ADMIN - Organisateurs

### US-034: Voir la liste des organisateurs
**En tant qu'** administrateur, **je veux** consulter la liste de tous les organisateurs inscrits, **afin de** superviser et gérer les comptes organisateurs.

**Critères d'acceptation:**
- [ ] Liste paginée de tous les comptes avec rôle "ORGANIZER"
- [ ] Affichage: nom, email, date d'inscription, statut, nombre d'événements
- [ ] Recherche par nom ou email
- [ ] Filtres: statut (actif/inactif), date d'inscription
- [ ] Tri par colonne (nom, date, nombre d'événements)
- [ ] Accès aux détails de chaque organisateur
- [ ] Statistiques globales: total organisateurs, actifs, inactifs

**Estimation:** 5 points  
**Priorité:** Moyenne  
**Labels:** `admin`, `organizer`, `frontend`, `backend`

---

### US-035: Supprimer un organisateur
**En tant qu'** administrateur, **je veux** supprimer le compte d'un organisateur, **afin de** retirer l'accès en cas de violation des conditions d'utilisation.

**Critères d'acceptation:**
- [ ] Bouton "Supprimer" accessible depuis la liste ou le profil
- [ ] Vérification des événements associés à l'organisateur
- [ ] Avertissement si événements actifs ou futurs existent
- [ ] Option de transférer les événements à un autre organisateur
- [ ] Option de suppression ou d'archivage des événements
- [ ] Confirmation double avec saisie du nom de l'organisateur
- [ ] Notification par email à l'organisateur supprimé
- [ ] Anonymisation des données si requis par RGPD

**Estimation:** 8 points  
**Priorité:** Basse  
**Labels:** `admin`, `organizer`, `backend`, `frontend`

---

## ⚙️ ADMIN - Configuration

### US-036: Accéder à la configuration globale
**En tant qu'** administrateur, **je veux** accéder aux paramètres de configuration de la plateforme, **afin de** personnaliser le fonctionnement de EventHub.

**Critères d'acceptation:**
- [ ] Panneau de configuration accessible uniquement aux admins
- [ ] Sections: général, paiement, emails, sécurité, apparence
- [ ] Paramètres modifiables: nom de la plateforme, logo, couleurs
- [ ] Configuration des emails (SMTP, templates)
- [ ] Configuration des paiements (clés API, frais)
- [ ] Paramètres de sécurité (sessions, mots de passe)
- [ ] Aperçu des modifications avant application
- [ ] Sauvegarde et application immédiate des changements

**Estimation:** 13 points  
**Priorité:** Moyenne  
**Labels:** `admin`, `configuration`, `frontend`, `backend`

---

### US-037: Voir les analyses globales
**En tant qu'** administrateur, **je veux** consulter les analyses globales de la plateforme, **afin de** suivre l'activité et la croissance de EventHub.

**Critères d'acceptation:**
- [ ] Tableau de bord avec KPIs: utilisateurs, événements, réservations, revenus
- [ ] Graphiques d'évolution dans le temps
- [ ] Métriques de croissance (nouveaux utilisateurs, événements créés)
- [ ] Top événements par ventes
- [ ] Top organisateurs par activité
- [ ] Analyse géographique si données disponibles
- [ ] Taux de conversion (visiteurs -> inscrits -> acheteurs)
- [ ] Export des données en CSV/PDF
- [ ] Période personnalisable (semaine, mois, année)

**Estimation:** 13 points  
**Priorité:** Basse  
**Labels:** `admin`, `analytics`, `dashboard`, `frontend`, `backend`

---

### US-038: Créer un libellé personnalisé
**En tant qu'** administrateur, **je veux** créer des libellés (labels/tags) personnalisés, **afin de** catégoriser et organiser les événements de manière flexible.

**Critères d'acceptation:**
- [ ] Formulaire de création de libellé
- [ ] Champs: nom, description, couleur
- [ ] Validation de l'unicité du nom
- [ ] Choix de la couleur parmi une palette ou saisie manuelle (hex)
- [ ] Aperçu du libellé
- [ ] Option de rendre le libellé public (visible par organisateurs)
- [ ] Sauvegarde et activation
- [ ] Possibilité d'assigner aux événements ou utilisateurs

**Estimation:** 5 points  
**Priorité:** Basse  
**Labels:** `admin`, `labels`, `frontend`, `backend`

---

### US-039: Modifier un libellé
**En tant qu'** administrateur, **je veux** modifier les informations d'un libellé existant, **afin de** ajuster la classification ou corriger des erreurs.

**Critères d'acceptation:**
- [ ] Liste de tous les libellés avec bouton "Modifier"
- [ ] Formulaire pré-rempli avec les informations actuelles
- [ ] Modification du nom, description, couleur
- [ ] Aperçu des modifications
- [ ] Affichage du nombre d'éléments utilisant ce libellé
- [ ] Sauvegarde et mise à jour immédiate
- [ ] Mise à jour automatique sur tous les éléments associés

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `admin`, `labels`, `frontend`, `backend`

---

### US-040: Supprimer un libellé
**En tant qu'** administrateur, **je veux** supprimer un libellé qui n'est plus utilisé, **afin de** maintenir une liste organisée.

**Critères d'acceptation:**
- [ ] Bouton "Supprimer" visible sur chaque libellé
- [ ] Affichage du nombre d'éléments utilisant le libellé
- [ ] Confirmation requise avant suppression
- [ ] Si libellé utilisé: retrait automatique de tous les éléments
- [ ] Option d'annulation
- [ ] Suppression définitive
- [ ] Mise à jour immédiate de la liste

**Estimation:** 3 points  
**Priorité:** Basse  
**Labels:** `admin`, `labels`, `backend`, `frontend`

---

## 📋 Résumé des estimations

| Catégorie | Nombre de US | Points totaux | Priorité haute |
|-----------|--------------|---------------|----------------|
| USER - Authentification | 2 | 8 | 2 |
| USER - Consultation | 3 | 13 | 1 |
| USER - Réservation | 5 | 36 | 3 |
| USER - Profil | 4 | 13 | 0 |
| ORGANIZER - Création | 15 | 94 | 6 |
| ORGANIZER - Analyses | 1 | 13 | 0 |
| ADMIN - Catégories | 3 | 13 | 0 |
| ADMIN - Organisateurs | 2 | 13 | 0 |
| ADMIN - Configuration | 4 | 37 | 0 |
| **TOTAL** | **40** | **240** | **12** |

## 🎯 Ordre de développement recommandé

1. **Sprint 1 - Fondations (US-001, US-002, US-015, US-031)**
   - Authentification de base
   - Création d'événements simple
   - Système de catégories

2. **Sprint 2 - Consultation et Découverte (US-003, US-005, US-016, US-017)**
   - Liste et filtres d'événements
   - Détails complets des événements

3. **Sprint 3 - Réservation (US-006, US-008, US-009, US-021, US-025)**
   - Système de réservation
   - Paiement
   - Génération QR codes

4. **Sprint 4 - Gestion (US-019, US-020, US-026, US-027)**
   - Gestion des événements
   - Validation des billets
   - Gestion des participants

5. **Sprint 5 - Avancé (US-010, US-023, US-028, US-029)**
   - Remboursements
   - Formules multiples
   - Notifications

6. **Sprint 6 - Analytics & Admin (US-030, US-034, US-036, US-037)**
   - Tableaux de bord
   - Administration

7. **Sprint 7 - Perfectionnement (toutes les US restantes)**
   - Profil utilisateur
   - Fonctionnalités secondaires
