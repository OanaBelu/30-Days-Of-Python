
# Day 27 - Setting Up a Local Development Environment

# Why set up a local development environment?
# The first reason is dependability
# The second reason is speed

# Your local development options:
# The first thing we need to do when setting up a local development environment is set up a new place to actually
# write our code. In this post, we're going to be setting up PyCharm

# Create It :
"""python -m venv venv"""
# Activate It
"venv\Scripts\activate"
# Install Packages Into It - After creating and activating your virtual environment, you can now install any external
# dependencies that you need for your project
"""python -m pip install <package-name>"""
# Deactivate It
"""deactivate"""

"""To better understand why this is so important, imagine you’re building Django websites for two different clients. 
One client is comfortable with their existing web app, which you initially built using Django 2.2.26, and that client 
refuses to update their project to a modern Django version. Another client wants you to include async functionality 
in their website, which is only available starting from Django 4.0.

If you installed Django globally, you could only have one of the two versions installed:

PS> mkdir client-old
PS> cd client-old
PS> python -m venv venv --prompt="client-old"
PS> venv\Scripts\activate
(client-old) PS> python -m pip install django==2.2.26
(client-old) PS> python -m pip list
Package    Version
---------- -------
Django     2.2.26
pip        22.0.4
pytz       2022.1
setuptools 58.1.0
sqlparse   0.4.2
(client-old) PS> deactivate

PS> cd ..
PS> mkdir client-new
PS> cd client-new
PS> python -m venv venv --prompt="client-new"
PS> venv\Scripts\activate
(client-new) PS> python -m pip install django==4.0.3
(client-new) PS> python -m pip list
Package    Version
---------- -------
asgiref    3.5.0
Django     4.0.3
pip        22.0.4
setuptools 58.1.0
sqlparse   0.4.2
tzdata     2022.1
(client-new) PS> deactivate
"""

