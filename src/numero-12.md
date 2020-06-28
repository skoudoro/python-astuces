<!--title: Initialization d'une variable avec "OR" -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

On m'a posé [une question intéressante](https://stackoverflow.com/questions/62425728/fastest-way-to-fill-a-2d-ndarray-like-an-histogram?fbclid=IwAR2boyAzpEYwAf0Q0ItXjYL7A-FDm-TQBWtE7nkVzw0GRQ3dZpK4NJeuPgo) la semaine dernière que je n'ai malheureusement pas encore pris le soin de répondre.

En effet, j'ai pris une année de plus la semaine dernière et j'en ai profité pour me déconnecter à la montagne (d'où l'absence de l'astuce la semaine dernière).

N'hésitez pas à donner votre opinion sur la question en me répondant par mail ou directement sur [StackOverflow](https://stackoverflow.com/questions/62425728/fastest-way-to-fill-a-2d-ndarray-like-an-histogram?fbclid=IwAR2boyAzpEYwAf0Q0ItXjYL7A-FDm-TQBWtE7nkVzw0GRQ3dZpK4NJeuPgo).

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# OR est pratique pour définir des valeurs par defaut
>>> ma_variable = None or 'Great Smokies'
>>> print(ma_variable)
Great Smokies
>>> ma_variable = '' or 'Great Smokies'
>>> print(ma_variable)
Great Smokies
>>> ma_variable = 0 or 'Great Smokies'
>>> print(ma_variable)
Great Smokies
>>> ma_variable = "bonjour" or 'Great Smokies'
>>> print(ma_variable)
bonjour

# J'utilise très régulierement dans mes fonctions
# Voici un exemple basique
>>> def initialiser(var=None):
...    resultat = var or "valeur par default "
...    resultat *= 2
...    return resultat


>>> print(initialiser())
"valeur par default valeur par default "

>>> print(initialiser(15))
30

>>> print(initialiser(0))
"valeur par default valeur par default "

>>> print(initialiser('Python Astuces'))
"Python AstucesPython Astuces "

# test avec un string vide, on obtient
# la valeur par defaut.
>>> print(initialiser(''))
"valeur par default valeur par default "

# idem avec une liste ou un tuple vide
>>> print(initialiser([]))
"valeur par default valeur par default "
>>> print(initialiser([1, 2, 3]))
[1, 2, 3, 1, 2, 3]

# bien sur vous pouvez combiner plusieurs
# opérateurs logiques "or" sur une ligne, ce
# qui peut s'avérer ultra pratique
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Now is better than never. Although never is often better than *right* now.” -- Zen Python

**A éviter**
```python
>>> connecter = True

# facilement evitable
>>> if connecter == True:
...    print('connecter')

# grosse erreure car on compare le
# type et non la valeur
>>> if connecter is True:
...    print('connecter')

```

**Bon**

```python
>>> if connecter:
...    print('connecter')
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
