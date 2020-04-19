<!--title: itertools sous utilisé ? -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

J'espère que vous avez passé de bonnes fêtes de Pâques ! Petite nouveauté suite à une demande, les [archives](https://pythonastuces.com/archives.html) ainsi qu'un [flux rss](https://pythonastuces.com/rss.xml) sont maintenant disponibles sur le site [pythonastuces.com](https://pythonastuces.com). Encore un grand merci pour vos retours!

Bonne fin de dimanche et Bonne semaine à tous !

ps: Désolé pour le retard de cette édition ;-)

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# 'combinations' est une fonction tres pratique!
>>> fruits = ['pomme', 'banane', 'fraise',]
>>> salade_de_fruits = itertools.combinations(fruits, 2)
>>> print(salade_de_fruits)
('pomme', 'banane')
('pomme', 'fraise')
('banane', 'fraise')

# Utiliser 'compress' pour selectionner certains éléments de votre liste
>>> bieres = ['leffe', 'cuvée des trolls', 'affligem', 'duvel']
>>> selections = [False, True, False, True]
>>> ma_selection = itertools.compress(bieres, selections)
>>> print(list(ma_selection))
['cuvée des trolls', 'duvel']

# Obtenir une liste de permutations
>>> joueurs = ['tom', 'jules', 'louis']
>>> classements = itertools.permutations(joueurs)
>>> print(list(classements))
[('tom', 'jules', 'louis'),
 ('tom', 'louis', 'jules'),
 ('jules', 'tom', 'louis'),
 ('jules', 'louis', 'tom'),
 ('louis', 'tom', 'jules'),
 ('louis', 'jules', 'tom')]

# itertools dispose de beaucoup de fonctions très pratique.
# C'est un super package, très performant !
# n'hésitez pas à jeter un oeil sur ce module !
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Explicit is better than implicit.” -- Zen Python

***Mauvais et à éviter**

```python
# Je vois trop souvent cela : belle variable sans aucun sens!
>>> x = 'Juste Leblanc'
>>> y, z = x.split()
>>> print(z, y, sep=', ')
'Leblanc, Juste'

# noms de fontions pas explicite: db = Database ?
# db = double ?
>>> def db(x):
...     return x*2

```

**Bon**

```python
# Quand on peut éviter la documentation avec des variables
# explicites, autant le faire. Un commentaire deviens très vite un
# mensonge car on prend rarement la peine de les mettre à jour...

>>> nom_complet = 'Juste Leblanc'
>>> prenom, nom = name.split()
>>> print(nom, prenom, sep=', ')
'Leblanc, Juste'

# fonction explicite, on sait ou on va.
>>> def multiplication_par_deux(x):
...     return x*2
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
