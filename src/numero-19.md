<!--title: Attention à bool! Alternative 2-3 fois plus rapide -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Avez vous noté:

- La "fin de vie" de Python 3.5 depuis début Septembre. Je vous conseille de mettre à jour votre version de python si vous êtes toujours sur python 3.5. Par fin de vie, je parle bien sur de l'arrêt de la maintenance de cette version de python, pas de panique, vous avez encore du temps pour migrer :-).
- La sortie fin Octobre de Python 3.9 avec plusieurs nouvelles fonctionnalités. J'aborderai les nouvelles fonctionnalités dans 1 ou 2 nouveaux numéros en Décembre.

En attendant, profitez bien de l'astuce de la semaine,

Bonne dimanche et bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Pour cette astuce, nous allons utilisé la
# fonction timeit dans l'interpreteur interactif
# afin de mesurer les performances de notre commande

# Définissons une variable
>>> ma_variable = 3.14

# Convertissons cette variable en bool et mesurons
# la performance de cette conversion.
>>> timeit bool(ma_variable)
83.9 ns ± 0.294 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

# il est temps d'utiliser notre ruse pour
# obtenir le même résultat plus rapidement.
>>> timeit not not ma_variable
30.6 ns ± 0.433 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

# Sur ma machine, on voit que la seconde solution
# (utilisation du "not not" au lieu de "bool")
# est 2.74 fois plus rapide tout en obtenant le même
# résultat. Je vous laisse expérimenter.
>>> print(bool(ma_variable))
True
>>> print(not not ma_variable)
True

# Ci dessous, un exemple pratique si vous avez besoin
# de votre propre objet.
>>> class MonObjectRapide:
...     def __init__(self):
...         self.ma_variable = 2
...     def __bool__(self):
...         return not not self.ma_variable
...
>>> class MonObjectLent:
...     def __init__(self):
...         self.ma_variable = 2
...     def __bool__(self):
...         return bool(self.ma_variable)
...
>>> lent = MonObjectLent()
>>> rapide = MonObjectRapide()

# Evaluons la performance des 2 objets avec un if.
# Pour des raisons pratiques, tout sera sur une ligne.
>>> timeit if lent:pass
206 ns ± 0.308 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> timeit if rapide:pass
99.8 ns ± 1.12 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

# Un gain en performance non négligeable si vous
# souhaitez accélérer votre code. Pour les débutants
# le code ci dessus est équivalent à:
>>> if lent:
...    pass
...
>>> if rapide:
...   pass
...

# Comme toute optimisation, ceci risque de rendre
# votre code moins lisible donc à utiliser avec
# modération.
#
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
