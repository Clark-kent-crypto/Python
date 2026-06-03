import pygame,sys
from pygame.locals import*
from random import *
class game_screen:
    def __init__(self,height,width):
        self.height=height
        self.width=width
class rectangles:
   def __init__(self,height,width):
      self.height=height
      self.width=width
class game_state:
   skip=0
   speed=8
   is_reversed=False
   is_reversed_ball_x=False
   is_reversed_ball_y=False
class circleCenter:# i dont really use it and has no value right now 
   def __init__(self,x,y):
      self.x=x
      self.y=y


New_screen=game_screen(500,800)#current game screen information not to be confused with the screen that takes the surface
new_rect=pygame.Rect(0,0,20,100)#Rect to render the boxes 
player_rect=pygame.Rect(New_screen.width-20,0,20,100)
new_Ball=[50,450]#x and y axis data for the ball object
new_game_state=game_state()#creation of a game_state class
if( pygame.init()==False):
    print("Failed to open pygame!")

screen=pygame.display.set_mode((New_screen.width,New_screen.height))
pygame.display.set_caption("MY APP")

def draw_a_rect(screen,rectangle):
   new_color=pygame.Color(1,2,3,255)
   pygame.draw.rect(screen,new_color,rectangle) 


def reverse_box():#its a function that is reversing the direction of the ai box movement 
   if(new_rect.top>0 and new_game_state.skip%new_game_state.speed==0):
      new_rect.top-=1


def isReverse():# check if the box is in reversable state if yes put the appropriate  value in current game_state as boolian
     if(new_rect.top==New_screen.height-new_rect.height):
      new_game_state.is_reversed=True
     elif(new_rect.top==0):
      new_game_state.is_reversed=False
      

def update():
   ai_animation()
   ball_movement()
   collision()
   speed_Check=new_game_state.skip%3==0
   key_state=pygame.key.get_pressed()
   for keys in key_state:
      if (key_state[pygame.K_s]==True and player_rect.top<New_screen.height-player_rect.height and speed_Check ):
         player_rect.top+=1
         break
      elif(key_state[pygame.K_w]==True and player_rect.top>0 and speed_Check):
         player_rect.top-=1
         break
   
   
      

 

   
def render():
   new_color=pygame.Color(134,156,235,255)
   pygame.Surface.fill(screen,new_color)
  
   draw_a_rect(screen,new_rect)
   draw_a_rect(screen,player_rect)
   draw_a_circle(15)

   update()
   
   
def draw_a_circle(radius:int):
   new_color=pygame.Color(123,234,240,255)
   pygame.draw.circle(screen,new_color,new_Ball,radius,0)
def ball_movement():
   collision()
   top_Check=new_Ball[1]>=0+15
   bottom_Check=new_Ball[1] <= New_screen.height-15
   left_Check=new_Ball[0]>=0+15
   right_Check=new_Ball[0]<New_screen.width-15
   if(top_Check and bottom_Check and left_Check and right_Check and new_game_state.is_reversed_ball_x==False and new_game_state.skip%new_game_state.speed==0):
    new_Ball[0]+=1
   if(top_Check and bottom_Check and left_Check and right_Check and new_game_state.is_reversed_ball_x==True and new_game_state.skip%new_game_state.speed==0):
      new_Ball[0]-=1
   if(top_Check and bottom_Check and left_Check and right_Check and new_game_state.is_reversed_ball_y==False and new_game_state.skip%new_game_state.speed==0):
      new_Ball[1]+=1
   if(top_Check and bottom_Check and left_Check and right_Check and new_game_state.is_reversed_ball_y==True and new_game_state.skip%new_game_state.speed==0):
      new_Ball[1]-=1


def ai_animation():
   isReverse()
 
   if(new_game_state.is_reversed==False):

     if(new_rect.top<New_screen.height-new_rect.height and new_game_state.skip%new_game_state.speed==0):
       new_rect.top+=1

   elif(new_game_state.is_reversed==True):
   
    reverse_box()  

   

def gameloop():
 while(True):
    render()
    input_section()
    
   #  for event in pygame.event.get():
   #    if(event.type==QUIT  ):
   #       pygame.quit()
   #       sys.exit()
   #    if(event.type==KEYDOWN):
   #       if(event.key==K_ESCAPE):
   #          pygame.quit()
   #          sys.exit()
      
      
      # if(event.type==KEYDOWN and event.key==K_s):
      #       player_rect.top+=10
    pygame.display.update()
    new_game_state.skip+=1
def input_section():
   for event in pygame.event.get():
      if(event.type==QUIT  ):
         pygame.quit()
         sys.exit()
      if(event.type==KEYDOWN):
         if(event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
def collision():
   top_collision=new_Ball[1]==0+15
   bottom_collison=new_Ball[1]==New_screen.height-15
   left_collison=new_Ball[0]==0+15
   right_collison=new_Ball[0]==New_screen.width-15
   if(top_collision==True):
      #
      new_game_state.is_reversed_ball_y=False
      new_Ball[1]+=1
   if(bottom_collison==True):
      new_game_state.is_reversed_ball_y=True
      new_Ball[1]-=1

   if(left_collison==True):
      new_game_state.is_reversed_ball_x=False
      new_Ball[0]+=1
   if(right_collison==True):
      new_game_state.is_reversed_ball_x=True
      new_Ball[0]-=1


def reverseBall_X():
   new_Ball[0]-=1
   new_game_state.is_reversed_ball_x=True
def reverseBall_Y():
   new_Ball[1]-=1
   new_game_state.is_reversed_ball_y=True

def main():
 gameloop()



main()
