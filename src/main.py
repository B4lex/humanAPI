from flask import Flask, request, render_template, redirect, url_for
import database


app = Flask(__name__)


@app.route('/')
def redirect_to_api():
    return redirect(url_for('api_index'))


@app.route('/api/v1/', methods=['GET'])
def api_index():
    return render_template('api_index.html')


@app.route('/api/v1/list', methods=['GET'])
def api_list_all():
    db = database.get_db()
    print(db.cursor())
    with db.cursor() as db_cur:
        humans_data = db_cur.execute('SELECT * FROM humans')
    return str(humans_data)


@app.route('/api/v1/init', methods=['GET'])
def init_api():
    database._init_db_values()
    return '<h1>API successfully initialized.</h1>'
