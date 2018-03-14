from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/return', methods=['POST'])
def gohome():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def user_data():
    print 'received the post data!'

    fname = request.form['fname']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['desc']

    print fname, location, language, comment

    return render_template('showData.html', name = fname, location = location, language = language, comment = comment)

app.run(debug=True)