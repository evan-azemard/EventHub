// Configuration de commitlint pour valider les messages de commit
module.exports = {
  // Étend la configuration conventionnelle standard (Conventional Commits)
  // Cette config de base impose le format : type(scope): description
  extends: ['@commitlint/config-conventional'],
  
  // Règles personnalisées qui surchargent ou complètent la config de base
  rules: {
    // Règle 'type-enum' : définit les types de commit autorisés
    'type-enum': [
      2,        // 1) Niveau d'erreur : 0 = désactivé, 1 = warning, 2 = erreur (bloque)
      'always', // 2) Quand appliquer : 'always' = toujours, 'never' = jamais
      [         // 3) Valeurs autorisées pour le type
        'feat',     // Nouvelle fonctionnalité
        'fix',      // Correction de bug
        'docs',     // Documentation
        'style',    // Formatage du code (sans impact fonctionnel)
        'refactor', // Refactorisation du code
        'test',     // Ajout ou modification de tests
        'chore',    // Tâches de maintenance (dépendances, config)
        'perf',     // Amélioration des performances
        'ci',       // CI/CD (GitHub Actions, etc.)
        'build',    // Système de build (webpack, vite, etc.)
        'revert',   // Annulation d'un commit précédent
      ],
    ],
  },
};
