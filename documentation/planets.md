# planets.py

Um die Änderungsraten von Planeten bequem handeln zu können, existiert
eine weitere Datei in diesem Repository.
*Wichtig* ist, dass man zur Nutzung einige weitere Dateien im selben
Verzeichnis ablegen muss:

- astrodate.py
- orbital_elements.py
- orbital_elements.json

Um die Klasse zu nutzen, benötigt man sowohl die Klasse selbst als auch Pythons __datetime__ Bibliothek [s. Einführung](introduction.md):

```
from planets import Planets
from datetime import datetime

observation_time = datetime(year=2025, month=2, day=6)
track_elements = Planets(time=observation_date, radians=True)
```

Durch diese Befehle kann man die Klasse *Planets* so initiieren, dass man die
Bahnlageelemente eines der verfügbaren Planeten am 06.02.2025 auslesen
kann. Dabei werden alle Winkelangaben im Gradmaß gemacht (da __radians=True__).
Beide Parameter sind optional. Lässt man den __time__ Parameter aus, wird die aktuelle Systemzeit als Observationszeitpunkt verwendet.
Ohne den __radians__ Parameter verwendet das Programm das Gradmaß als Rückgabewert.

## Auslesen der Bahnlageelemente
Hat man den Observationszeitpunkt festgelegt, kann man die Bahnlageelemente
der einzelnen Planeten zum gegebenen Zeitpunkt bequem auslesen.
Ist man sich unsicher, welche Planeten zur Verfügung stehen, kann man sich eine Liste/einen Array mit den verfügbaren Planeten ausgeben lassen:

```
print(track_elements.planet_list)
```

Um dann letztendlich den Planeten festzulegen und die Elemente abzurufen, kann folgender Code verwendet werden:

```
track_elements.planet = "Mars"

e = track_elements.excentricity
a = track_elements.major_axis
i = track_elements.inlcination
bigOmega = track_elements.ascending_node
omega = track_elements.arg_of_perihelon)
M = track_elements.mean_anomaly
```

Die Zuweisungen zu Variablen sind hier in der Praxis __nicht nötig__, die
Eigenschaften (Properties) können analog wie Variablen verwendet werden.
Die Werte der hier definierten Variablen sind in folgenden Einheiten gespeichert:
- __e__ --> Zahl
- __a__ --> AU (Astronomische Einheit bzw. Astronomical Unit)
- __i__ --> Grad / Bogenmaß
- __bigOmega__ --> Grad / Bogenmaß
- __omega__ --> Grad / Bogenmaß
- __M__ --> Grad / Bogenmaß
