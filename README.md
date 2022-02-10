# Stripe Processor

## Installation

- Clone the repository
- Run the command `docker-compose up` to start the database container
- Enter the project directory `cd stripe_processor`
- Migrate the tables `python manage.py makemigrations`

## Usage
- Run the project `python manage.py runserver`
- Go to your browser and enter http://127.0.0.1:8000/api/charge/ to send a request
