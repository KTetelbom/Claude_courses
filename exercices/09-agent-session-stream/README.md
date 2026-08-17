# Exercice 9 — Envoyer une tâche à l'agent et suivre son exécution en direct

Complète l'exercice 8 : une fois l'agent, l'environnement et la session créés,
on envoie une tâche à l'agent (`sessions.events.send`) puis on écoute le flux
d'événements (`sessions.events.stream`) pour afficher sa réponse au fur et à
mesure, ainsi que chaque outil qu'il utilise.

## À propos de la boucle fournie

Votre boucle `for event in stream: ...` était déjà correcte telle quelle —
les noms d'événements (`agent.message`, `agent.tool_use`,
`session.status_idle`) et la structure (`event.content`, `block.type`,
`event.name`) correspondent exactement à l'API du SDK.

Ce qui manquait, c'est tout ce qu'il y a *avant* : recréer l'agent, l'environnement
et la session (comme dans l'exercice 8), puis surtout **envoyer une tâche** à
l'agent avec `client.beta.sessions.events.send(...)` avant de lancer le stream
— sans ça, il n'y a rien à observer et le flux resterait simplement ouvert
sans événements intéressants.

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/09-agent-session-stream/main.py
```

Le script demande à l'agent de créer un fichier `notes.txt` de 5 lignes dans
son environnement cloud, puis d'en compter les lignes. Vous devriez voir
s'afficher en direct : les outils utilisés (`[tool] ...`, écriture de
fichier, lecture, etc.), le texte de la réponse au fur et à mesure qu'elle
est générée, puis `--- Agent done ---` une fois la session revenue au repos.
