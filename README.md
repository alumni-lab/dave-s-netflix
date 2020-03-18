# Dave's Netflix

## Setup Instructions

### Prerequesites: 

You will need the following installed on your machine:
- Python 3
- Pip
- Node
- Yarn

### Steps:

- Clone the repository
- If necessary, install pipenv:
  ```
  $ pip install pipenv
  ```
- Install the dependencies from the Pipfile:
  ```
  $ pipenv install
  ```
- Run the virtual environement:
  ```
  $ pipenv shell
  ```
- Navigate to the backend folder:
  ```
  $ cd backend/
  ```
- Run the migrations:
  ```
  $ python manage.py migrate
  ```
- Seed the database:
  ```
  $ python manage.py seed daves_netflix --number=15
  ```
- Launch the server:
  ```
  $ python manage.py runserver
  ```
- On a different terminal, navigate to the frontend folder:
  ```
  $ cd frontend/
  ```
- Install the front end dependencies:
    ```
  $ yarn install
  ```
- Run the React server:
  ```
  $ yarn start
  ```
- To access the site, navigate to http://localhost:3000
- To access the django admin site, navigate to http://localhost:8000/admin
- To access the REST framework API, navigate to http://localhost:8000/api

The REST Framework API provides a clear map of all the endpoints and what they return
