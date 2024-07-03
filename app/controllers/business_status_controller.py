from flask import Blueprint, render_template, request
from app.services.business_status_service import BusinessStatusService

business_status_bp = Blueprint('business_status_bp', __name__)

@business_status_bp.route('/query', methods=['GET', 'POST'])
def query_business_status():
    status = None
    if request.method == 'POST':
        business_id = request.form['business_id']
        status = BusinessStatusService.check_business_status(business_id)
    return render_template('business_status/query.html', status=status)
