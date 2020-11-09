<!--title: Alternative au print? -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

J'espère que vous allez tous bien en cette période de confinement.

Comme chaque année, Python fait une enquête sur votre usage de python afin d'améliorer le language. Si vous avez 3-4 minutes, je vous conseille fortement de contribuer à cette enquête. Voici le lien: [Enquête Python](https://surveys.jetbrains.com/s3/c8-python-developers-survey-2020).

Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**


#### Astuces de la semaine

```python
# Cette astuce marche uniquement à partir de
# Python 3.8 et plus
#
# Faisons une opération classique dans un
# interpreteur interactif
>>> resultat = 7 + 11
# Pour afficher le résultat, nous sommes obligé
# d'appeler print
>>> print(resultat)
18

# En utilisant le walrus, on peut éviter cette
# étape supplémentaire du print
>>> (resultat := 7 + 11)
18

# Bien sur, comme précédemment, la variable résultat
# contient bien la valeur attendue.
>>> print(resultat)
18

# Pour information, ce n'est pas la fonctionnalité première
# du walrus. C'est un petit détournement qui vous permettra
# d'être plus rapide pour vérifier un résultat.
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
