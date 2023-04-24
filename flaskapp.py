from flask import Flask, render_template, request, render_template_string, redirect
import os
from datetime import datetime

HTML = '<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Malware Martini</title><link rel="stylesheet" href="/static/assets/css/member.css" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head><body><nav class="navbar navbar-expand-lg navbar-dark bg-dark"><div class="container-fluid"><a class="navbar-brand" href="/">Malware Martini</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item"><a class="nav-link" href="/team">Executive Team</a></li><li class="nav-item"><a class="nav-link" href="/contacts">Contacts</a></li></ul></div></div></nav><br><p id="error">{} not found</p><footer id="footererror"class="text-center text-white"style="background-color: #343a40"><br /><p>© 2023 Copyright: <a class="text-white" href="#">Malware Martini</a></p></footer></body></html>'

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret-key')
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Create a route decorator
@app.route('/')


def index():
	return render_template("index.html")
if __name__ == '__main__':
   app.run()


@app.route('/team')

def aboutus():
	return render_template("team.html")

@app.route('/contacts')

def contacts():
	return render_template("contacts.html")

@app.route('/member')

def member():
	names = ["Jason", "Jackson", "Matthew", "Lawrence", "Bob", "Mia", "Jonathan", "William", "Isabella"]
	member = request.values.get('member')
	if member in names:
		name = member
		return render_template("member.html", name = name)
	else:
		name = member
		return render_template_string(HTML.format(name))

@app.route('/message', methods=['POST'])
def create_message_file():
    name = request.form.get('name')
    message = request.form.get('message')
    return render_template('confirm.html', message=message, name=name)

@app.route('/confirm', methods=['POST'])
def confirm_message_file():
    name = request.form.get('name')
    message = request.form.get('message')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    path = "/var/www/html/flaskapp/"
    filename = name
    with open(os.path.join(path, filename + ".txt"), 'a+') as file:
        file.write(name + " : " + message + ' [' + timestamp + ']' + '\n')
    return redirect('/sent?file=' + filename)

@app.route('/sent', methods=['GET'])
def confirm_send():
	filename = request.values.get('file')
	path = "/var/www/html/flaskapp/"
	with open(os.path.join(path, filename + ".txt"), 'r') as file:
		message = file.read()
	return render_template('confirm_send.html', message=message)