from settings import *
import game

class Display():
    def __init__(self):
        pygame.display.set_caption("Platformer Title")
        self.screen = pygame.display.set_mode(SC_SIZE)
        # a second surface that will zoom in to make objects visable
        # NOTE: render all into smaller surface then scale it up to main screen
        self.display_surface = pygame.Surface(DISPLAY_SIZE)
        
        self.clock = pygame.Clock()
        self.game = game.Game(self.display_surface)
        
        self._running = True
        

    def run(self):
        while self._running:
            self._running = self.game.update()
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()),(0,0))
            self.clock.tick(FPS)
            
            
             
            
if __name__ == "__main__":
    display = Display()
    display.run()