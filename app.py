from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# video guia: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=554s
