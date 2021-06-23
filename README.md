# QA_Project_1 ZMR

## Table of contents:
- What this project is
- Scope of the project
- Design specification

## What this project is
This project will be a way for you to upload reviews about your favorite movies!
This is a web based application running with flask / python intergrating a cloud database.
There will be no login system and anyone can leave a review on a movie, reviews can be
liked and the most liked reviews will appear closer to the top of the list. It is down
to the site owner to update the movie titles but , again, anyone can submit a review!

## Scope of the projects
There are a few basic requirements this project must hit, they are as followed:
    
- At least two databases, in this case two with a relationship
- A HTML front end, a base layout will be used and a navigation bar will be used
- WTForms to allow user input
- Self testing python to be run during each build
- Archiving of tests to allow backtracing

## Design specification
There isnt a need for a fancy website frontend, however, it would still be nice for it to 
look easy to navigate and intuitive. The most that will be used will be CSS. One of the main
focus's of the project will be the backend python code. It is very important that it is structured and that it follows a base file tree. This is not only important to seperate the code for testing / debugging but is also important as some modules being used require a certain file tree to be adheared too. 

The basic tree structure is as follows:

* MAIN_APP
    - templates
        - layout.html
        - index.html
        - *.html
    - testing
        - __init__.py
        - *_test.py
    - sub_programs
        - __init__.py
        - models.py
        - routes.py
        - forms.py
    - (Hidden) venv
    - app.py

There will also need to be a design for the database, using draw.io i have generated an ERD for this. Please see below:

![ERD_Diagram](https://i.imgur.com/Ek9tza7.jpg "ERD")