from flask import Blueprint, render_template, request, redirect, url_for
from app.services.invoice_service import InvoiceService

invoice_bp = Blueprint('invoice_bp', __name__)

@invoice_bp.route('/create', methods=['GET', 'POST'])
def create_invoice():
    if request.method == 'POST':
        data = request.form
        InvoiceService.create_invoice(data)
        return redirect(url_for('invoice_bp.list_invoices'))
    return render_template('invoice/create.html')

@invoice_bp.route('/list', methods=['GET'])
def list_invoices():
    invoices = InvoiceService.get_all_invoices()
    return render_template('invoice/list.html', invoices=invoices)
