# django-polls

The project creating with the Django starter 5 steps of tutorial is a simple polls app where the user can sign up, login and then create their polls for others to take them. Using Django and python through out the whole project with the following features.

## Creating admin user

Using the command :
>'*$ python manage.py createsuperuser* ' 

to create the admin user and then modify the code to  make the poll app modifiable by the created admin.

The admin feature allow the user to xxplore the free admin functionalit :
* Change list of questions.
* Delete questions.

Note:
>> * The form is automatically generated from the Question model.



## Date and timezone
On the app when admin creates any questions, date and time is the next thing admin has to input after the actual question.

This feature comes after :
> from django.utils import timezone

to be able to use the present date and time.

Note:

>>* The different model field types (DateTimeField, CharField) correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin.
>> * Each DateTimeField gets free JavaScript shortcuts. Dates get a “Today” shortcut and calendar popup, and times get a “Now” shortcut and a convenient popup that lists commonly entered times.

