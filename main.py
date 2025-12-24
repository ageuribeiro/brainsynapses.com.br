from flask import Flask, render_template


app = Flask(__name__, template_folder='src/infrastructure/public/templates', static_folder='src/infrastructure/public/static')

@app.route('/')
def index():
    name = "Ageu Ribeiro"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)