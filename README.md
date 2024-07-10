# 🛡️ DockerShield

DockerShield est un outil d'audit de sécurité avancé pour les conteneurs Docker. Il fournit une analyse complète des images et des conteneurs Docker, détectant les vulnérabilités, les secrets exposés, et les problèmes de configuration.

⚠️ **Note:** Ce projet est actuellement en développement actif. Les fonctionnalités peuvent changer et des bugs peuvent être présents. Vos contributions et retours sont les bienvenus !

## ✨ Caractéristiques

- 🔍 Analyse statique des images Docker
- 🐛 Détection des vulnérabilités connues
- 🔑 Recherche de secrets exposés
- ✅ Vérification de la conformité aux bonnes pratiques
- 🏃‍♂️ Analyse dynamique des conteneurs en cours d'exécution
- 📊 Génération de rapports détaillés

## 🚀 Installation

```bash
git clone https://github.com/jacquesbagui/DockerShield.git
cd DockerShield
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
pip install -r requirements.txt

# Pour une utilisation en tant que package
pip install -e .
```

## 🖥️ Utilisation

Il y a deux façons d'utiliser DockerShield :

1. En développement (utilisant main.py)

```bash
python main.py --image <nom_de_l_image>
```

2. Après installation (en tant que package)

```bash
dockershield --image <nom_de_l_image>
```
Pour spécifier un format de rapport :

```bash
dockershield --image <nom_de_l_image> --report-format json
```

## ⚙️ Configuration

## 🤝 Contribuer

DockerShield est un projet open source et nous accueillons chaleureusement toutes les contributions ! Voici comment vous pouvez participer :

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

Nous sommes particulièrement intéressés par les contributions dans les domaines suivants :
- 🧩 Ajout de nouveaux analyseurs ou scanners
- ⚡ Amélioration des performances
- 🧪 Extension de la couverture des tests
- 📖 Amélioration de la documentation

Avant de soumettre une pull request importante, veuillez d'abord discuter des changements que vous souhaitez apporter en ouvrant une issue.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📞 Contact

Jean Jacques BAGUI - [@jacquesbagui](https://x.com/jacquesbagui) - jacquesbagui@gmail.com

Lien du projet : [https://github.com/jacquesbagui/DockerShield.git](https://github.com/jacquesbagui/DockerShield.git)