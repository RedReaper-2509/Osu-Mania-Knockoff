import pygame as pg
from note import Note

class Note_Zone(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos=pos
        self.size=size
        self.is_pressed=False
        
        self.img_path='assets/note_zone/note_zone_reg.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, size))
        self.rect=self.image.get_rect(topleft=pos)
        
        

    def press(self, pos, size):
        self.img_path='assets/note_zone/note_zone_hit.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, size))
        self.rect=self.image.get_rect(topleft=pos)




    def release(self, pos, size):
        self.img_path='assets/note_zone/note_zone_reg.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, size))
        self.rect=self.image.get_rect(topleft=pos)


    
    

    def update(self, zone_event):
        if zone_event==True:
            self.press(self.pos, self.size)
            
        

        else:
            self.release(self.pos, self.size)
            
        

