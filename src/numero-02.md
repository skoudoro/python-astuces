<!--title: Deux très bon alliés: unpacking et arguments de fonction -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Tout d'abord, un grand merci pour les contributions surprises sur le projet opensource [FURY!](https://github.com/fury-gl/fury) Je ne me m'y attendais pas :-), ce n'est pas le but de la liste mais cela fait toujours plaisir. L'astuce est la semaine est donc dédié au code que j'ai pu voir lors de la révision de ces Pull Requests (PR). Une question ? Une idée ? Une erreur ? Une remarque ? N'hésitez pas à répondre à cette email !

Bonne fin de dimanche et Bonne semaine à tous !

#### Astuces de la semaine

```python
# La magie de l'unpacking dans les arguments de fonctions

>>> def ma_fonction(a, b, c):
...     print(a, b, c)

>>> pt_list = [1, 0, 1]
>>> pt_tuple = (1, 0, 1)
>>> pt_dict = {'a': 1, 'b': 0, 'c': 1}

>>> ma_fonction(*pt_tuple)
1, 0, 1

>>> ma_fonction(*pt_list)
1, 0, 1
>>> ma_fonction(**pt_dict)
1, 0, 1

# l'ordre n'a pas d'importance si vous précisez les arguments
>>> ma_fonction(b=0, a=1, c=1)
1, 0, 1
# l'appel de fonction classique
>>> ma_fonction(1, 0, 1)
1, 0, 1
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Sparse is better than dense.” -- Zen Python

***Mauvais et à éviter**

```python
# manque d'espace
>>> i=i+1
>>> submitted +=1

# Trop d'espace, on ne distingue plus les priorités
>>> x = x * 2 - 1
>>> hypot2 = x * x + y * y
>>> c = (a + b) * (a - b)

# les "keywords" arguments ne doivent pas contenir d'espaces
>>> def complex(real, imag = 0.0):
...     return magic(r = real, i = imag)
```

**Bon**

```python
>>> i = i + 1
>>> submitted += 1
>>> x = x*2 - 1
>>> hypot2 = x*x + y*y
>>> c = (a+b) * (a-b)
>>> def complex(real, imag=0.0):
...    return magic(r=real, i=imag)
```

**Happy Pythoning 🐍!**

**Serge ([@skoudoro](https://twitter.com/skoudoro)) - [pythonastuces.com](https://pythonastuces.com)**

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)