<!--title: NamedTuples vs Classes -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Notre projet python opensource [FURY](https://github.com/fury-gl/fury) a été accepté et participera donc à
[Google Season of Docs](https://developers.google.com/season-of-docs) !!!

- Si vous êtes à l'aise avec python / [sphinx](https://www.sphinx-doc.org/en/master/) / git et la langue de shakespeare.
- Si vous aimez écrire / améliorer les docs techniques ou développez des plugins.
- Si vous souhaitez arrondir vos fins de mois tout en contribuant à un projet excitant.

N'hésitez pas à me faire signe (future candidature ou simple question). Une page dédié sera créé et je vous partagerais le lien la semaine prochaine.

Bonne fin de dimanche et Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# Les namedtuples sont un outil qui vous permettra
# de simplifier votre code. En bonus, ils réduisent
# l'utilisation mémoire de votre code.

# Création d'un nouvel objet simple.
>>> from collections import namedtuple
>>> Point2D = namedtuple('Point2D' , ['x', 'y'])

# Creation de points grâce à notre nouvel objet
>>> mon_point_1 = Point2D(x=1, y=2)
>>> print(mon_point_1)
Point2D(x=1, y=2)
>>> mon_point_2 = Point2D(4, 5)
>>> print(mon_point_2)
Point2D(x=4, y=5)

# accès facile à nos valeurs
>>> distance_x = mon_point_1.x + mon_point_2.x
>>> print(distance_x)
5
# équivalent à
>>> distance_x = mon_point_1[0] + mon_point_2[0]
>>> print(distance_x)
5

# les tuples sont immuables, donc leur valeur ne peut
# pas être modifié. Vous devez créer un nouveau point
>>> mon_point_1.x = 10
AttributeError: "can't set attribute"

>>> mon_point_1 = Point2D(x=10, y=mon_point_1.y)
>>> print(mon_point_1)
Point2D(x=10, y=2)

# Créer un nouveau namedtuple depuis le précédent:
>>> Point3D = namedtuple('Point3D', Point2D._fields + ('z',))
>>> point = Point3D(x=1, y=2, z=3)
>>> print(point.x, point.y, point.z)
1, 2, 3

# Enfin pour les amateurs de dictionnaire...
>>> print(point._asdict())
{'x': 1, 'y': 2, 'z': 3}

# Bref, éviter de créer une classe si ce n'est pas
# nécessaire grâce aux namedtuples
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “If the implementation is hard to explain, it's a bad idea.” -- Zen Python

**A éviter**
```python
# Pas toujours évident à comprendre.
>>> if not foo is None:
...    pass
```

**Bon**

```python
>>> if foo is not None:
...    pass
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
