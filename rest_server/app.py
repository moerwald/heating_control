#!/usr/bin/python

from flask import Flask
from flask import jsonify
import Adafruit_DHT
import time


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

class Room:
   def __init__ (self, name, temp, humididy, datetime):
       self.Name = name
       self.Temperature = temp
       self.Humidity = humididy
       self.DateTime = datetime



@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
   return jsonify({'tasks': tasks})

@app.route('/rooms/bedroom/temp', methods=['GET'])
def get_temp():
   humdity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
   humdity -= 7
   now = time.strftime("%d/%m/%Y-%H:%M:%S")
   room = Room('bedroom', round(temperature,2), round(humdity,2), now)
   return jsonify({'room': room.__dict__})

def main(argv=None):
   app.run(debug=True)
   print('XXXXX')


if __name__ == '__main__':
   main()
