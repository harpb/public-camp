# Camp Wannajoinus
School's out for summer! We need to build an app to manage all the activities
for the upcoming Camp Wannajoinus. We've already done some of the heavy lifting
for you and need you to extend the project to allow for a few things.

## Here's what we have

We'll start you off with three basic models to get the camp going:

- User
 -  We'll keep things simple and use Django's stock user: django.contrib.auth.models.User
- Camp
 - This includes the very basic details of summer camp: its name, start datetime, and end datetime
- Attendee
 - We keep track of camp attendees, both campers and counselors

User (Django)

Camp
name
starts_at
ends_at

Attendee
user (fk to User)
role (camper or counselor)

## Here's what we want

Campers want to have tons of fun!

## How to get started

- Fork git repo
- In the base folder, set up a virtual environment using `virtualenv venv`
- Activate virtualenv by running `. venv/bin/activate`
- Install pip requirements by running `pip install -r requirements.txt`
- Run the initial migrations
 - `./manage.py migrate`
- Create you own user so you can login to the admin panel
 - `./manage.py createsuperuser`
- Run the local server
 - `./manage.py runserver`
- Check to see if it works by visiting: http://localhost:8000/admin/
- If that works, then you're on your way! If you get an error, please reach out
to us and we'll help you get it working (we know this is hard!)

## The Project
