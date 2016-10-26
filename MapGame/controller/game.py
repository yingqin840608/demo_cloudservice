from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
#import time

class gameMap(Widget):
    def __init__(self):
        
        self.curtime = 0
        self.gamemode=0
        self.map=None
        self.playersnum = 0
        self.players=[]
    
    def initPlayer(self, players):
        self.players = players

    def paintMap(self):
        pass

    def initMap(self):
        pass

    def startGame(self, **kvargs):
        pass
class MapGame(App):
    def build(self):
        return MapGame()

if __name__ == '__main__':
    game().run()

