# astrodate.py
Die astrodate.py Datei beinhaltet eine Klasse für das bequeme Handling
von gregorianischen und julianischen Daten. Man kann beispielsweise beide
Angaben ineinander umrechnen und Zeitunterschiede komfortabel addieren
oder subtrahieren.
Um die Klasse zu nutzen, müss sie zunächst wie gewohnt importiert werden. Die *datetime* Bibliothek
ist nicht erforderlich, aber es ist zu empfehlen, sie zu nutzen, da man sich das Leben so ungemein
einfacher machen kann.

```
from astrodate import AstroDate
from datetime import datetime, timedelta

new_date = AstroDate()
```

So wird die Klasse für das aktuelle Datum und die aktuelle Uhrzeit initiiert.
Im Folgenden werden alle mögliche Aufrufe von Methoden und Eigenschaften aufgelistet.
Um diese Klasse zu verwenden ist es empfehlenswert, sich mit
[Pythons Datetime Objekten](https://www.w3schools.com/python/python_datetime.asp) zu befassen.

## Julianische Daten
Hier kann man ein julianisches Datum als Zahlenwert nehmen und konvertieren,
so dass man sowohl das gregorianische Datum als auch einzelne Parameter (Stunde, Monat...) im Code
verwenden kann.
Die Abfrage des Wertes erfolgt im print Statement und kann analog wie eine Variable verwendet werden.
```
new_date.from_julian(<julianisches_datum>)
print(new_date.julian_date)
```

## Gregorianische Daten
Bei Bedarf kann der aktuelle Datumswert der Instanz auch geändert oder als String abgerufen werden werden.
Für Ersteres übergibt man wahlweise einen ISO8601 String (s. unten) oder ein Datetime Objekt:
```
new_date.date = datetime.now()
print(new_date.date)
```
Beim Setzen des Datums wird automatisch das entsprechende julianische Datum generiert, was über oben genannte
Eigenschaften abgefragt werden kann.

## Addition und Subtraktion von Zeitspannen
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
Einzelne Werte (Jahr, Monat, Stunde...) können auch dezidiert abgefragt werden, ohne sich direkt mit einem
langen String herumschlagen zu müssen:
```
print(new_date.year)
print(new_date.month)
print(new_date.day)

print(new_date.hours)
print(new_date.minutes)
print(new_date.seconds)
```
_Alle Rückgabewerte sind integer!_ Man kann diese also multiplizieren, addieren oder subtrahieren. Ein Setzen der einzelnen Werte ist nicht vorgesehen. Bei der nächsten Datumsänderung würden die Variablen in der Klasse überschrieben.

## Eigenes Datum beim Erstellen
Bei Bedarf kann auch von Anfang an ein anderes Datum gesetzt werden.
Dazu kann man der Klasse bei Erzeugung ein Datum im ISO8601 Format übergeben **(Format: Jahr-Monat-Tag T Stunde:Minute:Sekunde)**
Dies funktioniert wie folgt:

```
from astrodate import AstroDate

datum = "2024-04-22T12:12:05"
new_date = AstroDate(datum)
```

Alternativ ist auch eine Verwendung mit einem Datetime Objekt möglich:

```
from astrodate import AstroDate
from datetime import datetime, timedelta

datum = datetime(year=2000, month=12, day=12) --> 12.12.2000 um 00:00 Uhr
new_date = AstroDate(datum)
```
