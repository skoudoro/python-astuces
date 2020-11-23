<!--title: Gérer les espaces  ... -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Avec un léger retard, voici le numéro de cette semaine!

Bonne semaine à tous!

ps: avez vous vu passé [ce tweet](https://twitter.com/gvanrossum/status/1326932991566700549) du createur de python?
Espérons qu'un jour, python soit nativement disponible sur Windows comme ces homologues Linux et MacOS ;-).

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Définissons un simple texte
>>> message = "Bonne Semaine a tous"

# Cependant, nous souhaitons normaliser
# notre texte avec une taille particulière.
# Dans le cas ci dessous, le texte doit
# avoir une taile de 40 caracteres.
# Etant donné que les espaces ne sont pas
# visibles, ils seront remplacés par '-'
# afin de mieux visualiser le concept.
>>> taille = 40

# Justification du texte à gauche
>>> texte_a_gauche = message.ljust(taille, '-')
>>> print(texte_a_gauche)
Bonne Semaine a tous--------------------

# Justification du texte à droite
>>> texte_a_droite = message.rjust(taille, '-')
>>> print(texte_a_droite)
--------------------Bonne Semaine a tous

# Centrer le texte
>>> texte_au_centre = message.center(taille, '-')
>>> print(texte_au_centre)
----------Bonne Semaine a tous----------

# Contrairement à la semaine dernière, fonction
# bien utile et donc, à utiliser sans modération!
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
