This is My first project using Django in this the default response is Hello Jango, This is my first project.
& demo logic request by giving response Day1 of starting Django. the functions or the logic is handled in views.py by importing HttpResponse.
Then the path is build in urls.py by from .views import home, demo
and setting the path to
path("",home,name="home"),       The "" is empty indicates that the default page response.
path("demo/",demo,name="demo"),  The "demo/" indicates that we have to manually give demo/ in url then the response is shown that is Day1 of starting Django.

python manage.py runserver runs the server.
localhost port number 8000 is for django 
http://127.0.0.1:8000/
output:
Default
Hello Jango, This is my first project
http://127.0.0.1:8000/demo
Day 1 of starting Django.


In this I havent used model.py file just request is given by user and response is handled in views.py
& path is given in urls.py 
