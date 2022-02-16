from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Peter'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'PED185', 'title': 'Beginning Weight Training and Conditioning'},
                'instructor': 'Kristine Furlong'},
               {'classInfo': {'code': 'SEC300', 'title': 'Introduction to Cybersecurity'}, 'instructor': 'Yipkei Kwok'}]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
