# humanAPI
## Introduction
The task is to create a simple RESTful Flask application that takes data from a database and a script that will fetch data from an external API and fills the database. All the code should be written on Python and packed into a docker-compose (database + flask app).
After task completion, you should write an article about the task.

### Part 1. ETL script
The script written on Python should load 100 random users with Male gender from Random User Generator and save them to a database (for this purpose you may select the database of your choice).

### Part 2. Flask RESTful API 
The Flask app should work with data loaded with the previous script and support operations:
List all data from a collection
Get one specified entity
Delete one specified entity

### Part 3. Docker-compose configuration
The flask app should be packed into docker-compose and available for the external world (you can access the flask app from your local PC). It should take data from a database, deployed on the second container. The ETL script should be run on the container start.  
