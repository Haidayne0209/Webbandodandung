from flask import Blueprint, render_template, request, redirect

from service.auth_service import lock, unblock, get_list_user

account_admin_bp = Blueprint('account_admin', __name__)


@account_admin_bp.route('/')
def index():
    return render_template('admin/user/index.html', data=get_list_user())


@account_admin_bp.route('/lock')
def lock_user():
    user_id = request.args.get('id')
    lock(user_id)
    return redirect('/admin/account')


@account_admin_bp.route('/unblock')
def unblock_user():
    user_id = request.args.get('id')
    unblock(user_id)
    return redirect('/admin/account')
