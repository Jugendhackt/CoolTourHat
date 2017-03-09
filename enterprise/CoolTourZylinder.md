![Enterprise Zylinder](Colors.JPG)
##Hardware & Zubehör:
- Ein schöner Zylinder
- mindestens 3m ws2812b LED Stripes (144 LED pro Meter) ![Ebay](http://www.ebay.de/sch/i.html?_odkw=ws2812b&_osacat=0&_from=R40&_trksid=p2045573.m570.l1311.R5.TR12.TRC2.A0.H0.Xws2812b+.TRS0&_nkw=ws2812b+144&_sacat=0)
- Red Bear Lab BLE Nano
- Red Bear Programmer
- Dünne Kabel
- Ein Stück [Lochrasterplatte](https://cdn-reichelt.de/bilder/web/xxl_ws/C900/H25PR075.png)
- 1 ~500Ω Widerstand
- 1 [Kondensator](https://cdn.sparkfun.com//assets/parts/2/3/0/8/08982-03-L.jpg) (100µF- 1000µF)
- Akkupack für Smartphones
	- Maße sind am wichtigsten!
	- Idealerweiße klein und flach
	- mindestens 5000mAh (DC5V / 2A)
- Altes (kaputtes) USB Kabel (wird zerschnitten)

##Hilfreiches Werkzeug:
- Breadboard und Jumper Kabel [Ebay](http://www.ebay.de/itm/830-Kontakte-Steckboard-Steckbrett-Breadboard-mit-Jumper-Wire-Kabel-Set-/272102548188?hash=item3f5a9362dc:g:Tz8AAOSwYaFWeOx4)
- Lötkolben, Lötzinn
- Entlötlitze
- [Dritte Hand](https://img.conrad.de/medias/global/ce/5000_5999/5800/5880/5881/588124_LB_00_FB.EPS_1000.jpg)   
- [Seitenschneider](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Elektronikschere_%28smial%29.jpg/1024px-Elektronikschere_%28smial%29.jpg)
- [Heißklebepistole](http://i.ebayimg.com/images/g/AG4AAOSwvc9WFoqc/s-l300.jpg)
- sehr dünne Nadel (muss durch die Löcher im ws2812b Stripe passen)
- stabiles schwarzes Garn (wenn es sich leicht mit der Hand zerreißen lässt, ist es nicht stabil genug)

>Achtung: Dieses Projekt beinhaltet einige schwierige Lötstellen. Wenn du selbst wenig Erfahrung im Löten hast, suche dir für die schwierigeren Stellen Hilfe von einem Profi. Besuche zum Beispiel einen Hackspace in deiner Nähe.

##Schritt für Schritt
###1. Wie kommt der Code auf den Mikroprozessor?
####1.1 Beim online Compiler anmelden
Schließe den Red Bear Lab BLE Nano auf dem Programmer an einen USB-Port deines Computers an. Dieser erscheint als USB-Speichermedium in deinem Dateibrowser. Öffne die sich auf diesem befindende Datei „MBED.HTM“ mit deinem Browser. Du wirst nun auf die mbed.org Seite weitergeleitet. Falls du dies noch nicht getan hast, erstelle dir dort einen Account.
>Hinweis: Es ist technisch nicht erforderlich deine echte E-Mailadresse oder deinen echten Namen anzugeben, da vor Benutzung des Compilers keine E-Mailbestätigung stattfindet.

####1.2 Code importieren
Besuche das [CoolTourHat-Repository auf mbed.org](https://developer.mbed.org/users/pajowu/code/CoolTourHat/). Klicke in der „Repository toolbox“ auf „Import into Compiler“ und im aufgehenden Dialog auf „Import“.
####1.3 Interessen eintragen
Noch nicht implementiert
####1.4 Problemlösungstipps

###2. LED Stripes testen
Bevor die LED-Streifen verbaut werden, muss sichergestellt werden, dass sie auch einwandfrei funktionieren. Zum Aufbau des Tests eignen sich Breadboard und Jumperkabel.
####2.1 Stromquelle basteln
Um den Prozessor un die LEDs mit Strom versorgen zu können, kann man ein USB Kabel verwenden. Dieses wird durchgeschnitten, der Rote und der schwarze Draht wird abisoliert (grün und weiß werden nicht gebraucht). Dann die beiden Enden etwas verzinnen. 

####2.2 Anschließen

####2.3 Strandtest.ino ausführen
TODO
####2.4 Eventuell kaputte LEDs ausfindig machen


###3. LED Stripes zuschneiden & löten


###4. LED Stripes am Hut befestigen
TODO

###5. Platine Löten

