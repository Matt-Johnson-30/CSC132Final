from flask import Flask
from flask_restful import Resource, Api, reqparse
from pygame import mixer
from random import randint
import os

mixer.init()

app = Flask(__name__)
api = Api(app)

class MusicPlayer(object):
    def __init__(self):
        self.songlist = os.listdir("/home/pi/Documents/csc 132/Final/Library")
        self.queue = []
        self.queue.append(self.songlist[0])
        
    # take the input from the server and complete the action
    def decode(self, function, song = ""):
        if function == "play":
            mixer.music.unpause()
        elif function == "pause":
            mixer.music.pause()
        elif function == "skip":
            try:
                self.playsong(self.queue[0])
            except:
                self.playsong(self.songlist[randint(19)])
       # when functions are sent the song is blank so it makes sure it doesnt add "" to the queue
        else:
            if song != "":
                self.queue.append(song)
                print self.queue

    def playsong(self, songname):     
        location = "/home/pi/Documents/csc 132/Final/Library/{}".format(songname)
        self.queue.remove(songname)
            # PLAY SONG
        mixer.music.load(location)
        mixer.music.set_volume(1)
        mixer.music.play()
            
    def playnext(self):
        self.playsong(self.queue[0])
    
    def play_pause(self, state):
        if state == "1":
            mixer.music.unpause()
        elif state == "0":
            mixer.music.pause()
              

class Test(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('song', type=str)       # looks for the argument holding song name
        parser.add_argument('function', type=str)   # looks for the argument holding function
        args = parser.parse_args()
        print args
        # if song is not in queue doesn't crash
        try:
            print m.queue[0]
            m.playsong(m.queue[0])
        except:
            m.decode(args['function'], args['song'])
            if mixer.get_busy() == True:
                m.playnext()
        return

class SongList(Resource):
    def get(self):
        return #a list of all of the songs

m = MusicPlayer()

api.add_resource(Test, '/')
api.add_resource(SongList, '/list')


app.run(debug=True, host='0.0.0.0')

# python api.py
# on this pi, open another terminal and type 'ifconfig'
#   to get the private ip address
