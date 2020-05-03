<!--title: Le fameux __slot__ -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Cette année, tout était pret: billet d'avion, place pour la conférence, etc... bref, pret pour ma première conférence Python (conférence Scipy à Austin, Texas). Mais malheureusement, COVID-19 en a décidé autrement...

Donc aujourd'hui, j'ai une simple question pour vous: lorsque cette pandémie sera terminé (disons l'année prochaine), quelle conférence Python me conseillez vous? Ce sera peut être l'occasion de vous rencontrez! J'ai hâte de lire vos retours (en répondant à cette email).

Bonne fin de dimanche et Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# __slot__ est un attribut que vous pouvez ajouter à
# votre classe et qui vous permet de sauver de la mémoire
# ainsi qu'améliorer les performances de lecture/écriture
# de vos attributs de classes. Cependant, ceci réduira la
# flexibilité de vos classes.
# Performance vs Flexibilité ?

>>> class MaClasseAvecSlots:
...    __slots__ = ('x', 'y')
...
...    def __init__(self, x, y):
...        self.x, self.y = x, y

>>> class MaClasseClassic:
...
...    def __init__(self, x, y):
...        self.x, self.y = x, y

>>> test = MaClasseClassic(1, 2)
>>> test.z = 3
>>> print(test.x, test.y, test.z)
1 2 3

# __slot__ ne nous permet pas de creer
# de nouveau attributs dynamiquement

>>> test_slot = MaClasseAvecSlots(1, 2)
>>> test_slot.z = 3
AttributeError: 'MaClasseAvecSlots' object has no attribute 'z'

# Plusieurs articles montrent un gain en performance de
# lecture/écriture d'au moins 20% ainsi q'une reduction
# de la mémoire d'au moins 50% de votre classe. Cependant,
# __slot__ est à utiliser avec parcimonie car il réduit la
# flexibilité de votre code. Cette fonctionnalité est très
# intéressante et je vous recommande d'en lire plus.
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Special cases aren't special enough to break the rules.” -- Zen Python

**Correct mais simplifiable**

```python
>>> valeur_par_default = 'Aucune de reponse'
>>> mes_reponses = ['oui', 0, 'bonjour', None, 10, [], [0, 1, 2], '']
>>> for reponse in mes_reponses:
...    if reponse:
...        print(reponse)
...    else:
...        print(valeur_par_default)
...
oui
Aucune de reponse
bonjour
Aucune de reponse
10
Aucune de reponse
[0, 1, 2]
Aucune de reponse
```

**Bon**

```python
# En respectant la pep20, voici ce qu'on obtient.
# Ici, l'opérator logique OR nous permet de d'eviter de
# gérer chaque cas, en supprimant des if/else inutiles.
>>> valeur_par_default = 'Aucune de reponse'
>>> mes_reponses = ['oui', 0, 'bonjour', None, 10, [], [0, 1, 2], '']
>>> for reponse in mes_reponses:
...
...    print(reponse or valeur_par_default)
...
oui
Aucune de reponse
bonjour
Aucune de reponse
10
Aucune de reponse
[0, 1, 2]
Aucune de reponse

```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
