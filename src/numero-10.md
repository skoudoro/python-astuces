<!--title: La curryfication avec "partial" -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Curryfication... Intriguant comme mot n'est ce pas? Cependant, c'est un concept très intéressant de la programmation. Je ne vais pas me lancer dans une longue et interminable explication. Je préfère vous partagez [cet article](https://medium.com/elp-2018/la-curryfication-au-coeur-de-la-programmation-fonctionnelle-5fd50ce0e858) et vous allez vite comprendre le lien avec l'astuce de la semaine.

En cas de question, n'hésitez pas à répondre à cet email.

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# partial nous permet de réduire / fixer le
# nombre d'arguments de notre fonction original

# On importe partial.
>>> from functools import partial

# On définit une fonction générale
>>> def multiplier(valeur, facteur):
...    return valeur * facteur
...
# Définition de nos fonctions partielles
>>> doubler = partial(multiplier, facteur=2)
>>> tripler = partial(multiplier, facteur=3)
>>> quintupler = partial(multiplier, facteur=5)

# on teste nos nouvelles fonctions.
>>> print(doubler(5))
10
>>> print(tripler(5))
15
>>> print(quintupler(5))
25
# équivalent à
>>> print(multiplier(valeur=5, facteur=5))
25
# équivalent à
>>> print(5 * 5)
25

# Partial est un outil qui vous permettra d'être
# plus explicite dans votre code. Par exemple, j'ai
# généralement une fonction `save` dans mon code et
# partial me permet de creer des fonctions qui s'auto-documente
# tel que `save_ply`, `save_png`, save_as` sans trop
# d'effort et simplifiant ainsi la maintenance et
# lisibilité du code.
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “If the implementation is easy to explain, it may be a good idea.” -- Zen Python

**A éviter**
```python
>>> obj = 5
>>> if type(obj) is type(1):
...    print("Je suis un entier")
```

**Bon**

```python
>>> obj = 5
>>> if isinstance(obj, int):
...    print("Je suis un entier")
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
