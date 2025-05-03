# Einführung in Konzepte der Bibliothek

Um mit dieser Bibliothek zu arbeiten, gibt es ein paar Grundkonzepte, die zumindest oberflächlich
verstanden werden sollten.

## Klassen

### Das Konzept
Klassen gehören zum Konzept der Objektorientierten Programmierung (OOP, Object Oriented Programming).
Dieses ist von der echten Welt inspiriert und orientiert sich an "Objekten" als Teile des Codes mit verschiedenen
Funktionen und Variablen. Ein Objekt besitzt üblicherweise einige Eigenschaften (Variablen) und Methoden (also Funktionen).
Manche Objekte brauchen Informationen, um erschaffen (instanziiert) zu werden, andere nicht. Ein Löffel einer bestimmten Art wird
beim Herstellen immer gleich bleiben, während ein Auto des selben Modells in unterschiedlichen Farben lackiert werden kann.
Um das zu visualisieren, verwenden wir ein praktisches und anschauliches Beispiel:

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
Hier definieren wir die Klasse "Auto", die zur erstmaligen Instanziierung eine Information,
nämlich die Farbe des Autos als String, benötigt. Außerdem besitzt es vom Initiierungszeitpunkt an einige Eigenschaften mit
bereits festgelegten Werten (siehe \__init\__ Methode). Diese sind für jede Instanz (also jedes erschaffene Objekt) gleich.
Außerdem bietet das Objekt "Auto" einige Funktionalitäten (Methoden) an, die man verwenden kann und die die Eigenschaften
des Objektes beeinflussen.

Das wiederkehrende "self" Schlüsselwort steht als Referenz für die aktuelle Instanz des Objektes. Es wird also als Parameter
die aktuelle Instanz des Objektes übergeben oder darauf zugegriffen, damit Python weiß, wessen Eigenschaften es
nun verändern soll und wessen Methoden ausgeführt werden sollen. Die Übergabe des Parameters erfolgt dabei implizit, wie wir im Folgenden sehen werden.

### Verwendung der Objekte

Um die Objekte nun im Code zu nutzen und deren Methoden aufzurufen, müssen wir zunächst Instanzen erzeugen:
```
audi = Auto("Grün")
bmw = Auto("Rot")
```
Der Methodenaufruf funktioniert dann wie Folgt:
```
audi.drive(20)
bmw.drive(50)

audi.open_doors()
print(bmw.kilometers_driven)
```

So können zwei verschiedene Objekte unabhängig voneinander instanziiert (erschaffen) und in Variablen gespeichert werden.
Man kann die Methoden und Eigenschaften des Objektes nun verwenden und damit arbeiten.

Alle Module dieses Repositorys sind in Klassen aufgebaut, die instanziiert werden und für Berechnungen verwendet werden können.
So wird die Verwendung einfacher, da die Klassen jeweils eine Sammlung von Variablen und Methoden
anbieten und das Hauptprogramm übersichtlicher machen.
So kann man auch dem DRY Prinzip (Do not Repeat Yourself) folgen und muss die Funktionalitäten nurnoch aufrufen, anstatt
sie komplett neu zu implementieren. Die Verwendung der Klassen, deren Eigenschaften und Methoden
werden in den jeweiligen Dokumentationen beschrieben ([siehe README.md Datei](../README.md))

### Weiterführendes
Möchte man eine Methode in den Kontext des Objektes einordnen, weil sie semantisch am besten dorthin passt und anderswo
für Verwirrung sorgen würde, diese aber unabhängig von der aktuellen Instanz ist (also auf keine
Eigenschaften zugegriffen werden muss) kann man die Methode als statisch markieren:
```
@staticmethod
def one_plus_one():
    return 1 + 1
```

__Außerdem__ ist es möglich, Eigenschaften mithilfe von Funktionen zu definieren. Üblicherweise verstehen wir Eigenschaften
als "Variablen des Objektes". Manchmal reicht diese Variable allein aber nicht, um das Ziel zu erreichen, da man die dort
gespeicherten Daten für den Abruf oder das Verändern der Eigenschaft anpassen möchte. Ein typisches Szenario ist die
Speicherung von verschlüsselten Daten, die vor dem Abruf und vor der Speicherung Ent- bzw. Verschlüsselt werden müssen,
um für einen Menschen lesbar zu sein. Auch hier hat Python eine Lösung parat:

```
class UserAccount:
    def __init__(self, user: str, password: str):
        self.encrypted_password = self.encrypt(password)
        self.username = user

    def encrypt(self, text: str):
        return encryption_algorithm_blabla(text.encode("utf-8"))

    def decrypt(self, text: bytes):
        return decryption_algorithm_blabla(text.decode("utf-8"))

    @property
    def password(self):
        return self.decrypt(self.encrypted_password)

    @password.setter
    def password(self, value: str):
        self.encrypted_password = self.encrypt(value)
```
Hier wird das Passwort beim Setzen ver- und beim Zugriff entschlüsselt, ohne dass die Methode
vom Benutzer der Klasse explizit aufgerufen werden muss.
Andernfalls müsste man die Eigenschaft *encrypted_password* als Argument für die Funktion *decrypt* übergeben oder
den Rückgabewert der *encrypt* Methode manuell in der *encrypted_password* Eigenschaft speichern, was den Code für die
Verwendung des Objektes unübersichtlicher und weniger intuitiv macht.

*Übrigens!*\
Man hat sich in der Community von Python inoffiziell auf einige Namenskonventionen geeinigt:

- __ClassName__ (Upper Camel Case)
- __variable_name__ (Snake Case)
- __function_name__ oder __functionName__ (Snake Case / Lower Camel Case)

Es ist natürlich keineswegs verpflichtend, sich an diese Konventionen zu halten, die Benutzung macht den Code
aber wesentlich übersichtlicher für Menschen, die ihn zum ersten Mal lesen!


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

Möchte man Funktionen aus einer eigenen Datei importieren, so kann man das ebenfalls mithilfe des Import Statements tun.
Dabei ist zu beachten, dass die zu importierende Datei im selben Verzeichnis liegen muss!

