from roboarm import Arm
from flask import Flask

app = Flask(__name__)
arm = Arm()

@app.route('/elbow/up/<timeout>')
def elbow_up(timeout):
    arm.elbow.up(timeout=float(timeout))
    return 'OK'

@app.route('/elbow/down/<timeout>')
def elbow_down(timeout):
    arm.elbow.down(timeout=float(timeout))
    return 'OK'

@app.route('/grips/open/<timeout>')
def grips_open(timeout):
    arm.grips.open(timeout=float(timeout))
    return 'OK'

@app.route('/grips/close/<timeout>')
def grips_close(timeout):
    arm.grips.close(timeout=float(timeout))
    return 'OK'

@app.route('/wrist/up/<timeout>')
def wrist_up(timeout):
    arm.wrist.up(timeout=float(timeout))
    return 'OK'

@app.route('/wrist/down/<timeout>')
def wrist_down(timeout):
    arm.wrist.down(timeout=float(timeout))
    return 'OK'

@app.route('/shoulder/up/<timeout>')
def shoulder_up(timeout):
    arm.shoulder.up(timeout=float(timeout))
    return 'OK'

@app.route('/shoulder/down/<timeout>')
def shoulder_down(timeout):
    arm.shoulder.down(timeout=float(timeout))
    return 'OK'

@app.route('/base/rotate_clock/<timeout>')
def rotate_clock(timeout):
    arm.base.rotate_clock(timeout=float(timeout))
    return 'OK'

@app.route('/base/rotate_counter/<timeout>')
def rotate_counter(timeout):
    arm.base.rotate_counter(timeout=float(timeout))
    return 'OK'

@app.route('/led/on/<timeout>')
def led_on(timeout):
    arm.led.on(timeout=float(timeout))
    return 'OK'

@app.route('/led/off/<timeout>')
def led_off(timeout):
    arm.led.off(timeout=float(timeout))
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')