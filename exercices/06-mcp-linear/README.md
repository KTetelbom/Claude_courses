# Exercice 6 — Se connecter à un serveur MCP (Linear)

Connecte Claude à un serveur MCP distant (ici [Linear](https://linear.app)) via
`mcp_servers`, et lui donne accès à tous les outils exposés par ce serveur via
`tools: [{"type": "mcp_toolset", "mcp_server_name": "linear"}]`.

## Bug corrigé

Rien ne chargeait `.env.local` dans l'extrait fourni : `os.environ["LINEAR_MCP_TOKEN"]`
aurait levé une `KeyError` (variable introuvable), et `anthropic.Anthropic()` n'aurait
pas non plus trouvé `ANTHROPIC_API_KEY`. Ajouté `load_dotenv(...)` comme dans les
exercices précédents.

Le reste (`mcp_servers`, `tools`, `betas`) est déjà correct par rapport à l'API du SDK.

## Obtenir un token Linear MCP

1. Connectez-vous à Linear.
2. Allez dans **Settings → API → MCP** (ou **Settings → Security & access**
   selon votre plan) et créez un token d'accès pour le serveur MCP
   (`https://mcp.linear.app/mcp`).
3. Ajoutez-le dans `.env.local` à la racine du projet, sur une nouvelle ligne :
   ```
   LINEAR_MCP_TOKEN=votre_token_ici
   ```
   (ce fichier n'est pas versionné, comme `ANTHROPIC_API_KEY` — voir la mise en
   place initiale du projet)

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/06-mcp-linear/main.py
```

Le script affiche la réponse complète de Claude, qui doit lister les outils
Linear disponibles via le serveur MCP (créer un ticket, chercher des issues,
etc., selon ce que Linear expose).
