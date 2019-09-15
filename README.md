# django-polls


The project creating with the Django starter 5 steps of tutorial is a simple polls app where the user can sign up, login and then create their polls for others to take them. Using Django and python through out the whole project with the following features.

## Creating admin user

Using the command :
>       $ python manage.py createsuperuser

to create the admin user and then modify the code to  make the poll app modifiable by the created admin.

The admin feature allow the user to xxplore the free admin functionalit :
* Change list of questions.
* Delete questions.

Note:
>> * The form is automatically generated from the Question model.



## Date and timezone
On the app when admin creates any questions, date and time is the next thing admin has to input after the actual question.

This feature comes after :
>       from django.utils import timezone

to be able to use the present date and time.

Note:

>>* The different model field types (DateTimeField, CharField) correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin.
>> * Each DateTimeField gets free JavaScript shortcuts. Dates get a “Today” shortcut and calendar popup, and times get a “Now” shortcut and a convenient popup that lists commonly entered times.

## Raising 404 error
On which case were a question with the requested ID doesn’t exist. The view should raise an error, an 404 error, which done by throwing try-except :
>       try:
>           question = Question.objects.get(pk=question_id)
>       except Question.DoesNotExist:
>           raise Http404("Question does not exist")
>       return render(request, 'polls/detail.html', {'question': question})

## Namespacing URL names
Add namespaces to your URLconf. In the polls/urls.py file,add an app_name to set the application namespace to differentiate the URL name between apps, using :

>       {% url %}

## Create an automated tests
In which case there are bugs amoung files, tests are simple routines that check the operation of your code. 

Note:
>> * Tests don’t just identify problems, they prevent them
>>* Tests make your code more attractive





