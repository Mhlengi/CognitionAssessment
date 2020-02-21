# Cognition Assessment

[Logical Skills Test : Answers](https://github.com/Mhlengi/CognitionAssessment/blob/master/LogicalSkillsTestAnswer.md)

[Cognition Assessment Live Heroku Application](https://cognition-assessment.herokuapp.com/)

## Requirements
- Python 3.7+
- PostgreSQL 9.6+

Please consult Google if you need to install any of the pre-requisites

## Installation
- Clone/Download the git repo - `https://github.com/Mhlengi/CognitionAssessment.git`.
- Create a Postgres database `cognition_assessment` with user `postgres` and password `password`
- Navigate to the project folder`cognition-assessment`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`
- Run the database migrations `python manage.py migrate`
- Run collect static files `python manage.py collectstatic`
- Start the WebServer `python manage.py runserver`
(*Please note everytime you pull from master you may need to run the migrations and install any new dependencies
- as per the above instructions*)

### Running django pytest
`py.test -xvv --create-db`.

### Running django pytest with code-coverage report
`coverage run -m py.test -xvv --create-db; coverage html; coverage report;`

### Test Localhost Browser Application
- Access [localhost application](http://localhost:8000) on your browser.

### Test Heroku Live Browser Application
- Access heroku application [https://cognition-assessment.herokuapp.com/](https://cognition-assessment.herokuapp.com/) on your browser.

### Application Endpoints
```
Other applicaiton endpoints and usage
```
### Step 0: 
- On your terminal command create a super user ot access Django admin interface.  
```
python manage.py createsuperuser
```

### Step 1:
- Create/Register a normal system-user or super-user.
- Link: [https://cognition-assessment.herokuapp.com/signup/](https://cognition-assessment.herokuapp.com/signup/)

### Step 2:
- Basic user profile update.
- Link: [https://cognition-assessment.herokuapp.com/user_profile/](https://cognition-assessment.herokuapp.com/user_profile/)

### Step 3:
- Login and Logout pages.
- Login Link: [https://cognition-assessment.herokuapp.com/login/](https://cognition-assessment.herokuapp.com/login/) 
- Logout Link: [https://cognition-assessment.herokuapp.com/logout/](https://cognition-assessment.herokuapp.com/logout/)

### Step 4
- Home page with all current log tickets.
- Link: [https://cognition-assessment.herokuapp.com/](https://cognition-assessment.herokuapp.com/)

### Step 5
- Dashboard with summary of stats insight application. 
- Link: [https://cognition-assessment.herokuapp.com/dashboard/](https://cognition-assessment.herokuapp.com/dashboard/)

`Docs Continue....`
