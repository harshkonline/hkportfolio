from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

if __name__ == '__main__':
    app.run()
