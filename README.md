# Echobot

Echobot est un chatbot interactif utilisant Flask pour répondre aux questions des utilisateurs. Lorsque la réponse à une question est disponible dans la base de données locale (fichier `data.json`), Echobot fournit la réponse directement. Si la question n'est pas dans la base de données, Echobot interroge Wikipedia et récupère un résumé, qu'il traduit en français pour l'utilisateur.

## Fonctionnalités

- **Réponses locales** : Si la question est présente dans la base de données (`data.json`), le bot retourne une réponse préconfigurée.
- **Recherche Wikipédia** : Si la question n'est pas dans la base de données, le bot cherche la réponse sur Wikipédia et la traduit en français.
- **Gestion des erreurs** : Le bot gère les erreurs de connexion à Wikipedia et les ambiguïtés des résultats.

## Prérequis

Avant de commencer, vous devez avoir installé Python 3.x et les dépendances suivantes :

- Flask
- Wikipedia
- googletrans==4.0.0-rc1 (pour la traduction)

Vous pouvez installer les dépendances en utilisant pip avec le fichier `requirements.txt`.

### Installation

Clonez ce dépôt et installez les dépendances :

```bash
git clone https://github.com/L-Sauvinet/echobot.git
cd echobot
pip install -r requirements.txt
