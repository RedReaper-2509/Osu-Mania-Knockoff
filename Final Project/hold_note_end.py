import pygame as pg

class Hold_Note_end(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        img_path='assets/hold_notes/hold_note_end.png'
        self.image=pg.image.load(img_path)
        self.Image=pg.transform.scale(self.image, (size, size))
        self.rect=self.image.get_rect(topleft=pos)

        

    def update(self, y_shift):
        self.rect.y+=y_shift
        