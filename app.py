from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/exp')
def exp():
    return render_template('exp.html')

@app.route('/major')
def major():
    return render_template('major.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    result = {"content": content, "name": name, "email": email}
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)