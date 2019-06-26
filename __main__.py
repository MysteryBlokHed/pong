# Created by MysteryBlokHed in 2019.
import pygame
import pygame.freetype
import player, ball

pygame.init()

width = 960
# Formula for 16:9
height = int(width/2+width/16)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong by MysteryBlokHed")

player1 = player.Player(25, 200, 25, 150)
player2 = player.Player(width-75, 200, 25, 150)
ball1 = ball.Ball(480, 270, 15, 15)
ball1.set_vel_x(10)
ball1.set_vel_y(-10)

player1_score = 0
player2_score = 0

scored = False
ai = True

text = pygame.freetype.SysFont("Roboto", 30)

running = True
while running:
    pygame.time.delay(50)

    # Handle each event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    # Get keystrokes
    keys = pygame.key.get_pressed()

    # Toggle AI
    if keys[pygame.K_f]:
        ai = not ai
    # Player 1 movement
    if keys[pygame.K_w] and player1.get_y() > 10:
        player1.set_vel_y(-7)
    elif keys[pygame.K_s] and player1.get_y() < height - 10 - player1.get_height():
        player1.set_vel_y(7)
    else:
        player1.set_vel_y(0)
    # Player 2 movement
    if not ai:
        if keys[pygame.K_UP] and player2.get_y() > 10:
            player2.set_vel_y(-7)
        elif keys[pygame.K_DOWN] and player2.get_y() < height - 10 - player2.get_height():
            player2.set_vel_y(7)
        else:
            player2.set_vel_y(0)
    else:
        # Player 2 AI
        if ball1.get_vel_x() > 0:
            if ball1.get_vel_y() > 0 and ball1.get_x() > width/3 and ball1.get_y() > height/8 and player2.get_y() <= height - 10 - player2.get_height():
                print("[AI] Going down")
                player2.set_vel_y(7)
            elif ball1.get_vel_y() < 0 and ball1.get_x() > width/4 and ball1.get_y() < height-height/8 and player2.get_y() >= 10:
                print("[AI] Going up")
                player2.set_vel_y(-7)
            else:
                print("Velocity Frozen!")
                player2.set_vel_y(0)
        # Fix AI breaking the damn boundaries
        if player2.get_y() < 10:
            player2.set_y(10)
            player2.set_vel_y(0)
            print("/!\\ AI tried to break upper boundaries")
        if player2.get_y() > height - 10 - player2.get_height():
            player2.set_y(height - 10 - player2.get_height())
            player2.set_vel_y(0)
            print("/!\\ AI tried to break lower boundaries")
    
    # Background colour
    screen.fill((0, 0, 0))
    # Ball collision detection with players
    if ball1.check_collision_rect_autohitbox(player1.get_x(), player1.get_y(), player1.get_width(), player1.get_height(), 1) or ball1.check_collision_rect_autohitbox(player2.get_x(), player2.get_y(), player2.get_width(), player2.get_height(), 1):
        ball1.set_vel_x(ball1.get_vel_x()*-1)
        # ball1.set_vel_y(ball1.get_vel_y()*-1)
    # Ball collision detection with top and bottom border
    if ball1.check_collision_rect_autohitbox(0, -15, width, ball1.get_height(), 1) or ball1.check_collision_rect_autohitbox(0, height, width, ball1.get_height(), 1):
        ball1.set_vel_y(ball1.get_vel_y()*-1)
    # Ball goes past Player 1
    if ball1.check_collision_rect_autohitbox(0, 0, ball1.get_width(), height, 1):
        player2_score += 1
        scored = True
    # Ball goes past Player 2
    if ball1.check_collision_rect_autohitbox(width, 0, ball1.get_width(), height, 1):
        player1_score += 1
        scored = True
    # Reset positions if anyone scored
    if scored:
        # Reset positions
        ball1.set_x(480)
        ball1.set_y(270)
        player1.set_x(25)
        player1.set_y(200)
        player2.set_x(width-75)
        player2.set_y(200)
        scored = False

    # Tick
    player1.tick()
    player2.tick()
    ball1.tick()
    ## Render objects
    # Game Objects
    player1.render(screen)
    player2.render(screen)
    ball1.render(screen)
    # Text
    text.render_to(screen, (width/2-30, 50), "{} - {}".format(player1_score, player2_score), (255, 255, 255))
    text.render_to(screen, (width/4, height-50), "Press F to toggle Player 2 AI", (255, 255, 255))
    # Update the display
    pygame.display.flip()

# Quit the game when user presses 'X'
pygame.quit()