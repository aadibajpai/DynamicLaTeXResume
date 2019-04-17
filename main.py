import datetime
from flask import Flask, redirect
from updater import update_resume

app = Flask(__name__, static_folder='')

update_date = 0


@app.route('/')
def hello():
    return redirect('https://aadibajpai.me')


@app.route('/aadi_resume.pdf')
def resume():
    global update_date
    print(f"resume last updated at {update_date}")
    date_now = datetime.date.today()
    if date_now != update_date:
        update_resume()
        update_date = date_now
        print(f"resume updated now at {update_date}")
    return app.send_static_file('aadi_resume.pdf')


if __name__ == '__main__':
    app.run()
