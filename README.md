
# QA_Project_1 ZMR

## Table of contents:
- What this project is (#What this project is)
- Scope of the project
    - MVP
    - Personal goals
- Design specification
    - Outline
    - Tree structure
    - Database ERD
- Risk assesment
- Trello Board
- Testing
- Pipeline overview
- Changes as project has progressed


## What this project is
This project will be a way for you to upload reviews about your favorite movies!
This is a web based application running with flask / python intergrating a cloud database.
There will be no login system and anyone can leave a review on a movie, reviews can be
liked and the most liked reviews will appear closer to the top of the list. It is down
to the site owner to update the movie titles but , again, anyone can submit a review!

## Scope of the projects
### MVP
There are a few basic requirements this project must hit, they are as followed:
- A Trello board
- At least two databases, in this case two with a relationship
- A HTML front end, a base layout will be used and a navigation bar will be used
- WTForms to allow user input
- Self testing python to be run during each build
- Archiving of tests to allow backtracing
- CRUD Functionality
- Usage of VCS (GIT)

### Personal Goals
I would like to tailor my own goals to the MVP so that I am not doing and unecessary work, a few of my own goals are as follows:
- Working list of movies, preferably with picture
- Working review system with multiple reviews for a couple of movies
- Rigidity in my code, I want my code to be top notch and ensure it is to standard practice


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
        - test_*.py
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
| :---------- | :--------: | :----: | :----------- | :--------- | :------- | :-------------- | :------------: | :--------: | 
|Too many users could be trying to use your cloud service|2|3|There could be an overwhelming amount of real or fake users trying to access your service or an increased number of processes running|Your entire service could stop working and might lead to errors for other users, it might also overwhelm the cloud service and disrupt other people operations|Service may need to be restricted if this occurs, it will ruin the end user experience|Ensure your using the correct cloud infastructure and ensure that it is flexible, Ensure your application can scale to handle an influx|1|1|
|You release an unstable or broken build|1|3|You may accidentally merge the unstable and stable release branch or unstable code might make it onto the release version|Users might have a bad end experience, buisness may be lost to yourself and to the client|You will need to revert to the latest stable branch|Ensure there are clear rules in place to differentiate between release builds and internal builds, Ensure that testing is thorough and tests every element of the version before release|1|2|
|Data loss that is integeral to function occurs|1|3|You may loose hardware or simply forget data that is key to the program being used, it could be accidentally deleted|The service would be out of operation until the orignal data could be recovered|You would either need to impliment a patch around the data or source new data|Ensure any vital data is backed-up, this may be on the cloud or physically. Using a VCS is a very good measure as it allows you to rollback easily|1|2|
|A first or third party could release important data such as passwords|2|3|A disgruntled employee, yourself or someone else might accidentally or maliciously release senitive information that allows unauthorised users to view sensitive content|Code could be stolen or important information could be leaked|Code would need to be changed, Passwords would need to be changed and re-distributed|Ensure employees are given the relevant access and not overall access, Ensure any important information is stored securley so if its leaked its harder to decode, Use 2FA To secure sensitive info so its not imediatly accesible|1|1|
|Hateful speech may be posted on your website|3|2|Someone may write harmful or abuse content on your website to purposley cause harm to other users|Site may get negative reviews or decreased traffic|The hateful speech will need to be taken down and the user be given limited funcitonality or banned|Validate the information before it is posted to the site, this might be a quick check written in code or migth be a human validation step|1|1|
|Connection to the database is lost|1|3|For whatever reason the connection to the database might be lost|The service will stop working functionally but the website will still be live|A new connection needs to be re-established or a backup of the database needs to be made|Ensure there is a fallback option, also ensure a repulatable cloud service is used. Ensure the used service allows for expansion |1|1|
|Incorrect data may be posted to the website|2|1|A spelling mistake or incorrect piece of information might make it onto the website|Although it wouldnt stop the website functioning it may decrease user satisfacton and again the site may get negative reviews or decreased traffic|Ensure the information is appended quickly and that it is from a repultable source|Ensure all information being posted to the website is factually correct and ensure the original source is reputable|1|1|

## Trello board
I will be using Trello to track my project, I will not be posting screenshots but rather providing a link.

https://trello.com/b/FogfXGWJ/zmr

I will be using trello to ensure there are a clear list of goals, I can track when I have met these goals and how confident i will be in meeting them for the set deadline.
I will also be tracking user stories throught the project to make sure what I am delviering is suitable for myself and the end user.

## Testing

I have used Flask' built in testing module, this allows simple POST requests to the website and forms, it then reads text from the GET that it receives back, i have acheived a 75% test
coverage in my program which is good so far. I could increase this however to save time I have not. The reason for this is because in the routes.py there are two very similar chunks of check code, by design they have had to be duplicated and changed instead of made into a function however they both perfom the same checks. I have checked on iteration and it is 100% covered, this gives me a good indication that the second duplicate block is perfoming its role great aswell.

The testing generates a coverage report automatically when a new commit is added to the main branch. This is done through a jenkins item and an automatic webhook. This means everytime something is committed to main it is automatically tests, built then deployed. The test results are artifacted allowing me to track changes, below is a screenshot of my jenkins interface. The reason builder has failed is because it is using gunicorn and running the task endlessly, this can be improved but works for now.

![Jenkins](https://i.imgur.com/tfqJ9wF.png "Jenkins")

![Coverage](https://i.imgur.com/ULW7J4p.png "Coverage")


## Pipeline Overview

Please see below a diagram as to my pipeline:

![Pipeline](https://i.imgur.com/b9kpqjL.png "Pipeline")

## Changes as project has progressed

I have restructured the project slightly, due to the need for me to add a users I have missed off the Review_Likes table, this is a small part but the main core of the site remains,
I have managed to achieve all CRUD functionality, create a trello board and complete a risk assesment. The new ERD diagram is as follows:

![ERD_Diagram](https://i.imgur.com/Z7ilG35.jpg "ERD")