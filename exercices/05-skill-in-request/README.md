# Exercice 5 — Attacher le skill à une requête

Utilise le skill créé à l'exercice 4 (`status-report-generator`) dans un vrai appel
à `messages.create()` : Claude charge le skill dans un container avec accès à
l'exécution de code, puis génère un rapport de statut à partir d'un journal
d'activité brut.

## Bugs corrigés / éléments manquants

- `model="claude-sonnet-5,` — guillemet de fermeture manquant, ce qui est une
  erreur de syntaxe Python (le fichier ne s'exécute même pas). Corrigé en
  `model="claude-sonnet-5"`.
- `skill` et `activity_log` étaient utilisés dans l'extrait sans être définis.
  - `activity_log` : ajouté un exemple de journal d'activité brut (plusieurs
    lignes horodatées).
  - `skill` : le script récupère maintenant le skill créé à l'exercice 4 s'il
    existe déjà (`client.beta.skills.list()`), sinon le crée à la volée — pour
    ne pas dupliquer un skill à chaque exécution.

Le reste du code (`container`, `tools`, `betas`) était déjà correct par rapport
à l'API du SDK.

## Installer les dépendances

Depuis la racine du projet :

```
pip install -r requirements.txt
```

## Lancer l'exercice

```
python exercices/05-skill-in-request/main.py
```

Le script affiche le rapport de statut généré par Claude, structuré selon les
instructions du skill (Done / In progress / Blockers / Next steps).
