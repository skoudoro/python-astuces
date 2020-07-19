<!--title: Alternative aux boucles imbriquées -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

L'astuce d'aujourd'hui vous permettra d'améliorer les performances de votre code (du moins, je l'espère). Si Vous souhaitez que je parle un peu plus de la notation Big O, n'hésitez à me répondre à cette email et je m'adapterais en fonction de la demande.

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# le module product est très important dans cette
# astuce
>>> from itertools import product

# création d'une liste imbriquée. Cela pourrait
# être une image par exemple
>>> A = [[1, 2, 3, 4],
...      [5, 6, 7, 8]]

>>> B = [[0, 0, 0, 0],
...      [0, 0, 0, 0]]

# Manière classique / complexité O(n2).
# Plus la liste sera grande et plus
# l'opération ci dessous sera lent.
>>> for x in range(2):
...    for y in range(4):
...        B[x][y] = A[x][y] * 2

>>> print(B)
[[2, 4, 6, 8],
 [10, 12, 14, 16]]

# Voici une alternative / complexité O(n)
# Je vous la recommande!
>>> for x, y in product(range(2), range(4)):
...    B[x][y] = A[x][y] * 2

>>> print(B)
[[2, 4, 6, 8],
 [10, 12, 14, 16]]

# Dans ce cas, on génére tous les indices
# possibles grâce à la fonction "product" ce qui nous
# permet de réduire la complexité de notre algorithme
# et d'éviter les boucles imbriquées !

# Si vous avez 3 boucles imbriquées, le même principe
# fonctionne! Les indices générés vous permettront
# d'accéder facilement à vos listes / dictionnaires
# etc...

>>> for x, y, z in product(range(2), range(3), range(4)):
...    print(x,y,z)
0 0 0
0 0 1
0 0 2
0 0 3
0 1 0
0 1 1
0 1 2
0 1 3
0 2 0
0 2 1
0 2 2
0 2 3
1 0 0
1 0 1
1 0 2
1 0 3
1 1 0
1 1 1
1 1 2
1 1 3
1 2 0
1 2 1
1 2 2
1 2 3

# Je parle d'indices, mais cette astuce est possible
# avec différent type de données. N'hésitez pas à
# expérimenter et poser des questions si vous avez
# des soucis, je ferais de mon mieux pour vous
# répondre.
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
