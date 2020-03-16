from flask import Flask, render_template, request, redirect, url_for, Response
#from model import User
# from wtforms import StringField, Form, SubmitField
# from wtforms.validators import DataRequired
# import quickstart
# import sqlite3
# db = 'challenge.db'
# conn = sqlite3.connect(db)
# c = conn.cursor()
from camera import VideoCamera

application = app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('home.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host= '192.168.1.137', port=9000, debug=False)
