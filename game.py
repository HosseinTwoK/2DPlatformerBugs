from settings import *
from scripts.utilities import *
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game():
    def __init__(self, display_surface):
        self.screen = display_surface
        self.assets = {
            "grass": load_images("tiles","grass"),
            "Player": load_image("player","idle","idle1.png")
        }
        
        self.tilemap = Tilemap(self)       
        
        self.movement = [False, False]
        self.player = PhysicsEntity(self, "Player", (50,120), (16,16))
        

    def blits(self):
        self.screen.fill((0,0,0))
        self.tilemap.render(self.screen)

    def update(self):
        self.blits()
        
        # movement logic:        
        # 0 - 0 = 0 
        # 1 - 0 = 1     right direction
        # 0 - 1 = -1    left direction
        # 1 - 1 = 0
        self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
        self.player.render(self.screen)
        
        #print(self.tilemap.physics_rects_around(self.player.position))

        # # TODO remove
        # rects = self.tilemap.physics_rects_around(self.player.position)
        # for r in rects:
        #     pygame.draw.rect(self.screen, (255,0,0), r, width=1)
        # TODO remove (purpose: collision fix)          
        rect = self.player.rect()
        pygame.draw.rect(self.screen, (255,0,0), rect, width=1)
        
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                return False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.movement[0] = True
                if event.key == K_RIGHT:
                    self.movement[1] = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    self.movement[0] = False
                if event.key == K_RIGHT:
                    self.movement[1] = False
            

        
        pygame.display.update()

        return True