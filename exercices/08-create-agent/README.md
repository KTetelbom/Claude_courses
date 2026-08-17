# Exercice 8 — Créer un agent manégé

Crée un [Managed Agent](https://docs.claude.com/en/docs/agents-and-tools/agents)
("Line Counter") équipé du toolset intégré `agent_toolset_20260401` (lecture/
écriture de fichiers, recherche, etc. — l'agent a accès à un vrai bac à sable
de fichiers), pour effectuer de petites tâches sur des fichiers.

## Bugs corrigés

- `mport anthropic` → faute de frappe, il manquait le `i` : `import anthropic`.
- `model="claude-opus-4-8"` n'est pas un ID de modèle valide → remplacé par
  `claude-opus-5`.
- Il manquait le header beta requis pour l'API Agents (encore en beta) :
  ajouté `betas=["managed-agents-2026-04-01"]`.
- Rien ne chargeait `.env.local` pour `ANTHROPIC_API_KEY` → ajouté
  `load_dotenv(...)` comme dans les exercices précédents.
- Le résultat n'était pas affiché → ajouté `print(agent.id)`, pour pouvoir
  réutiliser l'agent dans un futur appel.

Le reste (`tools`, `default_config`) était déjà correct par rapport à l'API du SDK.

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/08-create-agent/main.py
```

Le script affiche l'ID de l'agent créé (`agent_...`) — notez-le, il servira à
lui envoyer des tâches dans un prochain exercice.

## Créer l'environnement (`create_environment.py`)

Un agent manégé s'exécute dans un **environnement** (bac à sable cloud isolé).
`create_environment.py` en crée un avec un accès réseau non restreint.

Votre extrait de code était en fait déjà correct tel quel par rapport à l'API
du SDK — j'ai seulement ajouté le chargement de `.env.local` et l'affichage
de l'ID créé, comme pour `main.py`. Notez que, contrairement aux autres appels
beta vus jusqu'ici, `environments.create()` n'a pas besoin qu'on lui passe
`betas=[...]` explicitement : le SDK ajoute automatiquement le header
`managed-agents-2026-04-01` pour cet endpoint.

```
python exercices/08-create-agent/create_environment.py
```

Le script affiche l'ID de l'environnement créé (`env_...`) — il servira à
démarrer une session pour l'agent dans un prochain exercice
(`client.beta.sessions.create(agent=..., environment_id=...)`).
