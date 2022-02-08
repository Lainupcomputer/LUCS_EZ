# lucs_ez


## Modul : log

Modul bietet die Möglichkeit Log Daten als Datei abzulegen.
+ Zeitstempel + Log Nachricht

| Method   | parameter     | type | default  |
|----------|---------------|------|----------|
| __init__ | `destination` | "str" | "log.txt" |
| log      | `msg`         | "str" | "blanc"  |


## Modul : user

Modul bietet die Möglichkeit einer Benutzerverwaltung.
+ Benutzer Anlegen/Entfernen
+ Passwort abfrage 
+ Verschlüsselung 
+ Daten Felder hinzufügen

| Method   | parameter                | type             | default               |
|----------|--------------------------|------------------|-----------------------|
| __init__ | `destination`<br/> `debug` | "str" <br/> bool | "log.txt" <br/> False |


## Modul : config

Modul bietet die Möglichkeit Konfigurationen zu erstellen und zu laden.
+ Konfiguration auswählen
+ Daten speichern
+ Daten abrufen	

| Method   | parameter                                  | type             | default                     |
|----------|--------------------------------------------|------------------|-----------------------------|
| __init__ | `destination`<br/>`seperator`<br/> `debug` | "str" <br/>"str" <br/> bool | "log.txt" <br/>"#"<br/> False |


