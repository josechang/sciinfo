1.Create new djongal project folder.

```
mkdir django_project
```

2.Create a virtual environment in django_project folder.

```
virtualenv django_project/
```

3.Activate virtual environment in ```django_project/```.

```
source bin/activate
```

4.Install django data package.

```
pip install django
```

5.Initialize a django project.

```
django-admin startproject myfirstdjangoproject
```

6.Use```tree```to check any file in```myfirstdjangoproject```. 

7.Test your django project.

```
(location)
pwd
/home/timhsia/django_project/myfirstdjangoproject
```

```
(check)
cd myfirstdjangoproject
python manage.py test
```

```
(show)
Ran 0 tests in 0.000s

OK
Destroying test database for alias 'default'...
```


8.Run server.

```
python manage.py runserver 0.0.0.0:8000

```

**Notice:** Port can use from 8000 to 8100

9.Input web address on browser.

```
epsilon.nordlinglab.org:8000
```
 
If you meet below problem, use ```python manage.py migrate``` command to solve it.

```
You have unapplied migrations; your app may not work properly until they are app
lied.
Run 'python manage.py migrate' to apply them.
```

