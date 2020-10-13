from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('bar_admin.html')

@app.route('/get_data')
def get_data():
    time.sleep(5)
    return render_template('get_data.html')

@app.route('/new_loader')
def new_loader():
    time.sleep(5)
    return render_template('new_loader')

if __name__ == '__main__':
    app.run()
