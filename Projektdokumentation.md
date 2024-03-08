
# Projekt-Dokumentation



Filip Mitrovic, Lennard Bühler, Filip Kritzner und Raul Gilardoni

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|   19.01.2024   | 0.0.1   | Wir haben in der Gruppe ein Thema ausgesucht für dieses Projekt  |
|  26.01.2024     |   0.0.2      |        Wir haben mit youtube tutorials den einstieg gemacht und den ganzen Tag daran gearbeitet das der Bot Instagramm startet, sich selbst einlogt und auf die Chats geht                |
|   02.02.2024   | 0.0.3   | Wir haben den ganzen Tag unseren Bot weiter programmiert und uns mit dem Thema im Internet befasst  |

## 1 Informieren

### 1.1 Ihr Projekt
In diesem Projekt entwickeln wir einen Instagram Bot mit der Programmiersprache Python. Dieser Bot kann selbstständig mit Leuten Chaten.




### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    |       Kann         |   Optional   | Als User möchte ich, dass der Bot mit einer AI verbunden ist um mit einer Person Chaten zu können   |
| 2    |       muss         |   funktional   |  Als User möchte ich, dass sich der Bot selbstständig im Account einloggen kann.  |
| 3    |       muss         |   funktional   |Als User möchte ich mit dem Bot chatten können.  |
| 4    |       kann         |   Qualität   | Als User möchte ich, dass der Bot Leuten Folgen kann   |
| 5    |       kann        |   funktional   |  Als User möchte ich, dass der Bot Bilder von anderen Instagram Users liken kann.  |
| 6    |       muss         |   funktional   |Als User möchte ich, dass der Bot selbst auf die Instagramm Webseite geht   |
| 7    |       muss         |   funktional   |Als User möchte ich, dass der Bot einer Person eine Nachricht senden kann    |
| 8    |       muss         |   funktional   | Als User möchte ich, dass ich die Nachricht die der Bot der Person auf Instagram anpassen kann   |







### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  |        Programm wird gestartet    |  Keine     |     Bot loggt sich im Instagram Account ein.          |
| 2.1  |     Programm wird gestartet        |  User schickt Nachricht ab    |     Bot antwortet entsprechend der Nachricht vom User.          |
| 3.1  |       Programm wird gestartet        |  Cookies werden vorgeschlagen    |     Bot akzeptiert Cookies.        |
| 4.1  |       Programm wird gestartet        | Startseite wird gezeigt     |  Der Bot geht auf die Nachrichten Option            |
| 5.1  |      Programm wird gestartet       | Die Personen denen man schreiben kann werden angezigt     |  Die gewünste Person wird ausgewählt           |
| 6.1  |       Programm wird gestartet        | Der Chat zwischen dem Bot und der anderen Person wird angezeigt    |  Die schreiben Funktion wird vom Bot ausgewählt          |
| 7.1  |       Programm wird gestartet       | Der Chat zwischen dem Bot und der anderen Person wird angezeigt     | Eine Nachricht wird vom Bot geschrieben             |
| 8.1  |      Programm wird gestartet       |   Der Chat zwischen dem Bot und der anderen Person wird angezeigt       |   Nachricht wird vom Bot gesendet            |
| 9.1  |       Programm wird gestartet       |   User schickt Nachricht ab   |     Chatbot liest Nachricht        |
| 10.1  |      Programm wird gestartet       |   Nachricht vom User wurde vom Bot gelesen    |  Chatbot gibt eine Antwort          |
| 11.1  |       Chatbot stellt die Frage wie viele Nachrichten der Bot ausgeben soll.      |  User gibt Zahl ein   |     Bot gibt entsprechend viele Nachrichten aus wie viele der Benutzer wollte.        |
| 12.1  |        Programm wird läuft   |   Nachrichten an Bot schreiben die er ausgeben soll    |     Bot gibt entsprechende Nachrichten aus.         |





### 1.4 Diagramme

![image](https://github.com/Mitro57vic/Instagram-Bot/assets/110892649/edd7a446-e88e-4f48-a738-037a62fea258)




## 2 Planen
Arbeitspakete:

| AP-№ | Zuständig | Beschreibung | geplante Zeit (min) |
| ---- |  --------- | ------------ | ------------- |
| 1.A  |   Filip Mitrovic              |   Einrichten des Instagram-Login-Prozesses im Chatbot-Programm, um sicherzustellen, dass der Bot sich erfolgreich in den Instagram-Account einloggen kann.  |   60 |
| 2.A  |   Lennard Bühler              |   Implementierung einer Funktion im Chatbot, um auf eingehende Nachrichten von Benutzern zu reagieren und entsprechende Antworten zu generieren.   |   90 |
| 3.A  |   Filip Kritzner            |   Integration einer Cookie-Akzeptanzfunktion, um sicherzustellen, dass der Bot vorgeschlagene Cookies akzeptieren kann, wenn sie angeboten werden.    |   30 |
| 4.A  |   Filip Mitrovic              |   Programmierung des Chatbot-Verhaltens, um nach dem Start auf die Startseite zu navigieren und die Nachrichtenoption zu wählen.   |   45 |
| 5.A  |   Filip Kritzner              |   Implementierung der Funktion, um die Liste der verfügbaren Personen anzuzeigen, denen der Bot schreiben kann, und Auswahl der gewünschten Person durch den Benutzer.   |   60 |
| 6.A  |   Raul Gilardoni              |   Entwicklung der Funktion, um den Chatverlauf zwischen dem Bot und der ausgewählten Person anzuzeigen und die Schreibfunktion zu aktivieren.   |   45 |
| 7.A  |   Filip Mitrovic              |   Programmierung des Bot, um eine Nachricht an die ausgewählte Person zu senden, basierend auf dem angezeigten Chatverlauf.   |   45 |
| 8.A  |   Lennard Bühler              |   Sicherstellen, dass der Bot Nachrichten an die ausgewählte Person senden kann, indem er die gesendeten Nachrichten im Chatverlauf anzeigt.   |   45 |
| 9.A  |   Raul Gilardoni              |   Implementierung einer Funktion, um eingehende Nachrichten von Benutzern zu erfassen und vom Chatbot zu lesen.   |   60 |
| 10.A |   Lennard Bühler              |   Entwickeln einer Antwortfunktion im Chatbot, um auf gelesene Nachrichten zu reagieren und entsprechende Antworten zu generieren.   |   60 |
| 11.A |   Raul Gilardoni             |   Programmierung des Chatbots, um eine Frage nach der Anzahl der Nachrichten zu stellen, die ausgegeben werden sollen, und die vom Benutzer angegebene Anzahl zu berücksichtigen.   |   60 |
| 12.A |   Filip Kritzner              |   Implementierung einer Funktion im Chatbot, um Nachrichten auszugeben, die vom Benutzer angefordert wurden, basierend auf der Eingabe des Benutzers.   |   60 |





## 3 Entscheiden

Wir haben uns für die geplanten Arbeitspakete entschieden.

## 4 Realisieren

| AP-№ | Datum      | Zuständig       | Beschreibung | geplante Zeit (min) | tatsächliche Zeit (min) |
| ---- | ----------| --------------- | ------------- | ----------------- | ----------------------- |
| 1.A  | 19.01.2024 | Filip Mitrovic  | Einrichten des Instagram-Login-Prozesses im Chatbot-Programm, um sicherzustellen, dass der Bot sich erfolgreich in den Instagram-Account einloggen kann. | 60 | 70 |
| 2.A  | 19.01.2024 | Lennard Bühler  | Implementierung einer Funktion im Chatbot, um auf eingehende Nachrichten von Benutzern zu reagieren und entsprechende Antworten zu generieren. | 90 | 80 |
| 3.A  | 19.01.2024 | Filip Kritzner  | Integration einer Cookie-Akzeptanzfunktion, um sicherzustellen, dass der Bot vorgeschlagene Cookies akzeptieren kann, wenn sie angeboten werden. | 30 | 40 |
| 4.A  | 19.01.2024 | Filip Mitrovic  | Programmierung des Chatbot-Verhaltens, um nach dem Start auf die Startseite zu navigieren und die Nachrichtenoption zu wählen. | 45 | 50 |
| 5.A  | 02.02.2024 | Filip Kritzner  | Implementierung der Funktion, um die Liste der verfügbaren Personen anzuzeigen, denen der Bot schreiben kann, und Auswahl der gewünschten Person durch den Benutzer. | 60 | 55 |
| 6.A  | 02.02.2024 | Raul Gilardoni  | Entwicklung der Funktion, um den Chatverlauf zwischen dem Bot und der ausgewählten Person anzuzeigen und die Schreibfunktion zu aktivieren. | 45 | 60 |
| 7.A  | 02.02.2024 | Filip Mitrovic  | Programmierung des Bot, um eine Nachricht an die ausgewählte Person zu senden, basierend auf dem angezeigten Chatverlauf. | 45 | 45 |
| 8.A  | 02.02.2024 | Lennard Bühler  | Sicherstellen, dass der Bot Nachrichten an die ausgewählte Person senden kann, indem er die gesendeten Nachrichten im Chatverlauf anzeigt. | 45 | 50 |
| 9.A  | 23.02.2024 | Raul Gilardoni  | Implementierung einer Funktion, um eingehende Nachrichten von Benutzern zu erfassen und vom Chatbot zu lesen. | 60 | 70 |
| 10.A | 02.02.2024 | Lennard Bühler  | Entwickeln einer Antwortfunktion im Chatbot, um auf gelesene Nachrichten zu reagieren und entsprechende Antworten zu generieren. | 60 | 65 |
| 11.A | 23.02.2024 | Raul Gilardoni  | Programmierung des Chatbots, um eine Frage nach der Anzahl der Nachrichten zu stellen, die ausgegeben werden sollen, und die vom Benutzer angegebene Anzahl zu berücksichtigen. | 60 | 60 |
| 12.A | 19.01.2024 | Filip Kritzner  | Implementierung einer Funktion im Chatbot, um Nachrichten auszugeben, die vom Benutzer angefordert wurden, basierend auf der Eingabe des Benutzers. | 60 | 60 |




## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum    | Resultat        | Tester         | Laptop                 |
| ---- | -------- | --------------- | -------------- | ---------------------- |
| 1.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 2.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 3.1  | 23.02.24 | Funktioniert    | Kritzner       | Acer Windows 11        |
| 4.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 5.1  | 23.02.24 | Funktioniert    | Kritzner       | Acer Windows 11        |
| 6.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 7.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 8.1  | 23.02.24 | Funktioniert    | Kritzner       | Acer Windows 11        |
| 9.1  | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 10.1 | 23.02.24 | Funktioniert   | Kritzner       | Acer Windows 11        |
| 11.1 | 23.02.24 | Funktioniert    | Mitrovic       | HP Spectre Windows 11  |
| 12.1 | 23.02.24 | Funktioniert nicht    | Kritzner       | Acer Windows 11        |



`Fazit:`
Das Projekt hat gezeigt, dass die Entwicklung eines Instagram-Bots, der grundlegende Funktionen wie das Einloggen, das Senden und Beantworten von Nachrichten sowie das Akzeptieren von Cookies ausführen kann, machbar ist. Jedoch stellte die Integration einer Künstlichen Intelligenz eine bedeutende Herausforderung dar, die wir in diesem Rahmen nicht bewältigen konnten. 

Die Erfahrung, im Team zu arbeiten, war insgesamt positiv und förderte den Austausch von Wissen und Fähigkeiten. die Temmitglieder hätten alle aber Homeoffice präferiert.

Abschließend lässt sich sagen, dass das Projekt wertvolle Einblicke in die Entwicklung von Bots und die Arbeit im Team geliefert hat. 







## 6 Auswerten
Reflexion bei unseren Portfolios.

