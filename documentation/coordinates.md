# coordinates.py

Diese Datei beinhaltet eine Klasse zum komfortablen
Handling von sowohl 2D als auch 3D Koordinaten in
cartesischer und polarer Form. Dabei passt sich die Klasse dynamisch
an die Dimensionen der Koordinaten an, eine Differenzierung ist für
die Nutzung somit nicht nötig.

Initiiert wird die Klasse wie folgt:

```
from coordinates import Coordinates

my_coordinates = [[1, 2, 3],[-1, 2, 3],[-1, 2, 0]]
coords = Coordinates(my_coordinates)
coords.radians = True
```
Hier wird eine Instanz der Klasse mit diesen Koordinaten erstellt. Wahlweise kann statt
einer Variable auch direkt der Array übergeben werden. Eine Konvertierung in einen
Numpy Array ist nicht nötig, dies geschieht intern in der Klasse.
Außerdem werden durch *coords.radians = True* die Berechnung mit dem
Bogenmaß anstatt des Gradmaßes durchgeführt. Standardmäßig sind alle Rückgabewerte im Gradmaß,
wenn man nicht explizit das Bogenmaß als Einheit aktiviert.

Möchte man während der Nutzung einzelne Koordinaten hinzufügen oder alle
gespeicherten Koordinaten überschreiben, kann man das mit folgenden Befehlen tun:
```
coords.coordinates = [[1, 2, -3],[-1, 2, 0]]
coords.add_coordinate([1, 1, 1])
```
Da die Klasse intern mit cartesischen Koordinaten arbeitet, kann der add_coordinate() Methode
bei Bedarf auch der Parameter "polar"
hinzugefügt werden:
```
coords.add_coordinate([1, 70, 60], polar=True)
```

Außerdem sind folgende Eigenschaften (Properties) verfügbar und können
bei Bedarf abgefragt werden, wobei in beiden Fällen ein Numpy Array zurückgegeben wird:

```
print(coords.coordinates)
print(coords.polar_coordinates)
```

Auch die Rotation der gegebenen Koordinaten ist möglich, wobei hier
das Format je nach Dimension der Koordinaten zu beachten ist.

```
rotated = coords.rotate(35) --> 2D Rotation (Gradmaß)
rotated = coords.rotate([0, 0, 60]) --> 3D Rotation (Gradmaß)
```

Sofern *coords.radians = True* gesetzt wurde, kann analog natürlich auch mit dem
Bogenmaß als Winkelangabe gearbeitet werden. Auch hier ist der Rückgabewert ein Numpy Array.