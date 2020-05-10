<!--title: Remplacer vos switch/case par un dictionnaire -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Connaissez vous [Google Season of Docs](https://developers.google.com/season-of-docs)? Je viens de remplir une candidature pour notre projet python opensource [FURY](https://github.com/fury-gl/fury).

- Si Vous êtes à l'aise avec python / [sphinx](https://www.sphinx-doc.org/en/master/) / git et la langue de shakespeare.
- Si Vous aimez écrire / améliorer les docs techniques ou développez des plugins.
- Si Vous souhaitez arrondir vos fins de mois tout en contribuant à un projet excitant.

N'hésitez pas à me faire signe (future candidature ou simple question)! Je vous tiendrai informer si notre projet a été sélectionné.

Bonne fin de dimanche et Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# switch/case classique que l'on rencontre un peu partout
>>> def obtenir_la_note(eleve):
...    if eleve == 'thomas':
...        return 15
...    elif eleve == 'bill':
...        return 9
...    elif eleve == 'jean':
...        return 19
...    else:
...        return -1
...
>>> obtenir_la_note('jean')
19

# Ceci peut être remplacer par un dictionnaire.
>>> def obtenir_la_note_via_dict(eleve):
...    notes = {'thomas': 15,
...             'bill': 9,
...             'jean': 19,}
...    return notes.get(eleve, -1)
...
>>> obtenir_la_note_via_dict('bill')
9

# Plus compacte, plus flexible, une bonne manière
# de simplifier votre code.
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “In the face of ambiguity, refuse the temptation to guess” -- Zen Python

La pep20 du jour recommande **d'éviter d'implémenter un code ambigu**. Ne laisser **aucune place au doute**, ne laisser pas votre code deviner la suite. Reprenons, l'exemple ci dessus pour illustrer ceci:

**A éviter/ code ambigu**
```python
# switch/case classique que l'on rencontre un peu partout
>>> def obtenir_la_note(eleve):
...    if eleve == 'thomas':
...        return 15
...    if eleve == 'bill':
...        return 9
...    if eleve == 'jean':
...        return 19
...    return
...
# Que se passe t il dans ce cas?
# Qu'elle est la valeur?
# Que signifie ce None?
# Attendu ou une erreur inconnu dans la fonction?
>>> print(obtenir_la_note('lucile'))
None
```

**Bon**

```python
>>> def obtenir_la_note(eleve):
...    if eleve == 'thomas':
...        return 15
...    elif eleve == 'bill':
...        return 9
...    elif eleve == 'jean':
...        return 19
...    else:
...        return None
...
# Nous savons explicitement qu'il y a le cas None à gerer.
# Cela peut être en générant une erreur ou, tout simplement,
# en ignorant l'élève.
>>> print(obtenir_la_note('lucile'))
None
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
