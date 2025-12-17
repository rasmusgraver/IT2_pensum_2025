import pygame as pg
import os
from constants import *

class NinjaFrog:
    IMAGE_DIR = os.path.join(os.path.dirname(__file__), "MainCharacters", "NinjaFrog")

    def getImageSpriteList(self, image_name):
        full_image = pg.image.load(os.path.join(self.IMAGE_DIR, image_name))
        # Finn antall frames basert på bildebredde
        frame_width = 32
        num_frames = full_image.get_width() // frame_width
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            frame = full_image.subsurface(pg.Rect(i * frame_width, 0, frame_width, 32))
            frames.append(frame)
        return frames


    def __init__(self, x, y):
        self.idle_frames = self.getImageSpriteList("Idle (32x32).png")
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.idle_frames

        # Animasjonsvariabler (som finner rett bilde å vise - i en loop)
        self.current_frame = 0
        self.frame_counter = 0
        
        # Sjekker om vi facer høyre eller venstre (speilvendt bilde eller ikke)
        self.hoyre = True

        # Typisk i PyGame: Bruker en "rect" for å plassere bildet på rett sted på skjermen (se draw metoden)        
        self.rect = self.frames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, keys=None):
        if keys:
            if keys[pg.K_RIGHT]:
                self.hoyre = True
                self.rect.x += 5
            elif keys[pg.K_LEFT]:
                self.hoyre = False
                self.rect.x -= 5

        self.frame_counter += 1
        if self.frame_counter >= 10:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def draw(self, surface):
        """Tegner karakteren på skjermen"""
        current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis han står til venstre
        if self.hoyre == False:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)
        
        surface.blit(current_frame_image, self.rect)
    
