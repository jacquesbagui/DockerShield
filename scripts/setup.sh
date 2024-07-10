#!/bin/bash

# Création de l'environnement virtuel
python -m venv venv

# Activation de l'environnement virtuel
source venv/bin/activate

# Installation des dépendances de développement
pip install -r requirements-dev.txt

# Installation de DockerShield en mode développement
pip install -e .

# Création des répertoires nécessaires
mkdir -p reports
mkdir -p logs

echo "Configuration terminée. L'environnement de développement DockerShield est prêt."
echo "N'oubliez pas d'activer l'environnement virtuel avec 'source venv/bin/activate' avant de travailler sur le projet."