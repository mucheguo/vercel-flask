from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def meihua():
    return render_template('meihua.html')

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
