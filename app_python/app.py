from flask import Flask
from datetime import datetime
from pytz import timezone
import os

app = Flask(__name__)

tz = timezone('Europe/Moscow')

@app.route('/')
def hello():
    add_visit()
    return 'Now in Moscow: ' + datetime.now(tz).strftime('%d-%m-%Y %H:%M:%S')


@app.route('/visits')
def get_visits():
    if not os.path.isfile("visits_count"):
        file = open("visits_count", "w")
        file.write("")
        file.close()
    file = open("visits_count", "r")
    visits = str(file.read())
    file.close()
    return visits

def add_visit():
    visits = get_visits()
    visits += datetime.now(tz).strftime('%d-%m-%Y %H:%M:%S') + '\n'
    file = open("visits_count", "w")
    file.write(str(visits))
    file.close()
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)