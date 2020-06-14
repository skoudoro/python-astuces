<!--title: Dictionnaires imbriqués -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Python Software Foundation a sorti un rapport sur les dernières tendances python. On y trouve des stats intéressantes donc je vous conseille d'y jeter un oeil : [Python Developers Survey](https://www.jetbrains.com/lp/python-developers-survey-2019/).

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# On définit un simple dictionnaire imbriqué
>>> notes = {"alex": {'math': 15,
...                   'francais': 5
...                  },
...          "Jean": {'math': 8,
...                   'francais': 18
...                  }
...          }

# La manière classique d'accéder à une valeur:
>>> print(notes["alex"]["math"])
15

# Si la clé n'existe pas, vous risquez
# de générer l'erreur KeyError. Je recommande
# donc d'utilisez "get" qui permet de définir
# une valeur par défaut si la clé n'est pas trouvé.
>>> print(notes.get("alex", {}).get("math", "Not Found"))
15

>>> print(notes.get("ale", {}).get("math", "Not Found"))
Not Found

# pour généraliser l'expression ci dessus, nous créons
# une fonction qui nous retourne la valeur quelque soit
# la profondeur du dictionnaire imbriqué. Si la clé souhaitée
# n'est pas trouvé, un dictionnaire vide est retourné.
>>> def get_value(dictionnaire, liste_de_cle):
...     valeur = dictionnaire
...     for l in liste_de_cle:
...         valeur = valeur.get(l, {})
...
...     if not valeur:
...         return "erreur dans une clé"
...     return valeur

# on teste avec des clés valides
>>> print(get_value(notes, ['alex', 'math']))
15

# on teste avec une des clés invalides
>>> print(get_value(notes, ['alex', 'mathématiques']))
"erreur dans une clé"

# J'utilise énormément la fonction ci dessus, quand
# je dois bosser avec le format JSON. Cela vous évitera
# d'avoir une tonne de try/except
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Readability counts.” -- Zen Python

**A éviter**
```python
>>> foo = "bar à tapas"
>>> if foo[:3] == 'bar':
...    print('found')
found
```

**Bon**

```python
>>> foo = "bar à tapas"
>>> if foo.startswith('bar'):
...    print('found')
found
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
