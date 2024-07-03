from app.models.cash_receipt_model import CashReceipt
from app import db

class CashReceiptService:
    @staticmethod
    def create_cash_receipt(data):
        receipt = CashReceipt(
            receipt_number=data['receipt_number'],
            issue_date=data['issue_date'],
            buyer_name=data['buyer_name'],
            buyer_registration_number=data['buyer_registration_number'],
            total_amount=data['total_amount'],
            tax_amount=data['tax_amount']
        )
        db.session.add(receipt)
        db.session.commit()

    @staticmethod
    def get_all_cash_receipts():
        return CashReceipt.query.all()
