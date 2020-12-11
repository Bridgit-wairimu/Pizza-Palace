from flask import render_template
from . import main

# views
@main.route('/')
def index():

    """
    view root page function that returns the index page and its data
    """
    title = "Welcome to Pizza Palace"
    return render_template('index.html', title = title)
    
@main.route('/pizza')
def pizza():

    """
    view root page function that returns the index page and its data
    """
    return render_template('pizza.html')
        

@main.route('/about')
def about():

    """
    view root page function that returns the index page and its data
    """
    return render_template('about.html')
