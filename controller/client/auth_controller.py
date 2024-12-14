from flask import Blueprint, request, jsonify

from service.auth_service import login, register

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login_route():
    email = request.form['email']
    password = request.form['password']
    user = login(email, password)
    if user:
        return jsonify({'success': True, 'message': 'Đăng nhập thành công', 'data': user.__dict__})
    return jsonify({'success': False, 'message': 'Tên đăng nhập hoặc mật khẩu không đúng'})


@auth_bp.route('/register', methods=['POST'])
def register_route():
    email = request.form['email']
    password = request.form['password']
    name = request.form['fullname']
    result = register(email, password, name)
    if result:
        return jsonify({'success': True, 'message': 'Đăng ký tài khoản thành công'})
    return jsonify({'success': False, 'message': 'Tên đăng nhập đã tồn tại'})
