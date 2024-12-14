from flask import Blueprint, render_template, request, redirect

from service.cart_service import get_cart_by_user_id, add_to_cart, remove_cart_item
from viewmodel.cart_viewmodel import CartViewModel

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('')
def index():
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    cart = get_cart_by_user_id(user_id)
    print(cart)
    model = CartViewModel(cart)
    return render_template('client/cart.html', model=model)


@cart_bp.route('add')
def add():
    user_id = request.cookies.get('user_id')
    if user_id is None:
        return redirect('/user?open-login=1x')
    product_id = request.args.get('pid')
    if product_id is None:
        return redirect('/products')
    quantity = request.args.get('q') if request.args.get('q') else 1
    add_to_cart(user_id, product_id, quantity)
    return redirect('/cart')

@cart_bp.route('remove/<int:cart_item_id>')
def remove(cart_item_id):
    remove_cart_item(cart_item_id)
    return redirect('/cart')