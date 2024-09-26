#  Install Ubuntu på Rasberry PI!!!

1. Sett SD korte på PC-en din
2. Last opp Rasberry Pi imager 
[Rasberry PI](https://www.raspberrypi.com/software/)
    - Velg Rasberry Pi 4
    - velg other-general-purposes OS
    - Velg det nyeste versjoner av Ubuntu
    - Velg din SD korte og Install 

<img src="https://assets.raspberrypi.com/static/4d26bd8bf3fa72e6c0c424f9aa7c32ea/d1b7c/imager.webp">

3. Sett SD korte på Rasberry Pi og installere alt som du trenger for eks

    ``For å åpne Terminalen trykk "CTRL + ALT + T" ``

    `  sudo apt update ` 

    `  sudo apt upgrade `

 - Det er ikke nødvendig, men det kan være nyttig å starte datamaskinen på nytt for å installere alt.


## Konfigurer brannmuren ved hjelp av UFW (Uncomplicated Firewall).

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

1. ``sudo apt install ufw`` (installerer UFW)

2. ``sudo ufw enable`` (aktiverer brannmuren ved oppstart)``

3. ``sudo ufw allow ssh`` (tillater SSH-tilkoblinger gjennom brannmuren)``

4. Senere kan du sjekke statusen på brannmuren ved å skrive ``sudo ufw status``

## Skru på ssh

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

1. ``sudo apt install openssh-server`` (installerer SSH-serveren)

2. ``sudo systemctl enable ssh`` (gjør sånn at SSH skrur seg på ved oppstart)

c. sudo systemctl start ssh (starter SSH her og nå)
## Installer Git, Python og MariaDB

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

1. ``sudo apt install python3-pip``

2. ``sudo apt install git``

3. ``sudo apt install mariadb-server``

4. ``sudo mysql_secure_installation``

