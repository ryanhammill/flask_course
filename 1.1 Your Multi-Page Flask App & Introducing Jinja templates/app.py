from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/log_out')
def logout():
    return render_template('logout.html')



if __name__ == '__main__':
    app.run(debug=True)