import pygame as pg


class Judgement(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos=pos
        self.size=size
        self.no_hit(self.pos, self.size)


   


    def no_hit(self, pos, size):
        self.img_path='assets/judgement/no_hit.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def miss(self, pos, size):
        self.img_path='assets/judgement/miss.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def bad(self, pos, size):
        self.img_path='assets/judgement/bad.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def good(self, pos, size):
        self.img_path='assets/judgement/good.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def great(self, pos, size):
        self.img_path='assets/judgement/great.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def perfect(self, pos, size):
        self.img_path='assets/judgement/perfect.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    def marvelous(self, pos, size):
        self.img_path='assets/judgement/marvelous.png'
        self.image=pg.image.load(self.img_path)
        self.image=pg.transform.scale(self.image, (size, 50))
        self.rect=self.image.get_rect(topleft=pos)

    
    

    def update(self, judge):
        if judge=='no_hit':
            self.no_hit(self.pos, self.size)
        elif judge=='miss':
            self.miss(self.pos, self.size)
        elif judge=='bad':
            self.bad(self.pos, self.size)
        elif judge=='good':
            self.good(self.pos, self.size)
        elif judge=='great':
            self.great(self.pos, self.size)
        elif judge=='perfect':
            self.perfect(self.pos, self.size)
        elif judge=='marvelous':
            self.marvelous(self.pos, self.size)
