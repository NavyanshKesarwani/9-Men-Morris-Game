import pygame
import pygame_menu
import NineMenMain


pygame.init()
surface = pygame.display.set_mode((800, 600))

def set_difficulty(difficulty, number):
    # Do the job here 
    pass
def start_the_game():
    # Do the job here !
    NineMenMain.main()

if __name__ == "__main__":
    menu = pygame_menu.Menu('Welcome', 800, 600,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Play', start_the_game)
    menu.add.selector('Difficulty :', [('Easy', 1), ('Normal', 2), ('Hard', 3)], onchange=set_difficulty)
    menu.add.selector('Mode :', [('Player vs Player', 1), ('Player vs AI', 2)])
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
