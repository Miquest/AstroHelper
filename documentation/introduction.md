# Einführung in Python

Python ist eine höhere, dynamisch typisierte Programmiersprache.
Um mit dieser Bibliothek zu arbeiten, gibt es ein paar Grundkonzepte, die
verstanden werden sollten.


## Klassen
Klassen gehören zum Konzept der Objektorientierten Programmierung (OOP, Object Oriented Programming).
Diese ist von der echten Welt inspiriert und orientiert sich an "Objekten" als Teile des Codes mit verschiedenen
Funktionalitäten. Ein Objekt besitzt üblicherweise einige Eigenschaften und Methoden (also Funktionalitäten).
Manche brauchen Informationen, um erschaffen zu werden, andere nicht. Ein Löffel einer bestimmten Art wird
beim Erschaffen immer gleich bleiben, während ein Auto unterschiedliche Farben zugewiesen bekommen kann.
Hier ein praktisches Beispiel in Python:

```
class Auto:
    def __init_(self, color: str):
        self.color = color
        self.kilometers_driven = 0
        self.doors_opened = False

    def drive(self, distance: int):
        self.kilometers += distance

    def open_doors(self):
        self.doors_opened = True

    def close_doors(self):
        self.doors_opened = False

```
Hier definieren wir die Klasse "Auto", die zur erstmaligen Instanziierung ("Erschaffung") eine Information,
nämlich die Farbe des Autos, benötigt. Außerdem hat es vom Initiierungszeitpunkt an einige Eigenschaften mit
bereits festgelegten Werten (\__init\__ Methode). Diese sind für jede Instanz (also jedes erschaffene Objekt) gleich.
Außerdem bietet das Objekt "Auto" einige Funktionalitäten (Methoden) an, die man verwenden kann und die die Eigenschaften
des Objektes beeinflussen.

Genutzt wird das Ganze wie Folgt:
```
audi = Auto("Grün")
bmw = Auto("Rot")

audi.drive(20)
bmw.drive(50)

audi.open_doors()

print(bmw.kilometers_driven)
```

So können zwei verschiedene Objekte unabhängig voneinander instanziiert (erschaffen) und in Variablen gespeichert.
Man kann die Methoden und Eigenschaften des Objektes nun verwenden und damit arbeiten.

Alle Module dieses Repositorys sind in Klassen aufgebaut, die instanziiert werden und für Berechnungen verwendet werden können.
So wird die Verwendung einfacher, da die Klassen jeweils eine Sammlung von Variablen und Methoden
anbieten und das Hauptprogramm entlasten. Die Verwendung der Klassen, deren Eigenschaften und Methoden
werden in den jeweiligen Dokumentationen beschrieben ([siehe README.md Datei](../README.md))

## Import
Python ist modular aufgebaut und hat standardmäßig nicht die volle Funktionalität.
Das macht die Sprache deutlich speicherfreundlicher, da die Module nur nach Bedarf geladen
werden. Der Import der Module funktioniert wie Folgt:

```
import <modulname>
```
Ist der Name des Moduls zur Verwendung im Code zu lang oder kompliziert, kann das Modul zur Verwendung
in der aktuellen Datei umbenannt werden:

```
import <modulname> as <dein name>
```
Will man nur eine einzige Funktion aus einer Bibliothek importieren, kann man das wie folgt tun:

```
from <modulname> import <funktion>
```
Mehrere Funktionen können mit Kommata separiert werden, also zum Beispiel:
```
from math import sqrt, pi
```


