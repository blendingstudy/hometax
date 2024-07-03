from app import db

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(255), unique=True, nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    seller_name = db.Column(db.String(255), nullable=False)
    seller_registration_number = db.Column(db.String(255), nullable=False)
    buyer_name = db.Column(db.String(255), nullable=False)
    buyer_registration_number = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Numeric(15, 2), nullable=False)
    tax_amount = db.Column(db.Numeric(15, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
