from flask import Blueprint, render_template, request

from service.category_service import get_list_active_category
from service.product_service import get_list_product, get_by_id
from viewmodel.product_viewmodel import ProductViewModel

product_bp = Blueprint('product', __name__)


@product_bp.route('')
def index():
    cate_id = request.args.get('cate') if request.args.get('cate') else -1
    page = request.args.get('page') if request.args.get('page') else 1
    key = request.args.get('key') if request.args.get('key') else ''
    list_cate = get_list_active_category()
    list_cate_1 = list_cate[:4]
    list_cate_2 = list_cate[4:]
    list_product = get_list_product(cate_id, key)
    model = ProductViewModel(list_cate_1, list_cate_2, list_product, cate_id, page, key)
    return render_template('client/products.html', model=model)

@product_bp.route('/detail/<int:product_id>')
def detail(product_id):
    product = get_by_id(product_id)
    return render_template('client/product_detail.html', model=product)
