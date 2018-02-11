from roboarm import Arm
from flask import Flask

app = Flask(__name__)
arm = Arm()

@app.route('/elbow/up/<int:timeout>')
def elbow_up(timeout):
    arm.elbow.up(timeout=timeout)
    return 'OK'

@app.route('/elbow/down/<int:timeout>')
def elbow_down(timeout):
    arm.elbow.down(timeout=timeout)
    return 'OK'

@app.route('/grips/open/<int:timeout>')
def grips_open(timeout):
    arm.grips.open(timeout=timeout)
    return 'OK'

@app.route('/grips/close/<int:timeout>')
def grips_close(timeout):
    arm.grips.close(timeout=timeout)
    return 'OK'

@app.route('/wrist/up/<int:timeout>')
def wrist_up(timeout):
    arm.wrist.up(timeout=timeout)
    return 'OK'

@app.route('/wrist/down/<int:timeout>')
def wrist_down(timeout):
    arm.wrist.down(timeout=timeout)
    return 'OK'

@app.route('/shoulder/up/<int:timeout>')
def shoulder_up(timeout):
    arm.shoulder.up(timeout=timeout)
    return 'OK'

@app.route('/shoulder/down/<int:timeout>')
def shoulder_down(timeout):
    arm.shoulder.down(timeout=timeout)
    return 'OK'

@app.route('/base/rotate_clock/<int:timeout>')
def rotate_clock(timeout):
    arm.base.rotate_clock(timeout=timeout)
    return 'OK'

@app.route('/base/rotate_counter/<int:timeout>')
def rotate_counter(timeout):
    arm.base.rotate_counter(timeout=timeout)
    return 'OK'

@app.route('/led/on/<int:timeout>')
def led_on(timeout):
    arm.led.on(timeout=timeout)
    return 'OK'

@app.route('/led/off/<int:timeout>')
def led_off(timeout):
    arm.led.off(timeout=timeout)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')