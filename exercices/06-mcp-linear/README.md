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

## Deux versions

- **`main.py`** — la version Linear telle que fournie, qui nécessite un
  compte Linear et un token (voir plus bas).
- **`main_deepwiki.py`** — une version qui utilise
  [DeepWiki](https://docs.devin.ai/work-with-devin/deepwiki-mcp), un serveur
  MCP public qui ne demande **aucune authentification** (pas de
  `authorization_token`). Pratique pour tester le mécanisme `mcp_servers` /
  `mcp_toolset` sans avoir de compte nulle part.

### Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

### Lancer la version sans compte (recommandé si vous n'avez pas Linear)

```
python exercices/06-mcp-linear/main_deepwiki.py
```

Le script demande à Claude quels outils il a à disposition et ce que fait le
dépôt `anthropics/anthropic-sdk-python` — Claude va interroger le serveur MCP
DeepWiki pour répondre, sans configuration supplémentaire de votre part.

### Obtenir un token Linear MCP (pour lancer `main.py`)

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

```
python exercices/06-mcp-linear/main.py
```
