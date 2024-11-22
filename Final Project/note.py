import pygame as pg

class Note(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        img_path='assets/note.png'
        self.image=pg.image.load(img_path)
        self.image=pg.transform.scale(self.image, (size, size))
        self.rect=self.image.get_rect(topleft=pos)
        self.location=self.rect.y


    def hit(self,score):
        if 510<self.location<685:
            score+=300
            self.kill()
        



        

    def points(self):
        if self.rect.y<=520:
            pass
            
    def update(self, y_shift):
        self.rect.y+=y_shift
        
            