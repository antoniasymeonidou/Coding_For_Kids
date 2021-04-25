import pygame, sys, time, random

difficulty = 25

w = 700
h = 500

pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((w, h))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Game variables
position = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (w/2, h/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (w/10, 15)
    else:
        score_rect.midtop = (w/2, h/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
        position[1] -= 10
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
        position[1] += 10
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
        position[0] -= 10
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        position[0] += 10

    snake_body.insert(0, list(position)) 
    if position[0] == food_pos[0] and position[1] == food_pos[1]:
        score = score + 1
        food_spawn = False
    else:
        snake_body.pop() #adding one tail to the snake

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10)) #coordinates

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Getting out of bounds
    if position[0] < 0 or position[0] > w-10:
        game_over()
    if position[1] < 0 or position[1] > h-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if position[0] == block[0] and position[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps.tick(difficulty)
