from flask_frozen import Freezer
from route import app

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['FREEZER_DESTINATION_IGNORE'] = []
app.config['ENV'] = 'production'

freezer = Freezer(app)


@freezer.register_generator
def url_generator():
    """
    Build the urls for the static site
    """
    yield '/'
    yield '/log_in.html'
    yield '/sign_up.html'
    yield '/about_us.html'
    yield '/contact_us.html'
    yield '/service2.html'
    yield '/service1.html'
    yield '/service2_templates.html'

if __name__ == '__main__':
    freezer.freeze()
