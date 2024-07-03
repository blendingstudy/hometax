from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://hometax:hometax1234!@localhost/hometax'
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bcrypt.init_app(app)

    from app.controllers.invoice_controller import invoice_bp
    from app.controllers.cash_receipt_controller import cash_receipt_bp
    from app.controllers.business_status_controller import business_status_bp

    app.register_blueprint(invoice_bp, url_prefix='/invoices')
    app.register_blueprint(cash_receipt_bp, url_prefix='/cash_receipts')
    app.register_blueprint(business_status_bp, url_prefix='/business_status')

    return app
