# Features

- Verarbeiten der Datenpackete mithilfe von nfstream und tcpdump als cronjob - die Daten werden täglich gespeichert
- Speichert man den Client Schlüssel in der Umgebungsvariable oder in der Datenbank??? 
- Jeder Benutzer bekommt eine Umgebungsvariable mit dem Verzeichnis wo der Schlüssel sich befindet
- optional: sha256 hashing + pepper?? (salt schon vorhanden) für die Website flask werkzeug-security
- nlp modul was die dns queries klassifizieren wird (Social Media, Shopping Seiten, Blogs, Entertainment etc....)
- wenn man alle ip adressen erlauben möchte muss man bei AllowedIPs: 0.0.0.0/0 eingeben
- Die Daten die geloggt wurden, werden danach mit matplotlib visualisiert
- certbot https zertifikat erstellen und mit cronjob aktualisieren
- dyndns cronjob erstellen 

