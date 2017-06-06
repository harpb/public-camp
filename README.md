# Camp Wannajoinus
School's out for summer! We need to build an app to manage all the activities
for the upcoming Camp Wannajoinus. We've already done some of the heavy lifting
for you and need you to extend the project to allow for a few things.

## Here's what we have

We'll start you off with three basic models to get the camp going:

- User: We'll keep things simple and use Django's stock user: django.contrib.auth.models.User
- Camp: This includes the very basic details of summer camp: its name, start datetime, and end datetime
- Attendee: This is how we keep track of camp attendees, both campers and counselors

## Your mission

Campers want to have tons of fun! How and when and with whom are they having fun? That will be your task. You will be building out the activities and activities registration section of our app. 

## How to get started

1. Fork git repo using `git clone https://github.com/jyveapp/summer-camp.git`
1. In the root folder (where `manage.py` resides), set up a virtual environment using `virtualenv venv` ([virtualenv installation guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
1. Activate virtualenv by running `. venv/bin/activate`
1. Install pip requirements by running `pip install -r requirements.txt`
1. Run the initial migrations with `./manage.py migrate`
1. Create you own user so you can login to the admin panel with `./manage.py createsuperuser`
1. Run the local web server with `./manage.py runserver`
1. Check to see if it works by visiting: http://localhost:8000/admin/
1. If that works, then you're on your way! If you get an error, please reach out to us and we'll help you get it working (we know this is hard!)

## What we're looking for

1. Well thought out models for activities and activity registrations
1. Admin panel for activities that allows you to create/edit/update/delete an activity, as well as see all the people attending. An activity should have a name, start datetime, end datetime, counselor that's leading it, and list of attendees (registrants)
1. Admin panel for activity registrations that allows you to create/edit/update/delete an activity registration. Note there should be a uniqueness constraint that disallows a user from signing up for the same activity more than once. 

## Bonus points

1. Unit tests on models
1. 100% test coverage using the `coverage` library ([docs here; it's included in our pip requirements](https://coverage.readthedocs.io/en/coverage-4.4.1/))
1. Deploy the app on Heroku ([details here](https://devcenter.heroku.com/articles/deploying-python))
1. Easter eggs you come up with that will make camp more fun for the campers
