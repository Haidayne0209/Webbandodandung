from flask import Blueprint, render_template, request, redirect

from service.auth_service import get_profile
from service.order_serivice import get_list_order_by_user_id, cancel_order
from viewmodel.history_viewmodel import HistoryViewModel

history_bp = Blueprint('history', __name__)


@history_bp.route('')
def index():
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    user = get_profile(user_id)
    list_order = get_list_order_by_user_id(user_id)
    list_done = []
    list_pending = []
    list_cancel = []
    list_shipping = []

    for order in list_order:
        if order.status == 'DONE' or order.status == 'done':
            list_done.append(order)
        elif order.status == 'pending' or order.status == 'PENDING':
            list_pending.append(order)
        elif order.status == 'cancel' or order.status == 'CANCEL':
            list_cancel.append(order)
        elif order.status == 'shipping' or order.status == 'SHIPPING':
            list_shipping.append(order)

    model = HistoryViewModel(user, list_done, list_cancel, list_pending, list_shipping)
    return render_template('client/history.html', model=model)


@history_bp.route('cancel/<int:order_id>')
def cancel(order_id):
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    cancel_order(order_id)
    return redirect('/history')