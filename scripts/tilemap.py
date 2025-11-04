import pygame


NEIGHBOR_OFFSETS = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(0,0),(-1,1),(0,1),(1,1)]
PHYSICS_TILE = {"grass"}

class Tilemap():
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        # all tiles re on a grid
        self.tilemap = {} # NOTE: only handle physics with grid tiles
        # things that might not come up with the grid
        self.offgrid_tiles = []
        
        # NOTE here can make a class Tile() pass this attributes and get tiles
        for i in range(10): # variant : goone
            #vertical
            self.tilemap[f"{str(3 + i)};10"] = {"type":"grass", "variant":0, "pos":(3+i,10)}
            # horizontal
            self.tilemap[f"10;{str(5 + i)}"] = {"type":"grass", "variant":0, "pos":(10,5+i)}
        
    def tiles_around(self, position):
        """pass pixel position , convert to grid position
        then check tiles around if they are in tilemap
        returns tiles
        
        filters tiles to nearby"""
        tiles = []
        tile_location = (int( position[0]// self.tile_size), int( position[1]// self.tile_size))
        for offsets in NEIGHBOR_OFFSETS:
            check_location = str(tile_location[0]+offsets[0])+";"+str(tile_location[1]+offsets[1]) # make a tilemap dict key
            if check_location in self.tilemap:
                tiles.append(self.tilemap[check_location])
    

        return tiles
    
    
    def physics_rects_around(self, position):
        """ gets players position
        returns a list of collision rects"""

        rects = []
        for tile in self.tiles_around(position): # looking in a set is more efficient
            if tile["type"] in PHYSICS_TILE:
                rects.append(pygame.Rect(tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size, self.tile_size, self.tile_size))
        
        # TODO remove (purpose: collision fix)
        for rect in rects:
            pygame.draw.rect(self.game.screen, (255,0,0), rect, width=1)
        return rects 
    
     
    def render(self, dest_surf):
        # Mostly decorations are off-grid so we put it in render earlier than main map
        for tile in self.offgrid_tiles:
            self.blit(self.game.assets[tile["type"]][tile["varriant"]], tile["pos"])
        
        for location in self.tilemap: # we get all keys when iterate through dict
            tile = self.tilemap[location]
            dest_surf.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["pos"][0]*self.tile_size, tile["pos"][1]*self.tile_size)) # return grass image
        
        
