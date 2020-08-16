<!--title: frozenset dans vos dictionnaires -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Après 2 semaines d'absence due à d'importantes deadlines, j'espère que Python Astuces vous a manqué ;-)

[L'afpy](https://afpy.org/) organise une conférence python en France: [PyconFr 2020](https://www.pycon.fr/2020/fr/index.html). Pour le moment, il y a très peu d'information mais n'hésitez pas à y jeter un oeil pour retenir les dates.

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Créons un dictionnaire avec comme clé des
# tuples (nom, prenom) du sportif
>>> surnoms_sportif = {
...    ("gabriel", "heinze") : "El Gringo",
...    ("fabien", "barthez") : "le divin chauve",
...    ("eric", "cantona")  : "the king",
...    ("mickael", "pietrus") : "air france",
...    ("hakeem", "olajuwon") : "hakeem the dream",
...    ("allen", "iverson") : "the answer",
...    }

# Pour accéder au surnom
>>> print(surnoms_sportif[("gabriel", "heinze")])
"El Gringo"
# Malheureusement, si vous interchangez nom et prenom
# vous aurez l'erreur suivante:
>>> print(surnoms_sportif[("heinze", "gabriel")])

KeyError            Traceback (most recent call last)
----> 1 print(surnoms_sportif[("heinze", "gabriel")])
KeyError: ('heinze', 'gabriel')

# Pour rendre plus flexible votre clés de dictionnaire
# vous pouvez le créer de la manière suivante:
>>> surnoms_sportif = {
...    frozenset({"gabriel", "heinze"}) : "El Gringo",
...    frozenset({"fabien", "barthez"}) : "le divin chauve",
...    frozenset({"eric", "cantona"})  : "the king",
...    frozenset({"mickael", "pietrus"}) : "air france",
...    frozenset({"hakeem", "olajuwon"}) : "hakeem the dream",
...    frozenset({"allen", "iverson"}) : "the answer",
...    }

# Et cette voici, les valeurs de clés sont interchangeables
>>> print(surnoms_sportif[frozenset({"hakeem", "olajuwon"})])
"hakeem the dream"
>>> print(surnoms_sportif[frozenset({"olajuwon", "hakeem"})])
"hakeem the dream"

# Je vous accorde que la syntaxe est légèrement plus
# lourde, cependant, ceci peut vraiment rendre votre code
# plus flexible.
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
