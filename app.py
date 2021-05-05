from flask import Flask, render_template, request
from models import Akademik

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ajaxAjaxJalan'

@app.route('/')
def ajaxJalan():
	form = Akademik()
	container = []
	container = form.SelectDB()
	return render_template('cobaAjax.html', container=container)

@app.route('/db')
def golekCari():
	return render_template('AjaxDatabase.html')


if __name__ == '__main__':
	app.run(debug=True)
