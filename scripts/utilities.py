import pygame
import os

BASE_ASSET_PATH = os.path.join("assets")


def load_image(*path):
    img = pygame.image.load(os.path.join(BASE_ASSET_PATH,*path)).convert()
    img.set_colorkey((0,0,0)) # to transparent black bg after convert()
    return img

def load_images(*path):
    images = []
    for img_name in sorted(os.listdir(os.path.join(BASE_ASSET_PATH,*path))): # NOTE we sort it cuz in linux it may be get images high to low number but in windows it gets low to high
        images.append(load_image(*path,img_name))

    return images
