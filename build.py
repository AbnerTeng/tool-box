from flask_frozen import Freezer
from route import app

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['ENV'] = 'production'

freezer = Freezer(app)

def url_generator():
    yield 'home'
    yield 'login'
    yield 'signup'
    yield 'about'
    yield 'services'

if __name__ == '__main__':
    freezer.freeze()