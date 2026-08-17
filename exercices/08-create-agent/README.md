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
