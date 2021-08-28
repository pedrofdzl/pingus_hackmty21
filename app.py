from flask import Flask, render_template, redirect, flash, url_for, request

# DB dependencies
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySuperSecretKey'

# DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Log In
from flask_login import (
                        UserMixin, login_manager, login_user, LoginManager,
                        login_required, logout_user, current_user,
)

# Clases camelCase
# todo lo demas snake_case




# Custom Error Pages
@app.errorhandler(404):
def error_404_handler(e):
    return render_template('404.html')


@app.errorhandler(500):
def error_500_handler(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run(debug=True)
