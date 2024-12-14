from flask import Flask, redirect

from controller.admin.account_admin_controller import account_admin_bp
from controller.admin.category_admin_controller import category_admin_bp
from controller.admin.home_admin_controller import home_admin_bp
from controller.admin.order_admin_controller import order_admin_bp
from controller.admin.product_admin_controller import product_admin_bp
from controller.client.auth_controller import auth_bp
from controller.client.cart_controller import cart_bp
from controller.client.checkout_controller import checkout_bp
from controller.client.history_controller import history_bp
from controller.client.home_controller import home_bp
from controller.client.product_controller import product_bp

app = Flask(__name__)

# Register blueprint for client
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(home_bp, url_prefix='/user')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(checkout_bp, url_prefix='/checkout')
app.register_blueprint(history_bp, url_prefix='/history')
# Register blueprint for admin
app.register_blueprint(home_admin_bp, url_prefix='/admin')
app.register_blueprint(account_admin_bp, url_prefix='/admin/account')
app.register_blueprint(category_admin_bp, url_prefix='/admin/category')
app.register_blueprint(product_admin_bp, url_prefix='/admin/product')
app.register_blueprint(order_admin_bp, url_prefix='/admin/order')
@app.route('/')
def index():
    return redirect('/user')


if __name__ == '__main__':
    app.run()
