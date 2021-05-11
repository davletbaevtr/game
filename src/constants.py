import pygame

pygame.init()

window_length = 1000
window_height = 800
store_y = 75

window = pygame.display.set_mode((window_length, window_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_BLUE = (51, 90, 114)

time_for_req = 0

common_path = 'resources/sprites/'
background_img = pygame.image.load(common_path + '/background.png')
putin_img = pygame.image.load(common_path + 'putin_img.png')
polic_img = pygame.image.load(common_path + 'police.png')
rosgv_img = pygame.image.load(common_path + 'rosgv.png')
prist_img = pygame.image.load(common_path + 'prist.png')
dvorec_img = pygame.image.load(common_path + 'dvorec.png')
novichek_img = pygame.image.load(common_path + 'nov.png')
menu_img = pygame.image.load(common_path + 'menu.png')
end_img = pygame.image.load(common_path + 'end.png')
win_img = pygame.image.load(common_path + 'win.png')

list_of_fbuttons = [pygame.K_DELETE, pygame.K_PRINTSCREEN, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, 
                    pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, 
                    pygame.K_F12, pygame.K_HOME, pygame.K_HELP, pygame.K_END, pygame.K_PAGEDOWN, pygame.K_PAGEUP, 
                    pygame.K_NUMLOCK, pygame.K_CAPSLOCK, pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_LCTRL, 
                    pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT, pygame.K_TAB]
