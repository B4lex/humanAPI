from flask import Flask, render_template, redirect, url_for

from database import db_manager


app = Flask(__name__)


@app.route('/')
def redirect_to_api():
    return redirect(url_for('api_index'))


@app.route('/api/v1/', methods=['GET'])
def api_index():
    return render_template('api_index.html')


@app.route('/api/v1/humans/', methods=['GET'])
def api_list_all_humans():
    return {'results': db_manager.get_all_data_dict() or []}


@app.route('/api/v1/humans/<int:human_id>/', methods=['GET'])
def api_specified_human(human_id):
    human_data = db_manager.get_data_by_id(human_id)
    if human_data:
        return human_data
    else:
        return {'error': f'Human with id {human_id} does not exist.'}, 404


@app.route('/api/v1/humans/<int:human_id>/', methods=['DELETE'])
def api_delete_specified_human(human_id):
    human_data = db_manager.get_data_by_id(human_id)
    if human_data:
        db_manager.remove_data_by_id(human_id)
        return {'info': f'Human with id {human_id} has been deleted.'}
    else:
        return {'error': f'Human with id {human_id} does not exist.'}, 404
