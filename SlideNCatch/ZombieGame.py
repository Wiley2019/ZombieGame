import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("house.png")
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.score = 0
        
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.cage = Cage(self)
        
        
        self.zombies = []
        
        for i in range(10):
            self.zombies.append(Zombie(self))
        
        self.sprites = [self.cage, self.zombies, self.lblScore, 
        self.lblTime]
        self.sndZombie = simpleGE.Sound("Zombie Sound.wav")
   
    def process(self):
        for zombie in self.zombies:
            if self.cage.collidesWith(zombie):
                self.sndZombie.play()
                zombie.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()
                
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
             
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)
  

class Cage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cage2.png")
        self.setSize(50, 50)
        self.position = (320,400)
        self.moveSpeed = 6
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed

class Zombie(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)               
        self.setImage("ZombieLeftX.png")
        self.setSize(75,75)
        self.reset()
        
    def reset(self):
        self.x = 0
        self.y = random.randint(40, self.screenHeight)
        self.dx = random.randint(2, 9)
        
    def checkBounds(self):
        if self.right > self.screenWidth:
            self.reset()
        
        
        
def main():
    game = Game()
    game.start()
    

if __name__ == "__main__":
    main()
    