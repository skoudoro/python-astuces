<!--title: underscore peut vous être utile -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

#### Astuces de la semaine

```python
# '_'  peut être utilisé comme séparateur de grand nombres

>>> vingt_billion = 20_000_000_000
>>> print(vingt_billion)
20000000000

# Mais '_' est aussi utilisé comme variable temporaire dans un
# interpreteur interactif.
>>> 2 + 2
4
>>> _
4
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.


> “Simple is better than complex.” -- Zen Python

**Mauvais et à éviter:**

```python
>>> if var == True:
>>>     print('var')
>>>
>>> if var == None:
>>>     print('var est nulle')
```

**Bon**

```python
# Tester juste la valeur
>>> if var:
>>>     print('var est vrai')

# ou bien tester la valeur fausse
>>> if not var:
>>>     print('var est faux')

# None est évalué comme False mais est un type particulier
>>> if var is None:
>>>     print('var is None')
```
**Happy Pythoning** 🐍!

**Serge ([@skoudoro](https://twitter.com/skoudoro)) - [pythonastuces.com](https://pythonastuces.com)**
