from flask import Flask
import datetime, pytz
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
	t = datetime.datetime.now(pytz.timezone('US/Eastern'))
	return t.strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
