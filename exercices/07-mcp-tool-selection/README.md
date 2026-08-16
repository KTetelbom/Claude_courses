# Exercice 7 — Lister puis restreindre les outils d'un serveur MCP

Deux scripts, en deux temps, sur le même serveur MCP public
[DeepWiki](https://mcp.deepwiki.com/mcp) (pas d'authentification requise) :

## Étape 1 — `step1_list_tools.py`

Se connecte au serveur avec **tous** ses outils activés (comportement par
défaut) et demande à Claude de les lister avec leur nom exact. DeepWiki
expose typiquement trois outils : `read_wiki_structure`, `read_wiki_contents`
et `ask_question`.

```
python exercices/07-mcp-tool-selection/step1_list_tools.py
```

## Étape 2 — `step2_select_tools.py`

Réutilise les noms trouvés à l'étape 1 pour n'activer **qu'un sous-ensemble**
des outils du serveur, via deux champs du `mcp_toolset` :

- `default_config: {"enabled": False}` — désactive tous les outils du serveur
  par défaut.
- `configs: {"nom_de_l_outil": {"enabled": True}, ...}` — réactive
  individuellement ceux qu'on veut garder.

Dans cet exemple, seul `ask_question` est réactivé (`read_wiki_structure` et
`read_wiki_contents` restent désactivés) : Claude ne pourra poser une
question directe au wiki d'un dépôt, sans pouvoir explorer sa structure de
fichiers.

```
python exercices/07-mcp-tool-selection/step2_select_tools.py
```

Le script affiche le texte de la réponse, ainsi qu'une ligne `[tool used: ...]`
à chaque fois que Claude appelle un outil MCP — pratique pour vérifier qu'il
n'a bien utilisé que les outils autorisés.

## Pourquoi restreindre les outils ?

Sur un serveur MCP réel (Linear, GitHub, etc.), tous les outils exposés ne
sont pas forcément souhaitables dans un contexte donné : par exemple, donner
accès à un agent en lecture seule au wiki d'un repo sans lui laisser la
possibilité d'appeler des outils d'écriture/suppression si le serveur en
propose. `default_config` + `configs` permet de le faire sans changer le
serveur MCP lui-même.

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```
