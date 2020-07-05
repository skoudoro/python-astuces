<!--title: A quoi sert l'opérateur @ ? -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Il y a 2 semaines, je vous ai parler du [Python developer Survey](https://www.jetbrains.com/lp/python-developers-survey-2019/) avec quelques statistiques intéréressantes.

Cette semaine, je vous recommande le [StackOverflow Developer Survey](https://insights.stackoverflow.com/survey/2020). Python reste la 4ème techno la plus utilisée et le salaire moyen d'un développeur python semble être de 59K(dollars).

Bref, jetez y un oeil !

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# L'opérateur @ est utilisé pour la mulplication
# de matrices.
# Il a été introdruit à partir de Python 3.5 pour
# éviter la confusion suivante:
#  - '*' (multiplication élément par élément )
#  - '@' (Produit scalaire de matrice)
# Pour plus d'informations vous pouvez
# jetez un oeil à la PEP0465

# cette opérateur n'est pas encore présent pour les
# listes donc on utilisera la librairie Numpy
# pour créer nos matrices
>>> import numpy as np

# création des matrices
>>> A = np.array([[1, 2],
...               [3, 4]])

>>> B = np.array([[5, 6],
...               [7, 8]])

# Multiplication matrices (élément par élément)
>>> C = A * B
>>> print(C)
[[ 5 12]
 [21 32]]

# Multiplication matrices (produit scalaire)
>>> C = A @ B
>>> print(C)
[[19 22]
 [43 50]]

# Ceci simplifiera la lecture et la comprehension
# de votre code si vous travaillez avez des matrices.
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Namespaces are one honking great idea -- let's do more of those!” -- Zen Python

Pour afficher la PEP20 complète à partir d'un terminal, ouvrez un interpreteur python et lancer

```python
>>> import this
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
