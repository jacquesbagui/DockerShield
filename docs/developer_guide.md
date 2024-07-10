# Guide du développeur DockerShield

## Structure du projet

- `src/`: Contient le code source principal
  - `analyzers/`: Modules d'analyse d'images Docker
  - `scanners/`: Modules de scan pour différents types de problèmes
  - `reporters/`: Modules de génération de rapports
  - `utils/`: Fonctions utilitaires
- `tests/`: Tests unitaires et d'intégration
- `config/`: Fichiers de configuration
- `data/`: Données statiques (signatures, règles, etc.)
- `scripts/`: Scripts utilitaires
- `docs/`: Documentation

## Ajout d'un nouveau module

1. Créez un nouveau fichier dans le dossier approprié (par exemple, `src/analyzers/new_analyzer.py`)
2. Implémentez la classe en héritant de la classe de base appropriée
3. Ajoutez des tests unitaires dans `tests/`
4. Mettez à jour la configuration dans `config/default_config.yaml` si nécessaire
5. Documentez le nouveau module dans ce guide du développeur

## Exécution des tests

```bash
pytest tests/
```

## Bonnes pratiques de codage

- Suivez les conventions PEP 8
- Écrivez des docstrings pour toutes les classes et fonctions publiques
- Maintenez une couverture de test d'au moins 80%
- Utilisez le typage statique (annotations de type)

## Processus de contribution

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Créez une Pull Request