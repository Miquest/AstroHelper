# orbital_elements.py

In dieser Datei findet sich eine Sammlung an Funktionen, die das Handling der JSON Daten
vereinfachen sollen. Hierzu kommt wieder eine Klasse als Modell zum Einsatz.
Zu beachten ist, dass die *orbital_elements.json* im selben Verzeichnis liegen muss, da das Programm sonst nicht darauf zugreifen kann.


## Nutzung der Klasse
Um die Klasse zu nutzen, muss sie wie gewohnt zunächst importiert werden:
```
from orbital_elements import OrbitalElements

orbital_elements = OrbitalElements()
```
## Eigenschaften (Properties)
Um sich anzeigen zu lassen, welche Planeten in der JSON Datei verfügbar sind, kann man sich die Planeten
nach Instanziierung der Klasse als Liste/Array ausgeben lassen:
```
print(orbital_elements.planets)
```
Möchte man die Bahnelemente zur Epoche J2000.0 oder die Änderungsraten der Bahnelemente
abrufen, so muss man zunächst festlegen, um welchen Planeten man sich kümmern möchte.
Sowohl Bahnelemente als auch die sakulären Änderungsraten sind als Eigenschaft der Klasse
implementiert:
```
orbital_elements.planet = "Mars"

print(orbital_elements.change_rates)
print(orbital_elements.elements)
```
Beide Werte werden als Dictionary zurückgegeben und können die Variablen im Code genutzt werden.
Es kann auch mit der gewohnten Syntax für Dictionaries auf einzelne Einträge des Dictionarys zugegriffen werden:

```
print(orbital_elements.change_rates["de"])
```