from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('bar_admin.html')

@app.route('/demo_loader')
def demo_loader():
    time.sleep(3)
    return 'Waited for 3 secs'

if __name__ == '__main__':
    app.run()
