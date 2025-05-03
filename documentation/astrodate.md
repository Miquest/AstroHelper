# astrodate.py
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
Verschiedene Aufrufe (dem oberen Beispiel folgend) sind möglich.

## Julianische Daten
Wahlweise kann hier das julianische Datum als Zahl eingegeben oder zum julianischen
Datum konvertiert werden. Die Abfrage des Wertes erfolgt im print Statement und kann
analog wie eine Variable verwendet werden.
```
new_date.from_julian(<julianisches_datum>)
new_date.to_julian()

print(new_date.julian_date)
```

## Addition und Subtraktion
Um das Handling von Daten so einfach wie möglich zu machen, kann man mit Pythons timedelta() auch
Zeitspannen subtrahieren. Möchte man das neue Datum (bzw. die entstehende Klasse) mit einer
neuen Variable referenzieren, ist dies auch möglich (unten).
```
new_date += timedelta(days=10)
new_date -= timedelta(days=20)

twenty_years_before = new_date - timedelta(years=20)
```
Mögliche Argumente für timedelta() sind: seconds, minutes, hours, days, months, years

## Werte abfragen
Bei Bedarf kann man die Werte der Klasse abfragen:
```
print(new_date)

julian_date_number = new_date.julian_date
```
Ersteres gibt die aktuellen Werte als String in die Konsole aus.
Letzteres kann wie eine Variable in Rechnungen verwendet werden. Es ist nicht nötig, den Wert erneut einer Variable
zuzuweisen, um damit rechnen zu können.

## Eigenes Datum beim Erstellen
Bei Bedarf kann auch von Anfang an ein anderes Datum gesetzt werden.
Dazu kann man der Klasse bei Erzeugung ein Datum im ISO8601 Format übergeben **(Format: Jahr-Monat-Tag T Stunde:Minute:Sekunde)**
Dies funktioniert wie folgt:

```
from astrodate import AstroDate
from datetime import datetime, timedelta

datum = "2024-04-22T12:12:05"
new_date = AstroDate(datum)
```
