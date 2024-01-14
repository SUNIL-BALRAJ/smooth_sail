# SmoothSail
## Problem Statement Title: Frequent dislodgement of belt conveyor along hilly terrain for various reasons
The primary objective is to develop an innovative and efficient solution to mitigate the frequent dislodgement of belt conveyors along hilly terrain. The proposed solution addresses the various reasons causing dislodgement, ensuring the continuous and reliable operation of the belt conveyor system in challenging topographical conditions. The aim is to enhance the stability, safety, and overall performance of the conveyor system, ultimately leading to increased productivity and reduced downtime in the specified hilly terrain environment.

In our approach, two types of predictive models will be used:
## MODULE 1 : Prediction based on past data.
LSTM, a neural network architecture, excels in capturing temporal patterns and dependencies to understand the dynamic changes in the ropes and belt's condition over time.
## MODULE 2: Prediction from live data. 
Random Forest, a machine learning model, adeptly handles non-linear relationships and intricate interactions, enabling accurate predictions of pulley wear and tear by modeling the impact of environmental variables (e.g., temperature, load, humidity, and operational hours).

<br />

## Pages
![Smooth Sail - Home Page](https://github.com/SUNIL-BALRAJ/smooth_sail/blob/main/app_images/page1.jpg)
![Smooth Sail - Failure Prediction Page](https://github.com/SUNIL-BALRAJ/smooth_sail/blob/main/app_images/page2.jpg)
![Smooth Sail - Live data Page](https://github.com/SUNIL-BALRAJ/smooth_sail/blob/main/app_images/page3.jpg)
![Smooth Sail - Live Prediction Page](https://github.com/SUNIL-BALRAJ/smooth_sail/blob/main/app_images/page4.jpg)

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/SUNIL-BALRAJ/smooth_sail.git
$ cd django-black-dashboard
```
or you can simply download the project
<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
>  You can also install requirements without creating a virtual Enviroment too. Just navigate to the project folder and 

```bash
$ pip install -r requirements.txt
```
<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser for admin operations

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py    # Project Configuration  
   |    |-- urls.py        # Project Routing
   |
   |-- home/
   |    |-- views.py       # APP Views 
   |    |-- urls.py        # APP Routing
   |    |-- models.py      # APP Models 
   |    |-- tests.py       # Tests  
   |
   |-- requirements.txt    # Project Dependencies
   |
   |-- env.sample          # ENV Configuration (default values)
   |-- manage.py           # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />
