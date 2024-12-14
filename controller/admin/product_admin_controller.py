from flask import Blueprint, render_template, request, jsonify, redirect

from service.category_service import get_list_active_category
from service.product_service import get_list_product, add_product, get_by_id, update_product, delete_product

product_admin_bp = Blueprint('product_admin', __name__)


@product_admin_bp.route('/')
def index():
    list_product = get_list_product()
    return render_template('admin/product/index.html', model=list_product)


@product_admin_bp.route('/edit/<int:id>')
def edit(id):
    product = get_by_id(id)
    list_cate = get_list_active_category()
    return render_template('admin/product/edit.html', p=product, cates=list_cate)


@product_admin_bp.route('/add')
def add():
    list_cate = get_list_active_category()
    return render_template('admin/product/add.html', model=list_cate)


@product_admin_bp.route('/do-add', methods=['POST'])
def do_add():
    form = request.form
    name = form['name']
    cate = form['cate']
    price = form['price'] if 'price' in form else 0
    description = form['description'] if 'description' in form else ''
    url = form['url'] if 'url' in form else ''
    add_product(name, cate, price, description, url)
    return jsonify({'success': 'ok'})


@product_admin_bp.route('/do-update', methods=['POST'])
def do_edit():
    form = request.form
    product_id = form['product_id']
    name = form['name']
    cate = form['cate']
    price = form['price'] if 'price' in form else 0
    description = form['description'] if 'description' in form else ''
    url = form['url'] if 'url' in form else ''
    update_product(product_id, name, cate, price, description, url)
    return jsonify({'success': 'ok'})


@product_admin_bp.route('/delete/<int:id>')
def delete(id):
    delete_product(id)
    return redirect('/admin/product')
