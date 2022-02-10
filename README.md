# lucs_ez


## Modul : log

Modul bietet die Möglichkeit Log Daten als Datei abzulegen.
+ Zeitstempel + Log Nachricht

| Method   | parameter                | type            | default            |
|----------|--------------------------|-----------------|--------------------|
| __init__ | `destination`<br/> ´new´ | "str"<br/> bool | "log.txt"<br/>True |
| log      | `msg`                    | "str"           | "blanc"            |


## Modul : user

Modul bietet die Möglichkeit einer Benutzerverwaltung.
+ Benutzer Anlegen/Entfernen
+ Passwort abfrage 
+ Verschlüsselung 
+ Daten Felder hinzufügen

|           | parameter                | type             | default               |
|-----------|--------------------------|------------------|-----------------------|
| __init__ | `destination`<br/> `debug` | "str" <br/> bool | "log.txt" <br/> False |

| Method                   | parameter                        | type            | default / usage                                                                    |
|--------------------------|----------------------------------|-----------------|------------------------------------------------------------------------------------|
| __check_if_user_exists__ | `user_name`                      | "str"           | return user ID                                                                     |
| __create_user__          | `user_name`<br/> `user_password` | "str"<br/>"str" | create User <br/> return True on creation                                          |
| __delete_user__          | `user_name`<br/> `user_password` | "str"<br/>"str" | delete User <br/> return:<br/> 200=OK,<br/> 401=password_wrong,<br/> 404=not found |



## Modul : config

Modul bietet die Möglichkeit Konfigurationen zu erstellen und zu laden.
+ Konfiguration auswählen
+ Daten speichern
+ Daten abrufen	

| Method   | parameter                                  | type             | default                     |
|----------|--------------------------------------------|------------------|-----------------------------|
| __init__ | `destination`<br/>`seperator`<br/> `debug` | "str" <br/>"str" <br/> bool | "log.txt" <br/>"#"<br/> False |


