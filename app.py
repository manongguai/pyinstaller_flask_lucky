from flask import Flask,render_template
import webbrowser
url = 'http://127.0.0.1:8000/index.html/'
app = Flask(__name__, static_folder='web', static_url_path='/',)

if __name__ == '__main__':
    webbrowser.open(url)
    print('web listen on http://127.0.0.1:8000/index.html/')
    app.run(port=8000)

 