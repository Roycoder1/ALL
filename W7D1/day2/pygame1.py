

    # Exemple jeu method:


import os
import pygame
import starships
pygame.font.init() # load the font handler of pygame
pygame.mixer.init() # load sound effect handler of pygame

# ----- GEN VAR -----
WHITE = (255, 255, 255)
BLUE =  (40, 2, 90)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 1400
HEIGHT = 700
FPS = 60 

HEALTH_FONT = pygame.font.SysFont('comicsans', 40) 
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

LAZER_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
LAZER_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# pygame.display allow us to display the game window needs a height and width good practise to define those separetly.
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
# pygame rect allow us to create a rectangle that we will use to move images around or create blocks it needs the position of the image/block (x,y) as well as its height and witdh 
BORDER = pygame.Rect(WIDTH // 2 - 5 , 0, 10, HEIGHT) # double // to avoid float number by rounding the divide ( - 5 to compensate the witdh of 10)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
# ----- GEN VAR -----
pygame.display.set_caption("BattleStar Red Leader vs Yellow Leader") # rename the window (like title in html)


def draw_window(yellow, red) -> None:
    """
    function that handle all the drawing inside the window will be called at each iteration of the game loop
    """
    # WIN.fill(WHITE) # color the background of the window always first
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLUE, BORDER) # to draw rectangle that will be used as obstacle or projectile ?
   
    # render allow us to render the font previously declare and use it in a message it take a str a AA num (use 1 always) and a color
    yellow_health_text = HEALTH_FONT.render(f"Health: {str(starships.Yellow_Leader.HEALTH)}", 1, WHITE)
    red_health_text = HEALTH_FONT.render(f"Health: {str(starships.Red_Leader.HEALTH)}", 1, WHITE)

    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(red_health_text, (WIDTH - yellow_health_text.get_width() - 10, 10))
    
    # yellow and red are rectangle therefore we can acces there x and y directly
    WIN.blit(starships.Yellow_Leader.yellow_starship, (yellow.x, yellow.y)) # blit allow us to draw a new surface on the WIN (characters ,wall ect ect )
    WIN.blit(starships.Red_Leader.red_starship, (red.x, red.y))


    for lazer in starships.Yellow_Leader.YELLOW_AMUNITION:
        pygame.draw.rect(WIN, YELLOW, lazer)

    for lazer in starships.Red_Leader.RED_AMUNITION:
        pygame.draw.rect(WIN, RED, lazer)

    pygame.display.update() # update any change made to the WIN


def draw_winner(text:str) -> None:
    """
    funct that print the winner of the game to the screen
    """
    draw_text = WINNER_FONT.render(text, 1, WHITE) 
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() //2, HEIGHT // 2- draw_text.get_height() // 2 ))
    pygame.display.update()
    pygame.time.delay(5000) # allow us to delay the execution of the code


def main() -> None:
    """
    main function that will hold an "infinite" loop so the window will be kept open until we say differently
    will also handle all of the game events
    """
    clock = pygame.time.Clock() #clock object
   
    run = True #doesnt accept True / Break loop so we have to set a run var... best practice annyway  
    while run:
        clock.tick(FPS) #using clock object and fps var we make sure that the game run only to 60 frame per second making it more consistant on every machine
     # pygame.event is a list of event that we can loop threw and specified what to do in each event .. first thing to do inside the game loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #event.type allow us to check and compare event (pygame.quit is the event here so if we press the x window ...)
                run = False

            if event.type == pygame.KEYDOWN: #different then get pressed this one allow to check one particular key at a time only
                if event.key == pygame.K_SPACE and len(starships.Yellow_Leader.YELLOW_AMUNITION) < starships.Starship.MAX_AMUNITION: # space bar (yellow) + checking if already shoot max amu
                    starships.Yellow_Leader.charge_ammo()
                    LAZER_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(starships.Red_Leader.RED_AMUNITION) < starships.Starship.MAX_AMUNITION:# right control (red)
                    starships.Red_Leader.charge_ammo()
                    LAZER_FIRE_SOUND.play()

            if event.type == starships.Yellow_Leader.RED_HIT:
                starships.Red_Leader.HEALTH -= 1
                LAZER_HIT_SOUND.play()

            if event.type == starships.Red_Leader.YELLOW_HIT:
                starships.Yellow_Leader.HEALTH -= 1
                LAZER_HIT_SOUND.play()
                

        winner_text = ""
        if starships.Yellow_Leader.HEALTH <= 0:
            winner_text = "Red Wins !! "

        if starships.Red_Leader.HEALTH <= 0:
            winner_text = "Yellow Wins !! "

        if winner_text != "":
           draw_winner(winner_text)
           break

        keys_pressed = pygame.key.get_pressed() # store inside the keys_pressed var a list of the keys that is currently being preesed
        starships.Yellow_Leader.handle_moves(keys_pressed, BORDER, HEIGHT)
        starships.Red_Leader.handle_moves(keys_pressed, BORDER, HEIGHT, WIDTH)

        starships.Yellow_Leader.handle_fire(starships.Red_Leader.red_move, WIDTH)
        starships.Red_Leader.handle_fire(starships.Yellow_Leader.yellow_move)

        draw_window(starships.Yellow_Leader.yellow_move, starships.Red_Leader.red_move)

    pygame.quit() # terminate the game 

if __name__ == "__main__": # making sure we can play only threw this file and not if imported as a module 
    main() 
13 h 25
import pygame
import os

class Starship():
    """
    common action of all starship
    """
    WIDTH = 100
    HEIGHT = 60
    VELOCITY = 5
    MAX_AMUNITION = 3
    LAZER_VELOCITY = 10
    HEALTH = 10


class Yellow_Leader(Starship):
    """
    handle the personal action of the yellow ship (left)
    """
    pos_x = 200
    pos_y = 300
    # using pygame load image allow us to stock an image inside a variable . os is here to acces the path easilly allow us to be consistant to every computer. 
    image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
    # using pygame transform we can modify an image scale(width heigth)for the size rotate self explanatory ...
    yellow_starship = pygame.transform.rotate(pygame.transform.scale(image, (Starship.WIDTH, Starship.HEIGHT)), 90)
    yellow_move = pygame.Rect((pos_x, pos_y, Starship.WIDTH, Starship.HEIGHT))
    RED_HIT = pygame.USEREVENT + 2 # creating our own event for the game loops(pygame.event.get() the + 1 is only the id of the event
    YELLOW_AMUNITION = []


    @classmethod  
    def handle_moves(cls:object, keys_pressed:list, border:object, win_height:int) -> None:
        """
        method that handle the keys check for the yellow player 
        """
        # pygame.k_ check the key after the _ in this instance a ...
        if keys_pressed[pygame.K_a] and cls.yellow_move.x - cls.VELOCITY > 0: # left (the and here check collision simple logic ...)
            cls.yellow_move.x -= cls.VELOCITY
        if keys_pressed[pygame.K_d] and cls.yellow_move.x + cls.VELOCITY + cls.WIDTH < border.x: # right
            cls.yellow_move.x += cls.VELOCITY
        if keys_pressed[pygame.K_w] and cls.yellow_move.y - cls.VELOCITY > 0: # up
            cls.yellow_move.y -= cls.VELOCITY
        if keys_pressed[pygame.K_s] and cls.yellow_move.y + cls.VELOCITY + cls.HEIGHT < win_height - 50: # down ( - 50 is a hard fix ... bad assets !!!)
            cls.yellow_move.y += cls.VELOCITY
    

    @classmethod
    def charge_ammo(cls:object) -> None:
        """
        function that creat an amunition  by creating a rect and return it (append the amunition list)
        """
        # Pay attention when creating this rectangle to compensate the width and the height of the image according where you want the lazer to go out from. 
        lazer = pygame.Rect(cls.yellow_move.x + cls.yellow_move.width, cls.yellow_move.y + cls.yellow_move.height // 2 + 15 , 12, 6)
        cls.YELLOW_AMUNITION.append(lazer)

        
 
    @classmethod
    def handle_fire(cls:object, red:object, win_width:int) -> None:
        """
        function that fire the loaded amunition by sending t to the right direction the loaded check colision with red
        """
        for lazer in cls.YELLOW_AMUNITION:
            lazer.x += cls.LAZER_VELOCITY
            if red.colliderect(lazer):
                pygame.event.post(pygame.event.Event(cls.RED_HIT)) # pygame.event.post will conect with the main loop to inform that the event append
                cls.YELLOW_AMUNITION.remove(lazer)
            elif lazer.x > win_width:
                cls.YELLOW_AMUNITION.remove(lazer)


class Red_Leader(Starship):
    """
    handle the personal action of the red ship (right)
    """
    pos_x = 1100
    pos_y = 300
    image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
    red_starship = pygame.transform.rotate(pygame.transform.scale(image, (Starship.WIDTH, Starship.HEIGHT)), 270)
    red_move = pygame.Rect((pos_x, pos_y, Starship.WIDTH, Starship.HEIGHT))
    YELLOW_HIT = pygame.USEREVENT + 1 
    RED_AMUNITION = []


    @classmethod
    def handle_moves(cls:object, keys_pressed:list, border:object, win_height:int, win_width:int) -> None:
        """
        method that handle the keys check for the red player 
        """
        if keys_pressed[pygame.K_LEFT] and cls.red_move.x - cls.VELOCITY > border.x + border.width + 35:
            cls.red_move.x -= cls.VELOCITY
        if keys_pressed[pygame.K_RIGHT] and cls.red_move.x + cls.VELOCITY + cls.WIDTH < win_width + 35 : 
            cls.red_move.x += cls.VELOCITY
        if keys_pressed[pygame.K_UP] and cls.red_move.y - cls.VELOCITY > 0: 
            cls.red_move.y -= cls.VELOCITY
        if keys_pressed[pygame.K_DOWN] and cls.red_move.y + cls.VELOCITY + cls.HEIGHT < win_height - 50: 
            cls.red_move.y += cls.VELOCITY


    @classmethod
    def charge_ammo(cls:object) -> None:
        """
        function that emulate a shoot by creating a rect and return it (append the amunition list)
        """
        lazer = pygame.Rect(cls.red_move.x, cls.red_move.y + cls.red_move.height // 2 + 15, 12, 6)
        cls.RED_AMUNITION.append(lazer)
    
      

    @classmethod
    def handle_fire(cls:object, yellow:object) -> None:
        """
        function that fire the loaded amunition by sending t to the right direction the loaded check colision with red
        """
        for lazer in cls.RED_AMUNITION:
            lazer.x -= cls.LAZER_VELOCITY
            if yellow.colliderect(lazer):
                pygame.event.post(pygame.event.Event(cls.YELLOW_HIT))
                cls.RED_AMUNITION.remove(lazer)
            elif lazer.x < 0 :
                cls.RED_AMUNITION.remove(lazer)