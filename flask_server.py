from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def first():
    #return '小猴牛逼'
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True,port=5002,host='172.16.0.2')