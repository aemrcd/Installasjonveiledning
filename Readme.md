# CONTENTS
- [Installer Ubuntu](##install-ubuntu-på-rasberry-pi)

- [Installer SSH ](#konfigurer-brannmuren-ved-hjelp-av-ufw-uncomplicated-firewall)

- [Installer Git,Python og Mariadb](#installer-git-python-og-mariadb)

- [Lage Databaser på MariaDB](#lag-ny-database-bruker-og-sett-riktige-rettigheter)

##  Install Ubuntu på Rasberry PI!!!
1. Sett SD korte på PC-en din
2. Last opp Rasberry Pi imager 
[Rasberry PI](https://www.raspberrypi.com/software/)
    - Trykk Download windows åpne filen 
    - Trykk på Rasberry PI Device og Velg Rasberry Pi 4
    - Trykk på Operating System og Velg other-general-purposes OS Velg det nyeste versjoner av Ubuntu
    - Velg din SD korte og Install 

<img src="https://assets.raspberrypi.com/static/4d26bd8bf3fa72e6c0c424f9aa7c32ea/d1b7c/imager.webp">

3. Sett SD korte på Rasberry Pi og installere alt som du trenger for eks

    ``For å åpne Terminalen trykk "CTRL + ALT + T" ``

    `  sudo apt update ` 

    - Skriv Passord

    `  sudo apt upgrade `

 - Det er ikke nødvendig, men det kan være nyttig å starte datamaskinen på nytt for å installere alt.


## Konfigurer brannmuren ved hjelp av UFW (Uncomplicated Firewall).

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

1. ``sudo apt install ufw`` (installerer UFW)
- Skriv Passord

2. ``sudo ufw enable`` (aktiverer brannmuren ved oppstart)``

3. ``sudo ufw allow ssh`` (tillater SSH-tilkoblinger gjennom brannmuren)``

4. Senere kan du sjekke statusen på brannmuren ved å skrive ``sudo ufw status``

## Skru på ssh

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

1. ``sudo apt install openssh-server`` (installerer SSH-serveren)

2. ``sudo systemctl enable ssh`` (gjør sånn at SSH skrur seg på ved oppstart)

3. ``sudo systemctl start ssh`` (starter SSH her og nå)

## Installer Git, Python og MariaDB

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``

`` Det er noe spørsmal at man må skrive Y/N ``

1. ``sudo apt install python3-pip``

2. ``sudo apt install git``

3. ``sudo apt install mariadb-server``

4. ``sudo mysql_secure_installation``

## LAG ny database-bruker og sett riktige rettigheter

``Åpne Terminalen trykk "CTRL + ALT + T" ``

``SKRIV DISSE ALLE KODER PÅ TERMINALEN``


1. Logg inn i MariaDB >

    - ``sudo mariadb –u root``

2. Lag ny bruker >

    - ``CREATE USER 'Lag din username'@'localhost' IDENTIFIED BY ' lag din password';``

3. Gi ny bruker rettigheter >

    - ``GRANT ALL PRIVILEGES ON *.* TO 'din username'@’localhost’ IDENTIFIED BY 'din password';``

4. Oppdater rettigheter

    - ``FLUSH PRIVILEGES;``


