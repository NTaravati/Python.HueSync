## Start en stop Hue bij Windows aan- en uitzetten
In deze repository vind je een script dat je Philips Hue lampen en start stekkers automatisch aan- en uitzet zodra jij je aan- en afmeldt op je Windows compoter. 

## Installatie
Voer de volgende stappen uit om het script in te richten.

<h4>Python voorbereiden</h4>
Installeer Python op je computer (bv. Chocolately > choco install python). Open CMD op je computer en voer het onderstaande command uit.

```
pip install phue
```

<h4>Hue Bridge koppelen met script</h4>
Druk op de fysieke Hue Bridge knop en open daarna hue_start.py. Hiermee koppel je de computer met de Hue Bridge. Vanaf dat moment kan je acties uitvoeren.

<h4>Startup toevoegen aan Windows</h4>
Kopieer het bestand hue_start.sh naar de onderstaande map:

```
%AppData%\Microsoft\Windows\Start Menu\Programs\Startup
```

Vervang de inhoud in het bestand met de locatie van Python; bijvoorbeeld:

``` 
@echo off
"C:\Program Files (x86)\Python37-32\python.exe" "C:\Program Dev\Apps\Python.HueSync\hue_start.sh"
```

Vanaf nu zal dit bestand iedere keer worden aangeroepen zodra je Windows aanzet. Het gevolg is dat de Python Hue Client een lokaal verzoek stuurt naar je Hue Bridge om de lampen uit het bestand hue_start.py in te schakelen.

<h4>Logoff toevoegen aan Windows</h4>
Om ervoor te zorgen dat de lampen weer uitschakelen bij het uitzetten van Windows, volg je de stappen uit de bijgeleverde video of deze handleiding: https://lifehacker.com/use-group-policy-editor-to-run-scripts-when-shutting-do-980849001. Selecteer het bestand hue_stop.sh tijdens het instellen van het programma.
