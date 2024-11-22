import pygame as pg
from note_zone import Note_Zone
from note import Note
from judgment import Judgement
from hold_note_end import Hold_Note_end
from hold_note_mid import Hold_Note_mid
from chart import note_size, HEIGHT

class Map:
    def __init__(self, map_data,screen):
        self.screen=screen
        self.map_data=map_data
        self.num_of_notes=0
        self.judge_size=100
        self.judge_x=0
        self.judge_y=0
        self.one_second=0
        self.judge='no_hit'
        self.current_y=0
        self.chart_speed=10
        self.game_event = False
        self.score=0000000
        self.left_press=0
        self.combo=0
        self.left=False
        self.left2=True
        self.down=False
        self.down2=True
        self.up=False
        self.up2=True
        self.right=False
        self.right2=True
        self.song_length=84
        self.time_left=self.song_length
        self.frames=0
        self.max_score=1000000
        self._setup_map(map_data)
        
        #score
        self.font=pg.font.Font(None, 45)
        self.score_font=pg.font.Font(None, 70)
        self.timer_font=pg.font.Font(None, 45)
        
        
    
        

    

    def _setup_map(self,chart):

        self.judgement=pg.sprite.GroupSingle()

        #note
        self.note_left=pg.sprite.Group()
        self.hold_note_left_end=pg.sprite.Group()
        self.hold_note_left_mid=pg.sprite.Group()
        self.note_down=pg.sprite.Group()
        self.hold_note_down_end=pg.sprite.Group()
        self.hold_note_down_mid=pg.sprite.Group()
        self.note_up=pg.sprite.Group()
        self.hold_note_up_end=pg.sprite.Group()
        self.hold_note_up_mid=pg.sprite.Group()
        self.note_right=pg.sprite.Group()
        self.hold_note_right_end=pg.sprite.Group()
        self.hold_note_right_mid=pg.sprite.Group()

        #note zone sprites
        self.note_zone_left=pg.sprite.Group()
        self.note_zone_down=pg.sprite.Group()
        self.note_zone_up=pg.sprite.Group()
        self.note_zone_right=pg.sprite.Group()

        #note zones
            #left
        note_zone_left=Note_Zone((200, 600), note_size)
        self.note_zone_left.add(note_zone_left)
            #down
        note_zone_down=Note_Zone((275, 600), note_size)
        self.note_zone_down.add(note_zone_down)
            #up
        note_zone_up=Note_Zone((350, 600), note_size)
        self.note_zone_up.add(note_zone_up)
            #right
        note_zone_right=Note_Zone((425, 600), note_size)
        self.note_zone_right.add(note_zone_right)


       


        #make the chart
        for row_index, row in enumerate(chart):
            for col_index, cell in enumerate(row):
                x, y=col_index*note_size+200, (row_index/2)*note_size -(800)
                #left note
                if cell=="X" and col_index==0:
                    note=Note((x, y), note_size)
                    self.note_left.add(note)
                    self.num_of_notes+=1
                elif cell=="E" and col_index==0:
                    note=Hold_Note_end((x, y), note_size)
                    self.hold_note_left_end.add(note)
                    self.num_of_notes+=1
                elif cell=="I" and col_index==0:
                    note=Hold_Note_mid((x, y), note_size)
                    self.hold_note_left_mid.add(note)
                    self.num_of_notes+=1
                    #down note
                if cell=="X" and col_index==1:
                    note=Note((x, y), note_size)
                    self.note_down.add(note)
                    self.num_of_notes+=1
                elif cell=="E" and col_index==1:
                    note=Hold_Note_end((x, y), note_size)
                    self.hold_note_down_end.add(note)
                    self.num_of_notes+=1
                elif cell=="I" and col_index==1:
                    note=Hold_Note_mid((x, y), note_size)
                    self.hold_note_down_mid.add(note)
                    self.num_of_notes+=1
                    #up note
                if cell=="X" and col_index==2:
                    note=Note((x, y), note_size)
                    self.note_up.add(note)
                    self.num_of_notes+=1
                elif cell=="E" and col_index==2:
                    note=Hold_Note_end((x, y), note_size)
                    self.hold_note_up_end.add(note)
                    self.num_of_notes+=1
                elif cell=="I" and col_index==2:
                    note=Hold_Note_mid((x, y), note_size)
                    self.hold_note_up_mid.add(note)
                    self.num_of_notes+=1
                    #right note
                if cell=="X" and col_index==3:
                    note=Note((x, y), note_size)
                    self.note_right.add(note)
                    self.num_of_notes+=1
                elif cell=="E" and col_index==3:
                    note=Hold_Note_end((x, y), note_size)
                    self.hold_note_right_end.add(note)
                    self.num_of_notes+=1
                elif cell=="I" and col_index==3:
                    note=Hold_Note_mid((x, y), note_size)
                    self.hold_note_right_mid.add(note)
                    self.num_of_notes+=1

        
        

    





    def update( self, game_event, left_press, down_press, up_press, right_press):
        if self.judge=='no_hit':
            self.judge_size=50
        elif self.judge=='miss':
            self.judge_size=136
        elif self.judge=='bad':
            self.judge_size=124
        elif self.judge=='good':
            self.judge_size=178
        elif self.judge=='great':
            self.judge_size=192
        elif self.judge=='perfect':
            self.judge_size=258
        elif self.judge=='marvolous':
            self.judge_size=378
        
        if self.judge!='no_hit'and self.one_second<120:
            self.one_second+=1
        elif self.judge!='no_hit'and self.one_second<=120:
            self.one_second=0
            self.judge='no_hit'



        judgement=Judgement((350-(self.judge_size/2),400),self.judge_size)
        self.judgement.add(judgement)
        text=self.score_font.render(f'{str(1)if self.time_left>59 else str(0)}:{str(self.time_left-60 if self.time_left>59 else self.time_left)}', False, (225, 225, 225))
        self.screen.blit(text, (50, 50))
        if game_event=='running':
            if self.time_left>0:
                self.frames+=1
                self.time_left=self.song_length-(self.frames//120)
            
        
        #left
        if left_press and self.left2:
            self.left=True
        
        if self.left==True:
            for note in self.note_left.sprites():
                if 610>=note.rect.top>=580 and left_press:
                    self.score+=((100000/self.num_of_notes))
                    self.combo+=1
                    self.judge='perfect'
                    self.one_second=0
                    note.kill()
                    
                elif 640>=note.rect.top>=560 and left_press:
                    self.score+=((100000/self.num_of_notes)-((100000/self.num_of_notes)/3))
                    self.combo+=1
                    self.judge='great'
                    self.one_second=0
                    note.kill()
                elif 650>=note.rect.top>=550 and left_press:
                    self.score+=((100000/self.num_of_notes)/3)
                    self.combo+=1
                    self.judge='good'
                    note.kill()
                elif 670>=note.rect.top>=530 and left_press:
                    self.score+=((100000/self.num_of_notes)/6)
                    self.combo+=1
                    self.judge='bad'
                    note.kill()
                    
        self.left=False
        self.left2=False

        if left_press==False:
            self.left2=True
        #down
        if down_press and self.down2:
            self.down=True
        
        if self.down==True:
            for note in self.note_down.sprites():
                if 610>=note.rect.top>=580 and down_press:
                    self.score+=((100000/self.num_of_notes))
                    self.combo+=1
                    self.judge='perfect'
                    note.kill()
                elif 640>=note.rect.top>=560 and down_press:
                    self.score+=((100000/self.num_of_notes)-((100000/self.num_of_notes)/3))
                    self.combo+=1
                    self.judge='great'
                    note.kill()
                elif 650>=note.rect.top>=550 and down_press:
                    self.score+=((100000/self.num_of_notes)/3)
                    self.combo+=1
                    self.judge='good'
                    note.kill()
                elif 670>=note.rect.top>=530 and down_press:
                    self.score+=((100000/self.num_of_notes)/6)
                    self.combo+=1
                    self.judge='bad'
                    note.kill()
                    
        self.down=False
        self.down2=False

        if down_press==False:
            self.down2=True


        #up
        if up_press and self.up2:
            self.up=True
        
        if self.up==True:
            for note in self.note_up.sprites():
                if 610>=note.rect.top>=580 and up_press:
                    self.score+=((100000/self.num_of_notes))
                    self.combo+=1
                    self.judge='perfect'
                    note.kill()
                elif 640>=note.rect.top>=560 and up_press:
                    self.score+=((100000/self.num_of_notes)-((100000/self.num_of_notes)/3))
                    self.combo+=1
                    self.judge='great'
                    note.kill()
                elif 650>=note.rect.top>=550 and up_press:
                    self.score+=((100000/self.num_of_notes)/3)
                    self.combo+=1
                    self.judge='good'
                    note.kill()
                elif 670>=note.rect.top>=530 and up_press:
                    self.score+=((100000/self.num_of_notes)/6)
                    self.combo+=1
                    self.judge='bad'
                    note.kill()
                    
        self.up=False
        self.up2=False

        if up_press==False:
            self.up2=True


        #right
        if right_press and self.right2:
            self.right=True
        
        if self.right==True:
            for note in self.note_right.sprites():
                if 610>=note.rect.top>=580 and right_press:
                    self.score+=((100000/self.num_of_notes))
                    self.combo+=1
                    self.judge='perfect'
                    note.kill()
                elif 640>=note.rect.top>=560 and right_press:
                    self.score+=((100000/self.num_of_notes)-((100000/self.num_of_notes)/3))
                    self.combo+=1
                    self.judge='great'
                    note.kill()
                elif 650>=note.rect.top>=550 and right_press:
                    self.score+=((100000/self.num_of_notes)/3)
                    self.combo+=1
                    self.judge='good'
                    note.kill()
                elif 670>=note.rect.top>=530 and right_press:
                    self.score+=((100000/self.num_of_notes)/6)
                    self.judge='bad'
                    self.combo+=1
                    note.kill()
                    
        self.right=False
        self.right2=False

        if right_press==False:
            self.right2=True

        for note in self.hold_note_left_end.sprites():
            if 675>=note.rect.top>=600 and left_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_left_mid.sprites():
            if 675>=note.rect.top>=600 and left_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_down_end.sprites():
            if 675>=note.rect.top>=600 and down_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_down_mid.sprites():
            if 675>=note.rect.top>=600 and down_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_up_end.sprites():
            if 675>=note.rect.top>=600 and up_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_up_mid.sprites():
            if 675>=note.rect.top>=600 and up_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_right_end.sprites():
            if 675>=note.rect.top>=600 and right_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                self.judge='perfect'
        for note in self.hold_note_right_mid.sprites():
            if 675>=note.rect.top>=600 and right_press:
                note.kill()
                self.score+=((100000/self.num_of_notes))
                self.combo+=1
                



        for note in self.note_left.sprites():
            if note.rect.top>=HEIGHT+10:
                self.combo=0
                self.judge='miss'
                note.kill()
                
        for note in self.note_down.sprites():
            if note.rect.top>=HEIGHT+10:
                self.combo=0
                self.judge='miss'
                note.kill()
                
        for note in self.note_up.sprites():
            if note.rect.top>=HEIGHT+10:
                self.combo=0
                self.judge='miss'
                note.kill()
                
        for note in self.note_right.sprites():
            if note.rect.top>=HEIGHT+10:
                self.combo=0
                self.judge='miss'
                note.kill()
                
            



        #note zones
            #left
        self.note_zone_left.update(left_press)
        self.note_zone_left.draw(self.screen)
            #down
        self.note_zone_down.update(down_press)
        self.note_zone_down.draw(self.screen)
            #up
        self.note_zone_up.update(up_press)
        self.note_zone_up.draw(self.screen)
            #right
        self.note_zone_right.update(right_press)
        self.note_zone_right.draw(self.screen)

        #left note
        self.hold_note_left_end.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_left_end.draw(self.screen)
        self.hold_note_left_mid.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_left_mid.draw(self.screen)
        self.note_left.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.note_left.draw(self.screen)
        
        #down note
        self.hold_note_down_end.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_left_end.draw(self.screen)
        self.hold_note_down_end.draw(self.screen)
        self.hold_note_down_mid.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_left_end.draw(self.screen)
        self.hold_note_down_mid.draw(self.screen)
        self.note_down.update(self.current_y+self.chart_speed if game_event=='running' else self.current_y)
        self.note_down.draw(self.screen)
        
        #up note
        self.hold_note_up_end.update(self.current_y+self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_left_end.draw(self.screen)
        self.hold_note_up_end.draw(self.screen)
        self.hold_note_up_mid.update(self.current_y+self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_up_mid.draw(self.screen)
        self.note_up.update(self.current_y+self.chart_speed if game_event=='running' else self.current_y)
        self.note_up.draw(self.screen)
        
        #right note
        self.hold_note_right_end.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_right_end.draw(self.screen)
        self.hold_note_right_mid.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.hold_note_right_mid.draw(self.screen)
        self.note_right.update(self.current_y +self.chart_speed if game_event=='running' else self.current_y)
        self.note_right.draw(self.screen)
        #judgement
        self.judgement.update(self.judge)
        self.judgement.draw(self.screen)


        text=self.font.render(str(0000000+int(self.score//1)), 1, (225, 225, 225))
        self.screen.blit(text, (500, 10))
        text_combo=self.score_font.render(str(f'{self.combo}x'), 1, (225, 225, 225))
        self.screen.blit(text_combo, (500, 600))
    