from flask import *

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {}
    params['title'] = title
    return render_template('base.html', **params)

@app.route('/training/<prof>')
def plan(prof):
    params = {}
    if 'строитель' in prof.lower() or 'инжинер' in prof.lower():
        prof = 'инженер'
    else:
        prof = 'научный'
    params['prof'] = prof
    return render_template('content.html', **params)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
