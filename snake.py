Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pygame
... import time
... 
... pygame.init()
... 
... # Define colors
... white = (255, 255, 255)
... black = (0, 0, 0)
... red = (255, 0, 0)
... 
... # Set display width and height
... display_width = 800
... display_height = 600
... 
... # Create the game display
... game_display = pygame.display.set_mode((display_width, display_height))
... pygame.display.set_caption('Snake Game')
... 
... clock = pygame.time.Clock()
... snake_block = 10
... snake_speed = 30
... 
... font_style = pygame.font.SysFont(None, 50)
... score_font = pygame.font.SysFont(None, 35)
... 
... 
... def our_snake(snake_block, snake_list):
...     for x in snake_list:
...         pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])
... 
... 
... def message(msg, color):
...     mesg = font_style.render(msg, True, color)
...     game_display.blit(mesg, [display_width / 6, display_height / 3])
... 
... 
... def game_loop():
...     game_over = False
...     game_close = False
... 
...     x1 = display_width / 2
...     y1 = display_height / 2
... 
...     x1_change = 0
...     y1_change = 0
... 
...     snake_List = []
...     Length_of_snake = 1
... 
...     foodx = round((display_width / 2) / 10.0) * 10.0
...     foody = round((display_height / 2) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
