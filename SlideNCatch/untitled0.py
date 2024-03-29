import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("house.png")

class Cage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cage2")
        self.setSize(50, 50)
        self.position(320,400)
        self.moveSpeed = 6