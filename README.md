# AstroHelper
Dieses Repository beinhaltet einige hilfreiche Dateien
für die Arbeit des Astro NWT Kurses des Otto-Hahn-Gymnasiums in Göttingen.
Das Repository wird nicht aktiv maintained!

## astrodate.py
Die astrodate.py Datei beinhaltet einige Funktionen für das bequeme Handling
von gregorianischen und julianischen Daten. Man kann beispielsweise beide 
Angaben ineinander umrechnen und Zeitunterschiede komfortabel addieren
oder subtrahieren. 
Genutzt wird das Programm wie folgt:

```
from astrodate import AstroDate
from datetime import datetime, timedelta

new_date = AstroDate()
```

So wird die Klasse für das aktuelle Datum und die aktuelle Uhrzeit initiiert. 
Verschiedene Aufrufe (dem oberen Beispiel folgend) sind möglich:

```
new_date.from_julian(<julianisches_datum>) --> Datum als Zahl übergeben
julian_date = new_date.to_julian() --> Speichert das julianische Datum für die gegebene Zeit in der Variable

new_date += timedelta(days=10) --> Addiert 10 Tage zum Datum hinzu. Analog funktioniert dies auch für Monate (months), Jahre (years)...
new_date -= timedelta(days=20) --> Subtrahiert 20 Tage

print(new_date) --> gibt gespeichertes Datum in gregorianischer und julianischer Form zurück

julian_date_number = new_date.julian_date --> Eigenschaft der Klasse mit julianischem Datum abfragen
```
Letzteres kann wie eine Variable in Rechnungen verwendet werden. Es ist nicht nötig, den Wert erneut einer Variable
zuzuweisen, um damit rechnen zu können.

Bei Bedarf kann auch von Anfang an ein anderes Datum gesetzt werden.
Dazu kann man der Klasse bei Erzeugung ein Datum im ISO8601 Format übergeben **(Format: Jahr-Monat-Tag T Stunde:Minute:Sekunde)**
Dies funktioniert wie folgt:

```
from astrodate import AstroDate
from datetime import datetime, timedelta

datum = "2024-04-22T12:12:05"
new_date = AstroDate(datum)
```
