import datetime

import pytz
from flask import Blueprint, render_template, request, redirect, jsonify

from service.cart_service import get_cart_by_user_id
from service.checkout_service import create_order, update_order_status
from service.vnpay_service import VnPayService
from viewmodel.cart_viewmodel import CartViewModel

checkout_bp = Blueprint('checkout', __name__)


def sort_object(obj):
    """Sort a dictionary by its keys."""
    return dict(sorted(obj.items()))


def get_vnpay_link(full_name, address, email, phone, amount, user_id):
    # Timezone and date setup
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    date = datetime.datetime.now(tz)
    create_date = date.strftime('%Y%m%d%H%M%S')

    # Configuration values
    tmn_code = 'GLE8YXG4'  # Your VNPAY TMN code
    secret_key = 'ZCVPMHAELZKRPGTFLWJDPLQVPHBWEKXG'  # Your secret key
    vnp_url = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # VNPAY URL
    return_url = 'http://localhost:5000/checkout/vnpay_return'  # Your return URL
    txn_ref = date.strftime('%d%H%M%S')
    create_order(user_id, address, full_name, phone, email, 'VNPAY', txn_ref)
    expire_date = (date + datetime.timedelta(minutes=15)).strftime('%Y%m%d%H%M%S')

    vnp = VnPayService()
    vnp.requestData['vnp_Version'] = '2.1.0'
    vnp.requestData['vnp_Command'] = 'pay'
    vnp.requestData['vnp_TmnCode'] = tmn_code
    vnp.requestData['vnp_Amount'] = int(float(amount)) * 100
    vnp.requestData['vnp_CurrCode'] = 'VND'
    vnp.requestData['vnp_TxnRef'] = txn_ref
    vnp.requestData['vnp_OrderInfo'] = 'Thanh toán đơn hàng'
    vnp.requestData['vnp_OrderType'] = 'other'
    vnp.requestData['vnp_Locale'] = 'vn'

    vnp.requestData['vnp_CreateDate'] = create_date  # 20150410063022
    vnp.requestData['vnp_ExpireDate'] = expire_date  # 20150410103022
    vnp.requestData['vnp_IpAddr'] = get_client_ip()
    vnp.requestData['vnp_ReturnUrl'] = return_url
    final_url = vnp.get_payment_url(vnp_url, secret_key)
    print(final_url)
    # Return the generated URL
    return final_url


@checkout_bp.route('')
def index():
    user_id = request.cookies.get('user_id')
    cart = get_cart_by_user_id(user_id)
    if user_id is None:
        return redirect('/user?open-login=1x')
    model = CartViewModel(cart)
    return render_template('client/checkout.html', model=model)


@checkout_bp.route('send', methods=['POST'])
def send():
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    full_name = request.form['fullName']
    address = request.form['address']
    email = request.form['email']
    phone = request.form['phone']
    payment_method = request.form['paymentMethod']
    if payment_method == 'COD':
        create_order(user_id, address, full_name, phone, email, payment_method)
        link = '/history'
    else:
        amount = request.form['amount']
        link = get_vnpay_link(full_name, address, email, phone, amount, user_id)
    return jsonify({'link': link})


@checkout_bp.route('vnpay_return')
def vnpay_return():
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    txn_ref = request.args.get('vnp_TxnRef')
    status = request.args.get('vnp_ResponseCode')
    if status != '00':
        update_order_status(txn_ref, 'CANCEL')
    return redirect('/history')


def get_client_ip():
    """Retrieve the client's IP address."""
    return request.headers.get('X-Forwarded-For') or request.remote_addr
