# GA-Project3-Assessment

First not, Bart, is that you created a django project _inside_ another directory. This is not necessary. When you run `django-admin startproject mysite`, it will create a directory called `mysite` for you, which holds the whole django project. That will be the root folder for your project. There _will_ be a second folder _inside_ your `mysite` directory that is *also* called _mysite_. This is normal and automatically generated by django. In this case, you need to be inside the outter-most `mysite` directory in order to run the commands in terminal that start with `python3 manage.py` because that's where the `manage.py` file is.