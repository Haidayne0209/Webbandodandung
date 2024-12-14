from flask import Blueprint, render_template, make_response, url_for, redirect

from service.product_service import top_9

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    list_product = top_9()
    return render_template('client/index.html', data=list_product)


@home_bp.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_id')
    return response
