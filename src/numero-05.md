<!--title: L'utilité de contextlib.suppress -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

C'est une semaine qui démarre bien: J'ai eu la confirmation que notre projet opensource [FURY](https://github.com/fury-gl/fury) participera bien à [Google Summer of Code](https://summerofcode.withgoogle.com/). Nous allons pouvoir agrandir notre communauté et former des étudiants au monde opensource + python. Excitant tout cela!

D'ailleurs, en parlant de communauté, nous avons dépassé cette semaine les 300 abonnés. Un grand merci à tous et n'hésitez pas à continuer de parler de la newsletter autour de vous !

Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# Lorsque vous souhaitez ignorer une erreur attendue,
# contextlib propose une syntax beaucoup plus clair et
# simplifié que le traditionnel try/except

>>> import contextlib
>>> with contextlib.suppress(FileNotFoundError):
...    os.remove('somefile.tmp')

# Le code ci dessus est equivalent à:

>>> try:
...    os.remove('somefile.tmp')
... except FileNotFoundError:
...    pass
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Flat is better than nested.” -- Zen Python

**Code Imbriqué ("nested code")**

```python
>>> ma_liste = [1,2,3,4,5,6,7,8]
>>> nombre_impair = []
>>> for nombre in ma_liste:
...    if nombre % 2 != 0:
...        nombre_impair.append(nombre)

>>> print(nombre_impair)
[1, 3, 5, 7]
```

**Code simplifié (flat code)**

```python
# En respectant la pep20, voici ce
# qu'on obtient avec une liste de comprehension
>>> ma_liste = [1,2,3,4,5,6,7,8]
>>> nombre_impair = [x for x in ma_liste if x%2 != 0]
>>> print(nombre_impair)
[1, 3, 5, 7]

# "Flat is better than nested" incite à utiliser les
# listes de comprehension, les fonctions filter, map, reduce
# ou les operateurs ternaires afin de simplifier au maximum
# votre code.
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
