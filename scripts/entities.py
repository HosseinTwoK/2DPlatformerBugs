import pygame
from settings import *
import game

class PhysicsEntity():
    def __init__(self,
                 game:game.Game,
                 entity_type:str,
                 entity_position,
                 entity_size):
        
        self.game = game
        self.type = entity_type
        self.position = list(entity_position) # cuz it comes in tuple
        self.velocity = [0,0]
        self.entity_size = entity_size
        self.collisions = {'up':False, 'down':False, 'right':False, 'left':False}
    
    def rect(self): # make one dinamically 
        return pygame.Rect(self.position[0], self.position[1]+self.entity_size[1], self.entity_size[0], self.entity_size[1])
    
    def update(self, tilemap, movement=(0,0)):
        # to check what dirction has collision
        self.collisions = {'up':False, 'down':False, 'right':False, 'left':False}

        
        # TODO change physics later
        frame_movement = (movement[0]+self.velocity[0], movement[1]+self.velocity[1])
        
        self.position[0] += frame_movement[0]
        # COLLISION CHECK WITH NEARBY TILES
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0: # moving right
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0: # move left
                    entity_rect.left = rect.right
                    self.collisions['left'] = True    
                self.position[0] = entity_rect.x
            
        self.position[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0: # moving bottom
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                    
                if frame_movement[1] < 0: # move top
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                    
                self.position[1] = entity_rect.y - self.entity_size[1]
        
        # Gravity  
        self.velocity[1] = min(MAX_VERTICAL_ACCELERATION, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        
    def render(self , dest_surface):
        dest_surface.blit(self.game.assets[self.type],self.position)
        