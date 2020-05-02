from flask import Flask, render_template, request, redirect, url_for, Response
#from model import User

from forms import LoginForm
from camera import VideoCamera
import os
import User
SECRET_KEY = os.urandom(32)

application = app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
current_user = User.User()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print (form.data)
    if form.data['username'] != '':
        un = form.data['username']
        pw = form.data['password']
        print(un)
        print(pw)
        auth = current_user.check_password(un,pw)
        print (auth)
        print(current_user.check_authentication())
        if current_user.check_authentication():
            print("REDIRECT")
            return redirect('/')
    return render_template('login.html', title='Login', form=form)

@app.route('/', methods=['GET','POST'])
def index():
    print(current_user.check_authentication())
    if current_user.check_authentication():
        return render_template('home.html')
    else:
        return redirect('/login')


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
