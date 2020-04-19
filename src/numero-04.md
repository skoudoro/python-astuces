<!--title: Vous avez dit unicode ? -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

J'ai oublié de préciser que toutes les "astuces" sont compatibles avec python 3.5+. Etant donné la fin de vie
de notre très chère python 2 ainsi que les versions précédentes à 3.5, je ne prends pas la peine de vérifier cela.
D'ailleurs, si vous souhaitez connaitre le cyle de développement de python, ainsi que le calendrier des nouvelles version de python, [jetez un oeil sur cette page](https://devguide.python.org/#status-of-python-branches).
Comme d'habitude, si vous avez des questions ou remarques, [n'hesitez pas à répondre au mail!](mailto:info@pythonastuces.com)

Bonne fin de dimanche et Bonne semaine !

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# Python accepte les caractères spéciaux.
>>> résumé = 'mon cool résumé'
>>> print(résumé)
mon cool résumé

>>> El_Niño = "l'enfant en espagnol"
>>> print(El_Niño)
"l'enfant en espagnol"

# Pas vraiment recommandé mais cela peut s'avérer utile pour les math
>>> import math
>>> π = math.pi
>>> print(π)
3.141592653589793

# Par contre, cela ne fonctionne que pour les caractères.
# L'example suivant ne fonctionne pas
>>> 😓= 'désolé'
SyntaxError: invalid character in identifier
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “If the implementation is hard to explain, it’s a bad idea.” -- Zen Python

***Mauvais et à éviter**

```python
# Lambda est très utile mais doit être utilisé rarement et avec parcimonie.
>>> multiplication_par_deux = lambda x: 2*x

# Soyez précis sur les exceptions que vous souhaitez traiter
>>> try:
...    value = collection[key]
... except Exception:
...    return key_not_found(key)
```

**Bon**

```python
# On remplace lambda par une fonction clair et explicite
>>> def multiplication_par_deux(x):
...     return x*2

# Chacune des erreurs doivent être traité du mieux possible.
>>> try:
...    value = collection[key]
... except KeyError:
...    return key_not_found(key)
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
