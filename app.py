import pygame

pygame.init()

def game():
    grass = (124, 252, 0)
    dirt = (160, 82, 45)
    sky = (135, 206, 235)
    player_color = (255, 0, 0)

    width = 600
    height = 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("app.py")

    player_width = 40
    player_height = 40
    ground_y = 400
    
    player_x = width // 2 - player_width // 2
    player_y = ground_y - player_height 

    velocity_x = 5

    is_jump = False
    gravity = 1 
    jump_strength = -15
    vertical_velocity = 0
    
    clock = pygame.time.Clock()
    FPS = 60

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and not is_jump:
                    is_jump = True
                    vertical_velocity = jump_strength

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player_x > 0:
            player_x -= velocity_x
        if keys[pygame.K_d] and player_x < width - player_width:
            player_x += velocity_x

        if is_jump or player_y < ground_y - player_height:
            vertical_velocity += gravity
            player_y += vertical_velocity
            
            if player_y >= ground_y - player_height:
                player_y = ground_y - player_height
                is_jump = False
                vertical_velocity = 0

        window.fill(sky)
        pygame.draw.rect(window, grass, (0, ground_y, width, height - ground_y))
        pygame.draw.rect(window, dirt, (0, 550, width, height - 550))
        pygame.draw.rect(window, player_color, (player_x, player_y, player_width, player_height))
        
        pygame.display.flip()

    pygame.quit()
    
def init(run:bool):
    if run == True:
        game()
    else:
        pass