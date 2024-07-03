from app.models.invoice_model import Invoice
from app import db

class InvoiceService:
    @staticmethod
    def create_invoice(data):
        invoice = Invoice(
            invoice_number=data['invoice_number'],
            issue_date=data['issue_date'],
            seller_name=data['seller_name'],
            seller_registration_number=data['seller_registration_number'],
            buyer_name=data['buyer_name'],
            buyer_registration_number=data['buyer_registration_number'],
            total_amount=data['total_amount'],
            tax_amount=data['tax_amount']
        )
        db.session.add(invoice)
        db.session.commit()

    @staticmethod
    def get_all_invoices():
        return Invoice.query.all()
