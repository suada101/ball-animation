# Example file showing a basic pygame "game loop"
import sys, pygame

# pygame setup
pygame.init()
# erster Wert breite, zweite höhe
#screen = pygame.display.set_mode((1280, 700))
width = 1000
height = 700
screen = pygame.display.set_mode((width, height))
speed = [ 7, 7]
white = 255,255,255


ball = pygame.image.load("dinsball.png")
ball = pygame.transform.smoothscale(ball,(150,150))
ballrect = ball.get_rect()


font = pygame.font.Font(None, 100)
text = font.render("BALL ANIMATION!", True, white)
text_rect = text.get_rect(center=(width/2, height/2))

font = pygame.font.Font(None, 50)
unterschrift = font.render("            M A D E  B Y  S U A D A  ;) ", True, white)
u_rect = text.get_rect(center=(width/2, height/2+65))

# uhr?
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("red")

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    
    screen.fill("orange")

    # Mit screen.blit fügt man die sachen hinzu!! Und die Reihenfolge 
    # besteht auch die ebene
    screen.blit(text, text_rect) # ebene 1
    screen.blit(unterschrift, u_rect) # ebene 2
    screen.blit(ball, ballrect) # ebene 3
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()