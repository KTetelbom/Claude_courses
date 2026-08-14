# Exercice 1 — Revue de code automatisée

Envoie un extrait de code à Claude et affiche sa revue en une réponse texte.

## Bug corrigé

Le modèle demandé était `"Claude Haiku 4.5"` (nom marketing), qui n'est pas un ID de modèle
valide pour l'API. L'ID technique correct est `claude-haiku-4-5-20251001`.

## Lancer l'exercice

Depuis la racine du projet, avec `.env.local` rempli :

```
node --env-file=.env.local exercices/01-code-review/index.mjs
```
