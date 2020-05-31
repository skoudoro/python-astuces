<!--title: Obtenir plus de controle sur le formatage de texte  -->
# [![Python Astuces](https://pythonastuces.com/images/python-logo.jpeg)](https://pythonastuces.com) Python Astuces

Bonjour à tous,

La newsletter est écrite en Markdown et j'utilise énormément le formatage de strings pour générer
cette email ainsi que les archives, sitemap, rss du site. Voici donc ci dessous un tableau
pour rappeler quelque concept simple pour le formatage de vos strings.

| Nombre     | Format  | Résultat   | Description                                   |
|------------|---------|------------|-----------------------------------------------|
| 3.1415926  | \{:.2f\}  | 3.14       | Affiche 2 decimal après la virgule            |
| 3.1415926  | \{:+.2f\} | +3.14      | Affiche le signe et 2 decimal après la virgule |
| -1         | \{:+.2f\} | -1.00      | Affiche le signe et 2 decimal après la virgule |
| 2.71828    | \{:.0f\}  | 3          | Aroundi et affiche un entier                  |
| 5          | \{:0>2d\} | 05         | ajout de zéros à gauche (decalage de 2)       |
| 5          | \{:x<4d\} | 5xxx       | ajout de 'x' à droite (decalage de 4)         |
| 10         | \{:x<4d\} | 10xx       | ajout de 'x' à droite (decalage de 4)  |
| 1000000    | \{:,\}    | 1,000,000  | Ajout d'un séparateur, ici la virgule         |
| 0.25       | \{:.2%\}  | 25.00%     | Afficher en pourcentage                       |
| 1000000000 | \{:.2e\}  | 1.00e+09   | Forcer l'affichage de l'exposant              |
| 13         | \{:10d\}  | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13 | Alignement du texte à droite (largeur de 10)  |
| 13         | \{:<10d\} | 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         | Alignement du texte à gauche (largeur de 10)  |
| 13         | \{:^10d\} | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    | Alignement du texte au centre (largeur de 10) |

Bonne fin de dimanche et Bonne semaine à tous!

**Serge ([@skoudoro](https://twitter.com/skoudoro))**

#### Astuces de la semaine

```python
# formattage classic
>>> titre = "Python Astuces"
>>> print("Bonjour {}".format(titre))
Bonjour Python Astuces

# Remplacer plusieurs valeurs
>>> part1, part2 = "Python",  "Astuces"
>>> print("Bonjour {} {}".format(part1, part2))
Bonjour Python Astuces

# changer l'ordre
>>> ide1 = "vscode"
>>> ide2 = "spyder"
>>> print(" {0} est mieux que {1} ".format(ide1, ide2))
vscode est mieux que spyder
>>> print(" {1} est mieux que {0} ".format(ide1, ide2))
spyder est mieux que vscode

# Utilisation due format spécial.
>>> pi = 3.1415926
>>> precision = 4
>>> print( "{:.{}f}".format(pi, precision))
3.1415

# Nommer vos variables
>>> print(" {ide1} est mieux que {ide2} ".format(ide1="vscode", ide2="spyder"))
vscode est mieux que spyder

# Utiliser une variable plusieurs fois
>>> print("{0} {0}{0} est vraiment {0} idole.".format("ton"))
ton tonton est vraiment ton idole

# Générer un tableau
>>> joueurs = [
...    ['Tony Parker', 4, 3, 7 ],
...    ['Nico Batum ', 5, 0, 21 ],
...    ['Nando De colo', 5, 8, 36 ],
...    ['Evan Fournier', 9, 4, 11 ],
...    ['Rudy Gobert', 3, 0, 2 ],
]

# On definit la fonction format dans un variable
>>> ligne_de_stats = "| {joueur:<16s} | {reb:2d} | {passes:2d} | {pts:2d} |".format

>>> for j in joueurs:
...    print(ligne_de_stats(joueur=j[0], reb=j[1], passes=j[2], pts=j[3]))

| Tony Parker      |  4 |  3 |  7 |
| Nico Batum       |  5 |  0 | 21 |
| Nando De colo    |  5 |  8 | 36 |
| Evan Fournier    |  9 |  4 | 11 |
| Rudy Gobert      |  3 |  0 |  2 |
```

#### Rappel PEP8 / PEP 20 de la semaine

[PEP 20](https://www.python.org/dev/peps/pep-0020/) contient les 19 commandements pour produire un code de qualité en Python. [PEP 8](https://www.python.org/dev/peps/pep-0008/) est LE guide détaillé pour améliorer la lisibilité de Python.

> “Now is better than never. Although never is often better than *right* now.” -- Zen Python

**A éviter**
```python
# A bannir absolument. Facilement remplacable
>>> for value in range(len(foo)):
...    pass
```

**Bon**

```python
>>> for indices, values in enumerate(foo):
...    pass
```

**Bonne Pythonnade  🐍!**

**[PythonAstuces.com](https://pythonastuces.com)**

---

[archives](https://pythonastuces.com/archives.html) | [flux rss](https://pythonastuces.com/rss.xml)
