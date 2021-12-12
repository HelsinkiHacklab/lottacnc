from flask.helpers import url_for
from app import app
from flask import request, render_template, redirect

from app import serialport, init_serial
import serial

from datetime import datetime

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == 'GET':
		return render_template('index.html', nav="main")

	data = request.form['gcode'].encode('iso-8859-1')
	# data = "%\r\n" + data + "\r\n%\r\n"
	data = data.rstrip('\r\n'.encode()) + '\r\n'.encode()
	data = data.replace('\r\n(TIMESTAMP)\r\n'.encode(), '\r\n'.encode() + datetime.now().strftime("(%Y %m %d %H %M %S)").encode() + '\r\n'.encode())
	# init_serial() # for testing

	# TODO: G-code lint right about here

	if not serialport.cd:
		return render_template('index.html', nav="main", gcode=request.form['gcode'], error="Lotta is not ready. Hit PRGM, I/O, Read.")

	try:
		# TODO: Maybe this should be dynamic and line by line?
		serialport.write(data)
	except serial.SerialException as e:
		return render_template('index.html', nav="main", gcode=request.form['gcode'], error="Serial port error, try again (%s)" % e)
	except AttributeError as e:
		try:
			init_serial()
		except:
			return render_template('index.html', nav="main", gcode=request.form['gcode'], error="Serial port error, try again (%s)" % e)
	return render_template('index.html', nav="main", gcode=request.form['gcode'], message="Transfer successful (Sent %d bytes)" % len(data))

@app.route('/help')
def init():
	return render_template('help.html', nav="guides")

@app.route('/G43')
def length_compensation():
	return render_template('length_compensation.html', nav="helpers")

@app.route('/reset-serial-out')
def reset_serial_line_out():
	serialport.reset_output_buffer()
	return redirect(url_for("index"))

