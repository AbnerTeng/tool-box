import os
from app.route import app


if __name__ == "__main__":
    app.config['ENV'] = os.getenv('FLASK_ENV', 'development') 
    app.run(debug=app.config['ENV'] == 'development')
