from flask import render_template
from app import app 

# views
@app.route('/')
def index():

    """
    view root page function that returns the index page and its data
    """
    title = "Welcome to Pizza Palace"
    return render_template('index.html', title = title)
    
@app.route('/pizza')
def pizza():

    """
    view root page function that returns the index page and its data
    """
    return render_template('pizza.html')
        