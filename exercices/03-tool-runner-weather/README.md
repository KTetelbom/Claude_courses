# Exercice 3 — `toolRunner` avec deux tools (TypeScript)

Même idée que l'exercice 2 (agent qui appelle un outil météo), mais avec le helper
`client.beta.messages.toolRunner()` du SDK, qui gère lui-même la boucle
"Claude demande un tool → on l'exécute → on renvoie le résultat" à notre place.

Deux tools sont fournis : `get_weather` (météo du jour) et `get_forecast`
(prévisions à 3 jours), pour que Claude puisse combiner les deux dans sa réponse.

## Bugs corrigés

- `model: "claude-sonnet-4-6"` n'est pas un ID de modèle valide → remplacé par
  `claude-sonnet-5`.
- Le code original passait des fonctions brutes (`tools: [getWeather, getForecast]`) à
  `toolRunner()`. Ça ne fonctionne pas : `toolRunner()` attend des objets tool créés via
  le helper `betaTool()` (ou `betaZodTool()` si vous préférez décrire le schéma avec Zod),
  qui portent le nom, la description et le JSON schema de l'outil, en plus de la fonction
  à exécuter.
- `runner.untilDone()` n'existe pas dans le SDK → la bonne méthode est
  `runner.runUntilDone()`.

## Installer les dépendances

Depuis la racine du projet :

```
npm install
```

(installe entre autres `tsx`, qui permet d'exécuter du TypeScript directement avec
Node, sans étape de compilation séparée)

## Lancer l'exercice

```
npx tsx --env-file=.env.local exercices/03-tool-runner-weather/index.ts
```
