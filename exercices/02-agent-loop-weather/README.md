# Exercice 2 — Boucle d'agent avec un tool (météo)

Boucle d'agent minimale : Claude peut appeler un outil `get_weather` (simulé en dur)
pour répondre à une question qui nécessite une information externe.

## Bug corrigé

Le modèle demandé était `"claude-sonnet-4-6"`, qui n'est pas un ID de modèle valide.
Remplacé par `claude-sonnet-5`.

## Installer les dépendances Python

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/02-agent-loop-weather/main.py
```

Le script charge automatiquement la clé depuis `.env.local` à la racine du projet
(via `python-dotenv`), inutile de définir la variable d'environnement manuellement.
