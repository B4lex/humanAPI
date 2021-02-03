from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def redirect_to_api():
    return redirect(url_for('api_index'))


@app.route('/api/v1/docs', methods=['GET'])
def api_index():
    return render_template('api_index.html')


@app.route('/api/v1/list', methods=['GET'])
def api_list_all():
    return ''

