from flask import Blueprint, render_template, request, redirect

from service.order_serivice import get_list_order_by_user_id, update_order

order_admin_bp = Blueprint('order_admin', __name__)


@order_admin_bp.route('/')
def index():
    list_order = get_list_order_by_user_id()
    return render_template('admin/order/index.html', model=list_order)


@order_admin_bp.route('/update')
def update():
    oid = request.args.get('oid')
    status = request.args.get('s')

    update_order(oid, status)
    return redirect('/admin/order')
