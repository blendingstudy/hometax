from flask import Blueprint, render_template, request, redirect, url_for
from app.services.cash_receipt_service import CashReceiptService

cash_receipt_bp = Blueprint('cash_receipt_bp', __name__)

@cash_receipt_bp.route('/create', methods=['GET', 'POST'])
def create_cash_receipt():
    if request.method == 'POST':
        data = request.form
        CashReceiptService.create_cash_receipt(data)
        return redirect(url_for('cash_receipt_bp.list_cash_receipts'))
    return render_template('cash_receipt/create.html')

@cash_receipt_bp.route('/list', methods=['GET'])
def list_cash_receipts():
    cash_receipts = CashReceiptService.get_all_cash_receipts()
    return render_template('cash_receipt/list.html', cash_receipts=cash_receipts)
