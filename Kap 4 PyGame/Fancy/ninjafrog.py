import pygame as pg
import os
from constants import *

class NinjaFrog:
    IMAGE_DIR = os.path.join(os.path.dirname(__file__), "MainCharacters", "NinjaFrog")

    def getImageSpriteList(self, image_name:str, frame_width:int) -> list[pg.Surface]:
        full_image = pg.image.load(os.path.join(self.IMAGE_DIR, image_name))
        # Finn antall frames basert på bildebredde
        num_frames = full_image.get_width() // frame_width
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # OBS: ANTAR at bildene er kvadratiske - bruker frame widht både som høye og bredde
            frame = full_image.subsurface(pg.Rect(i * frame_width, 0, frame_width, frame_width))
            frames.append(frame)
        return frames
    
    def getSingleSpriteImage(self, image_name) -> pg.Surface:
        full_image = pg.image.load(os.path.join(self.IMAGE_DIR, image_name))
        return full_image


    def __init__(self, x, y):
        self.frames_idle = self.getImageSpriteList("Idle (32x32).png", 32)
        self.frames_double_jump = self.getImageSpriteList("Double Jump (32x32).png", 32)
        self.img_falling = self.getSingleSpriteImage("Fall (32x32).png")
        self.img_jumping = self.getSingleSpriteImage("Jump (32x32).png")

        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle

        # Setter opp y-farten:
        self.vy = 0
        self.jumping = False
        self.double_jump = False

        # Animasjonsvariabler (som finner rett bilde å vise - i en loop)
        self.current_frame = 0
        self.frame_counter = 0
        
        # Sjekker om vi facer høyre eller venstre (speilvendt bilde eller ikke)
        self.hoyre = True

        # Typisk i PyGame: Bruker en "rect" for å plassere bildet på rett sted på skjermen (se draw metoden)        
        self.rect = self.frames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def falling(self, jumping_key):
        # Sjekk om vi er oppe i lufta, eller hopper:
        if self.rect.bottom < BAKKE_HOYDE or self.jumping:
            # La gravitasjonen gjøre sin jobb:
            self.vy += GRAVITASJON
            self.rect.y += round(self.vy)

        # Under bakken: Få ham opp igjen:
        if self.rect.bottom > BAKKE_HOYDE:
            self.vy = 0
            self.rect.bottom = BAKKE_HOYDE
            self.jumping = False
            self.double_jump = False
            self.frames = self.frames_idle
            self.frame_counter = 0
            self.current_frame = 0
        
        if jumping_key:
            if not self.jumping:
                # Single jump:
                self.jumping = True
                self.vy -= JUMP_SPEED
            elif not self.double_jump:
                # double:
                self.double_jump = True
                if self.vy > 0:
                    # Hvis du er på vei ned, så stopp det:
                    self.vy = 0
                self.vy -= DOUBLE_JUMP_SPEED
                self.frames = self.frames_double_jump
                self.frame_counter = 0
                self.current_frame = 0

    def update(self, keys, jumping):
        if keys[pg.K_RIGHT]:
            self.hoyre = True
            self.rect.x += X_SPEED
        elif keys[pg.K_LEFT]:
            self.hoyre = False
            self.rect.x -= X_SPEED
        
        self.falling(jumping)

        self.frame_counter += 1
        if self.frame_counter >= FRAME_COUNTER_SPEED:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def draw(self, surface):

        if not self.double_jump and self.vy:
            # Vi er på vei opp eller ned, uten double jump:
            # Bruk enkelt-bilde (ikke liste av bilder):
            if self.vy > 0:
                current_frame_image = self.img_falling
            else:
                current_frame_image = self.img_jumping
        else:
            # Få det fra en liste av bilder: Enten idle eller double jump:
            current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis han står til venstre
        if self.hoyre == False:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Litt debug: Tegn rect til frosken:
        farge = WHITE
        if self.double_jump:
            farge=RED
        elif self.jumping:
            farge=ORANGE            
        elif self.vy == 0:
            farge=YELLOW
        # pg.draw.rect(surface, farge, self.rect)

        surface.blit(current_frame_image, self.rect)
    
