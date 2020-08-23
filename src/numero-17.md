<!--title: A quoi sert le mot clé nonlocal ? -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

Tout d'abord, j'aimerai vous remercier de suivre Python Astuces car vos questions ou commentaires sont toujours très intéressants.

Pour cela, chaque semaine, je partagerai l'un de vos projets / articles car il y a pas mal de contenus Python vraiment intéressants qui ne sont, malheureusement, pas assez mis en avant. N'hésitez à m'envoyer un mail si vous souhaitez partager un article ou un projet opensource sur lequel vous bossez (quelque soit votre niveau!).

Cette semaine, jetez un oeil sur ce projet vraiment sympa d'un abonné à Python Astuces: [labortablo](https://youtu.be/r9pEkCy_z5A) un environnement de bureau entièrement codé en python! Le code se trouve sur [cette page](https://gitlab.com/miamondo/labortablo).

Bonne lecture et bonne fin de dimanche à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Definissons une variable "valeur" sur 3 niveaux. Normalement,
# cette variable ne sera jamais modifié localement comme vous
# pouvez le voir ci dessous
>>> valeur = 0
>>> def ma_fonction():
...     valeur = 1
...     def fonction_imbriquée():
...         valeur = 2
...         print("fonction_imbriquée:", valeur)
...     fonction_imbriquée()
...     print("ma_fonction:", valeur)

>>> ma_fonction(); print("valeur global: {}".format(valeur))
fonction_imbriquée: 2
ma_fonction: 1
valeur global: 0

# Ajoutons le mot clé nonlocal pour voir l'effet causé.
>>> valeur = 0
>>> def ma_fonction():
...     valeur = 1
...     def fonction_imbriquée():
...         nonlocal valeur
...         valeur = 2
...         print("fonction_imbriquée:", valeur)
...     fonction_imbriquée()
...     print("ma_fonction:", valeur)

# Grâce au nonlocal, on a eu accès à la variable définit
# dans ma_function pour pouvoir la mettre à jour
>>> ma_fonction(); print("valeur global: {}".format(valeur))
fonction_imbriquée: 2
ma_fonction: 2
valeur global: 0

# Si l'on souhaite modifier la variable globale, il suffit
# de remplacer le mot clé nonlocal par global comme vous
# pouvez le voir ci dessous.
>>> valeur = 0
>>> def ma_fonction():
...     valeur = 1
...     def fonction_imbriquée():
...         global valeur
...         valeur = 2
...         print("fonction_imbriquée:", valeur)
...     fonction_imbriquée()
...     print("ma_fonction:", valeur)

>>> ma_fonction(); print("valeur global: {}".format(valeur))
fonction_imbriquée: 2
ma_fonction: 1
valeur global: 2

# nonlocal est un mot clé que j'utilise très souvent dans mes
# décorateurs donc je ne peux que vous le recommander.
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
