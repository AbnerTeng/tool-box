import os
from flask_frozen import Freezer
from app.route import app

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['ENV'] = 'production'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()