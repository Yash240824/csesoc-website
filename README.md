CSESoc Website
==========================================

http://www.csesoc.unsw.edu.au/

Getting Started
---------------------

The csesoc website uses django which is a python web framework. We also use git for version control with the repository hosted on here!

Installing Python
-----------------

Most OSs will include python. You will need a version of python between 2.5 and 2.7. Check this with

	python --version

Installing a python package manager and a virtual environment
-------------------------------------------------------------

Sometimes you may wish to work on more than one python application. If so then it is more than likely that at least two applications will have different dependencies of different versions. To save yourself from dependency hell, it is recommended to create a virtual environment for each set of dependencies so they don’t break other applications when you’re updating something. You may also wish to install a package manager to simpley the process of installing dependencies.

In this guide we are going to be using virtualenv (http://pypi.python.org/pypi/virtualenv)

On Debian/Ubuntu, the easiest way to do this is probably with apt

	sudo apt-get install python-pip python-dev build-essential
	sudo pip install --upgrade pip
	sudo pip install --upgrade virtualenv

On OS X, the easiest way is to use easy_install

	sudo easy_install virtualenv

Once you have virtualenv

	mkdir SOME_PATH
	virtualenv SOME_PATH
	source SOME_PATH/bin/activate

*substitute SOME_PATH for some path or folder where you want to create your virtual environment. For example a folder called env

You should now be inside your virtual environment. You can check this with

	$ which python
	   /usr/bin/python
	$ source env/bin/activate
	(env)$ which python
	   /Users/dylank/Documents/csesoc-website/env/bin/python

When your done with a virtual environment, you can easily deactivate with

	deactivate

Installing Django
-----------------

Now while your inside your python virtualenv, you can use pip to install packages like so

	pip install <package name>

The list of dependencies has already been made. So to install everything just run:

	pip install -r requirements.txt

Installing Git
--------------

Once you have git, you can grab a copy of the csesoc website with

	git pull https://github.com/csesoc/csesoc-website.git
	
Once you have a copy, cd into the directory and create a database

	(env)$ cd csesoc-website/
	(env)csesoc-website$ python manage.py syncdb
	Creating tables ...

Running the development webserver
---------------------------------

	python manage.py runserver
