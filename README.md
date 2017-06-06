# Camp Wannajoinus
School's out for summer! We need to build an app to manage all the activities
for the upcoming Camp Wannajoinus. We've already done some of the heavy lifting
for you and need you to extend the project to allow for a few things.

## Here's what we have

We'll start you off with three basic models to get the camp going:

- User: We'll keep things simple and use Django's stock user: django.contrib.auth.models.User
- Camp: This includes the very basic details of summer camp: its name, start datetime, and end datetime
- Attendee: We keep track of camp attendees, both campers and counselors

## Here's what we want

Campers want to have tons of fun!

## How to get started
a
1. Fork git repo
1. In the base folder, set up a virtual environment using `virtualenv venv`
1. Activate virtualenv by running `. venv/bin/activate`
1. Install pip requirements by running `pip install -r requirements.txt`
1. Run the initial migrations with `./manage.py migrate`
1. Create you own user so you can login to the admin panel with `./manage.py createsuperuser`
1. Run the local web server with `./manage.py runserver`
1. Check to see if it works by visiting: http://localhost:8000/admin/
1. If that works, then you're on your way! If you get an error, please reach out to us and we'll help you get it working (we know this is hard!)

## The asdf
