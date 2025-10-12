from flask import Flask, render_template, request
from math import pi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height =float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('areaoftriangle.html', area=area)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = pi * radius ** 2
    return render_template('areaofcircle.html', area=area)

if __name__ == "__main__":
    app.run(debug=True)