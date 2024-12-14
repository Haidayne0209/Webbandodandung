from datetime import datetime

from flask import Blueprint, render_template, redirect, request

from service.dashboard_service import get_dash_board

home_admin_bp = Blueprint('home_admin', __name__)


@home_admin_bp.route('/')
def index():
    from_date = request.args.get('from') if request.args.get('from') else datetime.today().date()
    to = request.args.get('to') if request.args.get('to') else datetime.today().date()
    print(from_date, to)
    model = get_dash_board(from_date, to)
    model.set_from_to(from_date, to)
    return render_template('admin/index.html', model=model)


@home_admin_bp.route('/logout')
def logout():
    return redirect('/')
