
# QA_Project_1 ZMR

## Table of contents:
- What this project is
- Scope of the project
- Design specification
    - Outline
    - Tree structure
    - Database ERD
- Risk assesment
- User base

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

### Outline

There isnt a need for a fancy website frontend, however, it would still be nice for it to
look easy to navigate and intuitive. The most that will be used will be CSS. One of the main
focus's of the project will be the backend python code. It is very important that it is structured and that it follows a base file tree. This is not only important to seperate the code for testing / debugging but is also important as some modules being used require a certain file tree to be adheared too.

The basic tree structure is as follows:

### Tree structure

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

### Database ERD

There will also need to be a design for the database, using draw.io i have generated an ERD for this. Please see below:

![ERD_Diagram](https://i.imgur.com/Ek9tza7.jpg "ERD")

There are three tables in this database. There is the main Movies table. This will contain all the information of the movie. Its title, an age rating, a description and the runtime. This will be avaliable on one page for the user to scroll through. This allows them to see all of the movies currently rated on the site. The next table is the Movie_Reviews, this has a relationship with the first table. A movie contained on the site can have many reviews but doesnt have to have any. A third table is used to keep track of the amount of likes each review has recieved. This requires a boolean value True = Like False = Dislike and a username. This means that each like/dislike is assigned to a user without the need to create an account. This allows for anonymous voting but could open up to spam. This might be better fixed with ip tracking or better, a user system. That is not in scope however so will not be included.

## Risk assesment

As with any web application there is always some threat to the application and/or the data it contains. See below for a breakdown of risks assocated and remidies that can be put in place to negate any risks.

| Risk        | Likleyhood | Impact | Description  | Evaluation | Response | Control Measure | New Likelyhood | New Impact |
| ------------| -----------|--------| -------------| -----------| ---------|-----------------|----------------|------------| 
|Too many users could be trying to use your cloud service|2|3|There could be an overwhelming amount of real or fake users trying to access your service or an increased number of processes running|Your entire service could stop working and might lead to errors for other users, it might also overwhelm the cloud service and disrupt other people operations|Service may need to be restricted if this occurs, it will ruin the end user experience|Ensure your using the correct cloud infastructure and ensure that it is flexible, Ensure your application can scale to handle an influx|1|1|
|You release an unstable or broken build|1|3|You may accidentally merge the unstable and stable release branch or unstable code might make it onto the release version|Users might have a bad end experience, buisness may be lost to yourself and to the client|You will need to revert to the latest stable branch|Ensure there are clear rules in place to differentiate between release builds and internal builds, Ensure that testing is thorough and tests every element of the version before release|1|2|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

