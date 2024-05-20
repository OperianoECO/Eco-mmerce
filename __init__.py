from flask import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = 'static/files'
allowed_extensions_list = ['jpg', 'png', 'jpeg', '']


@app.route('/')
def home():
    return render_template('store.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
