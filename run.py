from app import create_app, db
from app.models.invoice_model import Invoice
from app.models.cash_receipt_model import CashReceipt
from app.models.business_status_model import BusinessStatus

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Invoice': Invoice, 'CashReceipt': CashReceipt, 'BusinessStatus': BusinessStatus}

if __name__ == "__main__":
    app.run(debug=True)
