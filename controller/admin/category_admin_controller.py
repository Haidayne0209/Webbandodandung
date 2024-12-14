from flask import Blueprint, render_template, request, jsonify

from service.category_service import get_list_category, do_add_category, get_by_id, do_update_category, \
    get_list_active_category
from service.checkout_service import update_order_status

category_admin_bp = Blueprint('category_admin', __name__)


@category_admin_bp.route('/')
def index():
    return render_template('admin/category/index.html', data=get_list_active_category())


@category_admin_bp.route('/add')
def add():
    return render_template('admin/category/add.html')


@category_admin_bp.route('do-add', methods=['POST'])
def do_add():
    cate_name = request.form['cate_name']
    result = do_add_category(cate_name)
    return jsonify({'success': result})


@category_admin_bp.route('/edit')
def edit():
    cate_id = request.args.get('id')
    cate = get_by_id(cate_id)
    return render_template('admin/category/edit.html', data=cate)


@category_admin_bp.route('do-update', methods=['POST'])
def do_update():
    cate_id = request.form['cate_id']
    cate_name = request.form['cate_name']
    result = do_update_category(cate_id, cate_name)
    return jsonify({'success': True, 'message': result})

@category_admin_bp.route('/delete/<int:id>')
def delete(id):
    update_order_status(id, 'INACTIVE')
    return jsonify({'success': True})