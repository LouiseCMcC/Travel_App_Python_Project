# Travel_App_Python_Project
Full Stack app for tracking, recording, and planning travel. Solo project using Python, Flask, HTML, CSS and SQL

To Run:

In terminal to create the database and populate it:

from in the 'travel_app_code' folder

dropdb travel_manager createdb travel_manager psql -d travel_manager -f db/travel_manager python3 console.py

In terminal to run the app:

flask run CTRL + c to quit

In browser:

go to localhost:4999

The Brief:

Travel Bucket List - Build an app to track someone's travel adventures.

MVP: The app should allow the user to track countries and cities they want to visit and those they have visited. The user should be able to create and edit countries Each country should have one or more cities to visit The user should be able to create and delete entries for cities The app should allow the user to mark destinations as visited or still to see

Extensions: Have separate pages for destinations visited and those still to visit Add sights to the destination cities Search for destination by continent, city or country Any other ideas you might come up with

Technologies used: Postgres, Pythron 3.0, CSS, SQL, HTML 5.0
