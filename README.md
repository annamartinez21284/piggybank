# Final Project CS50 CS50Web

Web Programming with Python and JavaScript

## Description

This is a simple Django-based application that interacts with Starling Bank's API (https://developer.starlingbank.com/docs).
Having set up a sandbox for this project with dummy customers and dummy data, the app allows you to select the customers and view their account details.
The endpoints used request (GET, PUT, DELETE) the customer details, such as the account balance or details of savings goals, but also manage access and refresh tokens.

## Usage

In order to run this app, it is necessary to set up a (free) developer account with Starling: https://developer.starlingbank.com/signup, and create a sandbox with dummy customers
for this app.


1. Create a Python virtual environment:
    ```
    python3 -mvenv <virtual_env>
    ```
2. Install module dependencies:
    ```
    pip3 install -r requirements.txt
    ```
3. Clone Github repo:
    ```
    git clone https://github.com/annamartinez21284/piggybank.git
    ```

4. Change into directory
    ```
    cd starling
    ```

5. Create a .env file containing your client ID and your client secret which you obtain from your Starling Sandbox, for example:
    ```
    CLIENT_ID = "12345"
    CLIENT_SECRET = "abcde"

    ```
    I have added this file to my .gitignore file.

6. In the Django shell,
    ```
    python manage.py shell
    ```

    you can then run the script in starling/db.py, replacing the customer specifics with your own.

7. Admins can make changes to the database (orders, menu, users) via the Django admin interface(http://ip-address:port/admin/).
   If no database cloned from my repo, set up a superuser:
    ```
    python manage.py createsuperuser
    ```

## Relevant files

The relevant files created for this project are:

* piggybank\static\starling\converter.js - handles minorUnits conversion to a currency amount
* piggybank\templates\starling\base.html - base template
* piggybank\templates\starling\index.html - landing page
* piggybank\templates\starling\show_details.html - page to view customer details, add/delete/view savings Goals, Balance, Name
* piggybank\helpers.py - contains refresh token helpers
* piggybank\models.py - Customer and Account models
* piggybank\urls.py - urls
* piggybank\views.py - main logic
* db.py - script to populate DB with customer data


## Limitations

This app covers mainly the 'happy case', i.e. has limited error handling and although short in code, required a large amount of set-up and learning authorisation, authentication, etc from my end.
The interface is basic, as I focused on the functionalities that I wanted to explore. Lastly, setting the app up yourself is cumbersome as it requires a Starling Bank Developer account creation.
Please refer to the video submitted with this app for a demo.
