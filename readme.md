![epic_event_logo](https://user-images.githubusercontent.com/85108007/168476703-f820738c-6da3-4ab0-a0b0-c3c2db7e3ed9.png)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# **Epic Event V1.0.0** : CRM API

EECRM est une API qui falicitera la gestion de vos clients ! Il vous sera possible de gérer leurs contracts et événements en toute simplicité !

## Technologies :
- Python
- Django REST
- Django JWT / Simple JWT

## **Initialisation de l'environnement**

### 1. Télécharger la branche Main vers un répertoire local

- Pour Télécharger, cliquez sur le bouton vert "Code" puis "Download ZIP"

- Créer un dossier sur votre ordinateur pour y disposer les fichiers présents sous GitHub

- Ouvrir un terminal (Ex: Windows PowerShell) et se positionner dans le dossier en question avec la commande cd, par exemple:

```
cd d:
cd -- "D:\mon_dossier"
```

### 2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- Créer l'environnement:


`python -m venv env`

- Activer l'environnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:

    `env/Scripts/Activate.ps1` 

    - Inux et MacOS:  

    `source env/bin/activate`

- Installer les librairies : 

`pip install -r requirements.txt`

### 3. Installer PostGreSQL

Téléchargement : 
- [Download PostGreSQL](https://www.postgresql.org/download/)

Installation :
- Windows : [Install PostgreSQL on Windows](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/)
- MacOS : [Install PostgreSQL macOS](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-macos/)
- Linux : [Install PostgreSQL Linux](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-linux/)

⚠️ Retenez bien le mot de passe lors de l'installation

Sous SQL Shell:
- server [localhost] : faire ENTRER
- Database [postgres]: faire ENTRER
- Port [5432] : faire ENTRER
- Username [postgres]: faire ENTRER
- Mot de passe pour l'utilisateur postgres : Entrez le mot de passe que vous avez saisi lors de l'installation
- saisir et valider pour chaque ligne :
```
  - CREATE DATABASE epic_event;
  - CREATE USER epicevent_admin WITH ENCRYPTED PASSWORD 'openclassrooms00';
  - GRANT ALL PRIVILEGES ON DATABASE epic_event TO epicevent_admin;
```
Dans le cas où le nom de la database ou celui de l'utilisateur sont différents de ceux ci-dessus, veillez à modifier les paramètres dans `epicevent/settings.py` dans la variable `DATABASE`.

## **Lancement du projet**

### 1. Lancer le serveur Django sous l'environnement virtuel, dans le terminal:

Se positionner dans l'application LITReview:

`cd epicevent`

Lancer le serveur :
```
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Lors de la création d'un super user, la console vous demandera les paramètres suivants:
- Username : votre nom d'utilisateur
- Role : MANAGER
- Password : votre mot de passe

Utiliser le username pour se connecter au panel d'administration [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

### 2. Fonctionnalités de l'API:
L'application vous propose les fonctionnalités suivantes :
- Créer des utilisateurs suivant 3 profiles : MANAGER, SALES, SUPPORT
- suivant le profile de l'utilisateur connecté, il pourra :
  - Des clients
  - Des contrats
  - Des évènements
 
 Pour plus de détails :
 [Exigences fonctionnalités](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python+FR/P10+-+BDD/CRM+-+Exigences+fonctionnelles.pdf)
 
 ## Postman:
 
 Lien vers la documentation postman : [Documentation](https://documenter.getpostman.com/view/18469824/Uyxoh44Y)
    
