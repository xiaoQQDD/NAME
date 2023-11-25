"""REST api blueprint"""
import json
from datetime import datetime, timedelta
from flask import Blueprint, render_template, request, session
from . import db
from . import auth
bp = Blueprint('rest', __name__, url_prefix='')






@bp.get("/data/search/<prov>")
def data001(prov):
    """return search dataset"""
    datas = []
    res = [d for d in datas]
    return json.dumps({"code": 0, "data": res})


@bp.route("/settings", methods=('GET', 'POST'))
@auth.login_required
def settings():
    if request.method == 'GET':
        return render_template('settings.html')
    user = db.find_by_name(session['username'])
    goal = int(request.form['goal'])
    user['goal'] = goal
    db.update_user(user)
    return render_template('settings.html', success_msg="Goal updated.")

@bp.route("/record", methods=('GET', 'POST'))
def record():
    if request.method == 'GET':
        return render_template('record.html')
    user = db.find_by_name(session['username'])
    record = int(request.form['record'])
    if 'records' not in user:
        user['records'] = []
    user['records'].append({'record':record, 'time':datetime.now().strftime('%Y-%m-%d')})
    db.update_user(user)
    return render_template('record.html', success_msg="Record added.")

@bp.route("/statistics", methods=('GET', 'POST'))
def statistics():
    if request.method == 'GET':
        return render_template('statistics.html')