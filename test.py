@app.route('/confirm', methods=['POST'])
def confirm_message_file():
    name = request.form.get('name')
    message = request.form.get('message')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    path = "/var/www/html/flaskapp/"
    filename = name
    with open(os.path.join(path, filename + ".txt"), 'a+') as file:
        file.write(name + " : " + message + '\t' + " [ " + timestamp + " ] " + '\n')
    return redirect(url_for('sent', file = filename, path = path))

@app.route('/sent', methods=['GET'])
def confirm_send():
	filename = request.values.get('file')
	path = request.values.get('path')
	if not path or not filename:
		abort(400, 'Missing parameters')
	try:
		file_path = os.path.join(path, filename + ".txt")
		with open(file_path, 'r') as file:
			message = file.read()
	except FileNotFoundError:
		abort(404, 'file not found')
	return render_template('confirm_send.html', message = message)