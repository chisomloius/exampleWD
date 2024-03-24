Steps to Follow:
- create a virtual env: ` python -m preferred-env-name`
- activate virtual env: `python -m preferred-env-name/Scripts/activate`
- install dependencies: `pip install django`
- get env pip list in a file: `pip freeze > requirements.txt`
- create django main project: `django-admin startproject projectName`
- navigate to app: `cd /projectName`
- start python server: `python manage.py runserver`
- start component of your app: `django-admin startapp preferredComponentName`
- update changes done on your apps or main django project: `python manage.py migrate`
- create superuser on your app: `python manage.py createsuperuser`
    + username: chisomloius
    + email: chisanloius@gmail.com
    + password: testMyCRMApp

- create add a path on your urls.py to the main projectName
- create add a path on your urls.py to preferredComponentName App
    + add a the url path to the urls.py file from the views.py created on the app
    + start adding a functions, ladning pages on the views.py

- set up static files/folder
    + naviagte to the projectName folder and create a static folder
    + add as many subfolders under the files as you want

-

- create your app level templates under the prefferedComponentNameApp
    + add a folder called templates
    + under the templates folder add another folder called the prefferedComponentNameApp
    + add files like index.html under the prefferedComponentNameApp 

- create the app blueprint:
    + create the inherited base file: base.html, navbar.html
    + create the necessaries set-up templates
    + add the views by creating the necessary functions
    + add the different libraries been used to the settings 
    + start building the models on models.py
    + add the migrations by running `python manage.py makemigrations`
    + add the migrations to SQL DB by running `python manage.py migrate`
    + add crispy forms
    + add django messages
    +



- test cases
    + username1: dragonfire
    + password1: NaijainTinubutimes
    + username1: dragonfire2
    + password1: NaijainTinubutimes
    