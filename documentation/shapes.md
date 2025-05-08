# shapes.py

Diese Datei enthält Klassen für das Handling verschiedener
Formen.

## Ellipse

Diese Klasse muss wie gewohnt importiert und initiiert werden:
```
from shapes import Ellipse

ellipse = Ellipse(5, 3, radians=True)
```

So kann man eine Ellipse mit einer großen Halbachse von 5 und einer kleinen Halbachse von 3 initiieren.
Außerdem kann schon bei der Initiierung festgelegt werden, ob man im Gradmaß oder im Bogenmaß rechnen möchte.
Lässt man den Parameter weg, wird standardmäßig das Gradmaß verwendet.
Alle Parameter können auch im Nachhinein verändert werden:

```
ellipse.radians = False

ellipse.a = 6
ellipse.b = 4
```

Epsilon (die numerische Exzentrizität) wird sowohl bei der Initiierung als auch
bei der Veränderung der Maße der Ellipse automatisch neu kalkuliert.

Möchte man die exzentrische Anomalie für einen bestimmten Winkel herausfinden,
kann man das mit folgender Methode tun:
```
ea = ellipse.excentric_anomaly(120) --> Gradmaß
```
Analog dazu kann man, sofern aktiviert, natürlich auch das Bogenmaß als
Winkelangabe verwenden. Alle aktuellen Parameteter können folgendermaßen in die Konsole ausgegeben werden:
```
print(ellipse)
```