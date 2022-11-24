#Refera fullstack code challenge-backend

<h2>Requirements</h2>
Python (3.6, 3.7, 3.8, 3.9, 3.10)<br />
Django (2.2, 3.0, 3.1, 3.2, 4.0, 4.1)

<h2>Development</h2> 
Create the virtual environment and activate it 

For Windows:
```
pip install virtualenv
virtualenv -p python3 venv
venv\Scripts\activate
```
For Linux:
```
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```
After activating
```
pip install -r requirements.txt
```
To run the server:
```
python manage.py runserver
```

<h6>Describe how you would implement an authentication layer for the web application.<h6/>
Djangorestframework have token authentication using rest_framework.authtoken on your INSTALLED_APP and TokenAuthentication <br />
to REST_FRAMEWORK, migrate will create the table that will store the tokens so is needed to create a user account with <br />
python manage.py createsuperuser --username felipe--email felipe@example.com <br />
python manage.py drf_create_token felipe <br />
now u can use your token with the API request <br />
http://127.0.0.1:8000/API 'Authorization: Token ashu1uhi23hui1uashiuhi'
