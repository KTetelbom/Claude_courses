# Exercice 4 — Créer un Skill (générateur de rapport de statut)

Crée un [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
via l'API : un dossier contenant un `SKILL.md` (instructions + métadonnées) est
envoyé à Anthropic, qui renvoie un `skill.id` réutilisable dans de futures requêtes
(`messages.create(..., tools=[{"type": "skill", "skill_id": skill.id, ...}])`).

## Bugs corrigés / éléments manquants

- `files_from_dir` n'est pas une fonction magique disponible partout : c'est un
  helper du SDK, à importer explicitement avec
  `from anthropic.lib import files_from_dir`.
- L'appel à `client.beta.skills.create(...)` nécessite le header beta
  `skills-2025-10-02` (API encore en beta) → ajouté via `betas=["skills-2025-10-02"]`.
- Le dossier `status-report-skill/` était référencé mais vide dans l'extrait fourni :
  j'ai créé son `SKILL.md` avec un `name`, une `description` (qui dit à Claude
  *quand* utiliser ce skill) et des instructions pour transformer des notes de
  projet en rapport de statut structuré (Done / In progress / Blockers / Next
  steps).
- L'API impose que le **nom du dossier corresponde exactement au champ `name`**
  du `SKILL.md`. Le dossier a donc été renommé en `status-report-generator/`
  pour matcher `name: status-report-generator`.

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/04-skills-status-report/create_skill.py
```

Le script affiche l'ID du skill créé (`skill_...`) — notez-le, il servira à
l'invoquer dans un futur appel à `messages.create()`.
