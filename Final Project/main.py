from chart import*
import pygame as pg, sys

from map import Map




pg.init()
screen=pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Osu Mania Knockoff")


class Osu:
    def __init__(self, screen, width, height):
        self.screen_size=WIDTH, HEIGHT
        self.screen=screen
        self.clock=pg.time.Clock()
        self.bg_img=pg.image.load('assets/Background.png')
        self.bg_img=pg.transform.scale(self.bg_img, (width, height))
        self.track_img = pg.image.load('assets/note_track.png')
        self.track_img=pg.transform.scale(self.track_img, (300, 700))
        self.left_press=False
        self.down_press=False
        self.up_press=False
        self.right_press=False
        self.game_event = False
        self.key_press=None
        self.WHITE=(225, 225, 225)
        self.song=pg.mixer.Sound('song.mp3')
        

    def main(self):
        self.key_press=pg.key.get_pressed()
        mp = Map(chart_easy, self.screen)
        while True:
            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit( self.track_img, (200, 0))

        
            
            

            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_b and self.game_event!='running':
                        self.game_event='running'
                        self.song.play()
                    if event.key==pg.K_d and self.game_event=='running':
                        self.left_press=True
                    if event.key==pg.K_f and self.game_event=='running':
                        self.down_press=True
                    if event.key==pg.K_j and self.game_event=='running':
                        self.up_press=True
                    if event.key==pg.K_k and self.game_event=='running':
                        self.right_press=True
                elif event.type==pg.KEYUP:
                    if event.key==pg.K_d and self.game_event=='running':
                        self.left_press=False
                    if event.key==pg.K_f and self.game_event=='running':
                        self.down_press=False
                    if event.key==pg.K_j and self.game_event=='running':
                        self.up_press=False
                    if event.key==pg.K_k and self.game_event=='running':
                        self.right_press=False

                
            mp.update( self.game_event, self.left_press, self.down_press, self.up_press, self.right_press)
            pg.display.update()
            self.clock.tick(120)


if __name__== "__main__":
    play =Osu(screen, WIDTH, HEIGHT)
    play.main()