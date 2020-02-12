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
