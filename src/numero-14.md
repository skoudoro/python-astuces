<!--title: zip vs zip_longest -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Et sans plus attendre, le numéro 14 de Python Astuces.

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Contrairement à zip, zip_longest à besoin
# d'être importé
>>> from itertools import zip_longest

# création de 2 listes de même taille
>>> A = [1, 2, 3, 4]
>>> B = ['A', 'B', 'C', 'D']

# Dans ce cas particulier, zip et zip_longest
# donneront le même résultat
>>> for val in zip(A, B):
...    print(val)
(1, 'A')
(2, 'B')
(3, 'C')
(4, 'D')

# création de 2 listes de différente taille
>>> A = [1, 2, 3, 4, 6, 7, 8]
>>> B = ['A', 'B', 'C', 'D']

# Dans ce cas, zip stoppe l'itération à
# la liste la plus courte.
>>> for val in zip(A, B):
...    print(val)
(1, 'A')
(2, 'B')
(3, 'C')
(4, 'D')

# Contrairement à zip_longest qui continuera
# jusqu'a la liste la plus longue et complétera
# la seconde avec une valeur par defaut
>>> for val in zip_longest(A, B, fillvalue='-'):
...    print(val)
(1, 'A')
(2, 'B')
(3, 'C')
(4, 'D')
(6, '-')
(7, '-')
(8, '-')

# Alternative à zip_longest pour obtenir le
# même comportement
>>> A = [1, 2, 3, 4, 6, 7, 8]
>>> B = ['A', 'B', 'C', 'D']

# ici, on s'assure que A et B on la même taille
# afin d'utiliser zip au lieu de zip_longest
>>> B += ['-',] * (len(A) - len(B))

>>> for val in zip(A, B):
...    print(val)
(1, 'A')
(2, 'B')
(3, 'C')
(4, 'D')
(6, '-')
(7, '-')
(8, '-')
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
