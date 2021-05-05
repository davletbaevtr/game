import pygame
import time
import dollar

dollar_now = dollar.curr_price()

pygame.init()
pygame.display.set_caption('Clicker game')

background_img = pygame.image.load('sprites/background.png')

putin_img = pygame.image.load('sprites/putin_img.png')
polic_img = pygame.image.load('sprites/police.png')
rosgv_img = pygame.image.load('sprites/rosgv.png')
prist_img = pygame.image.load('sprites/prist.png')
dvorec_img = pygame.image.load('sprites/dvorec.png')
novichek_img = pygame.image.load('sprites/nov.png')
menu_img = pygame.image.load('sprites/menu.png')
end_img = pygame.image.load('sprites/end.png')
win_img = pygame.image.load('sprites/win.png')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_BLUE = (51, 90, 114)

class MainPutin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 70
        self.height = 71

        self.animation_state = 0

    def draw(self):
        if self.animation_state > 0:
            putin_img_scaled = pygame.transform.scale(putin_img, ( int(0.9*self.length),int(0.9*self.height) ))
            window.blit(putin_img_scaled, (putin_img_scaled.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2) ) )))
            self.animation_state -= 1
        else:
            window.blit(putin_img, putin_img.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2) ) ))

    def is_collidepoint(self, mouse_pos):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(mouse_pos)

class ScoreBoard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 100
        self.length = 100

    def draw(self):
        font = pygame.font.SysFont('arial', 24)
        small_font = pygame.font.SysFont('arial', 24)

        SCORE = font.render('{} rubles'.format( int(user.score) ), True, BLACK)
        dollar_now_ = font.render('dollar now:{}r'.format( dollar_now ), True, BLACK)
        time_for_req_ = font.render('time for update:{}min'.format( int((300 - time_for_req) / 60) ), True, BLACK)
        rps = font.render('per second: {:.1f}'.format(user.rps), True, BLACK)

        window.blit(SCORE, (SCORE.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2) ) )))
        window.blit(dollar_now_, dollar_now_.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2 - 20) ) ))
        window.blit(time_for_req_, time_for_req_.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2 - 40) ) ))
        window.blit(rps, (rps.get_rect( center=( int(self.x + self.length/2),int(self.y + self.height/2 + 20) ) )))

class improvement:
    def __init__(self, name, x, y, image, base_cost, increase_per_purchase, rps):
        self.name = name
        self.x = x
        self.y = y
        self.height = 45
        self.length = 150

        self.image = image
        self.base_cost = base_cost
        self.increase_per_purchase = increase_per_purchase
        self.rps = rps

        self.quantity = 0

    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(mouse_pos)

    def getTotalCost(self):
        return int(self.base_cost * self.increase_per_purchase**(self.quantity))

    def draw(self, solid = True):
        store_cost_font = pygame.font.SysFont('arial', 16)
        store_quantity_font = pygame.font.SysFont('arial', 36)
        store_improvement_font = pygame.font.SysFont('arial', 24)
        store_now_rps = pygame.font.SysFont('arial', 16)

        image = self.image

        if self.name == "Дворец":
            cost = store_cost_font.render('{}$'.format( format_number( int( 160 * self.increase_per_purchase**(self.quantity) ) ) ), True, BLACK)
        else:
            cost = store_cost_font.render('{}'.format( format_number(self.getTotalCost()) ), True, BLACK)
        quantity = store_quantity_font.render('{}'.format(self.quantity), True, BLACK)
        improvement_title = store_improvement_font.render('{}'.format(self.name), True, BLACK)
        rps = store_now_rps.render('{} rps'.format(self.rps), True, BLACK)
        now_rps = store_now_rps.render('produced {:.1f} rps'.format((self.rps * self.quantity)), True, BLACK)

        if solid == False:
            image.set_alpha(100)
        else:
            image.set_alpha(256)
        window.blit(image, (self.x, self.y))
        window.blit(cost, (self.x + self.length + 5, self.y + 25))
        window.blit(quantity, (980, self.y))
        window.blit(improvement_title, (self.x + self.length + 5, self.y))
        window.blit(rps, (950, self.y + self.height - 3))
        window.blit(now_rps, (self.x + 5, self.y + self.height))

class win_buttons:
    def __init__(self, x, y, image, cost):
        self.x = x
        self.y = y
        self.height = 168
        self.length = 300
        self.image = image
        self.cost = cost

    def collidepoint(self, mouse_pos):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(mouse_pos)

    def getCost(self):
        return self.cost

    def draw(self, solid = True):
        win_font = pygame.font.SysFont('arial', 24)
        name = win_font.render('{}'.format("Овальный"), True, BLACK)
        cost = win_font.render('{}'.format(self.cost), True, BLACK)
        image = self.image

        if solid == False:
            image.set_alpha(100)
        else:
            image.set_alpha(256)

        window.blit(name, (self.x + 5, self.y + self.height + 5))
        window.blit(cost, (self.x + self.length - 100, self.y + self.height + 5))
        window.blit(image, (self.x, self.y))

class Player:
    def __init__(self):
        self.score = 0
        self.rps = 0

    def updateTotalrps(self, list_of_improvement):
        self.rps = 0
        for improvement in list_of_improvement:
            self.rps += improvement.rps * improvement.quantity

window_length = 1000
window_height = 800
window = pygame.display.set_mode((window_length, window_height))
putin = MainPutin(500, 140)
score_board = ScoreBoard(100, 0)
user = Player()
win_button = win_buttons(50, 100, prist_img, 1000000)

store_y = 75
polic = improvement('Полиция', 700, 10, polic_img, base_cost = 15, increase_per_purchase = 1.15, rps = 0.1)
rosgv = improvement('Гвардия', 700, 10 + store_y, rosgv_img, base_cost = 100, increase_per_purchase = 1.15, rps = 1)
novichek = improvement('Новичок', 700, 10 + store_y * 2, novichek_img, base_cost = 1100, increase_per_purchase = 1.15, rps = 8)
dvorec = improvement('Дворец', 700, 10 + store_y * 3, dvorec_img, base_cost = dollar_now * 160, increase_per_purchase = 1.15, rps = 47)

list_of_improvement = [polic, rosgv, novichek, dvorec]
list_of_fbuttons = [pygame.K_DELETE, pygame.K_PRINTSCREEN, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, 
                    pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, 
                    pygame.K_F12, pygame.K_HOME, pygame.K_HELP, pygame.K_END, pygame.K_PAGEDOWN, pygame.K_PAGEUP, 
                    pygame.K_NUMLOCK, pygame.K_CAPSLOCK, pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_LCTRL, 
                    pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT, pygame.K_TAB]

def format_number(n):
    if n >= 1000000000:
        if (n / 1000000000 )% 1 == 0:
            n = '{:.0f} billion'.format(n / 1000000000)
        else:
            n = '{:.2f} billion'.format(n / 1000000000)
    elif n >= 1000000:
        if (n / 1000000) % 1 == 0:
            n = '{:.0f} million'.format(n / 1000000) 
        else:
            n = '{:.2f} million'.format(n / 1000000)
    return n

time_for_req = 0 

def draw():
    global tmp_time
    global time_for_req
    window.blit(background_img, (0, 0))

    putin.draw()
    score_board.draw()

    if user.score >= win_button.getCost():
        win_button.draw(solid = True)
    else:
        win_button.draw(solid = False)    

    now_all_rps = 0
    for improvement in list_of_improvement:
        if user.score >= improvement.getTotalCost():
            improvement.draw(solid = True)
        else:
            improvement.draw(solid = False)

        now_all_rps += improvement.rps * improvement.quantity

    now_time = pygame.time.get_ticks()
    if now_time - tmp_time >= 1000:
            user.score += now_all_rps
            tmp_time = now_time
            time_for_req += 1
            if time_for_req >= 300:
                dollar_now = curr_price()
                time_for_req = 0
    pygame.display.update()

def menu_draw():
    window.blit(menu_img, (0, 0))

    menu_font = pygame.font.SysFont('arial', 48)
    charac_font = pygame.font.SysFont('arial', 24)
    charac1 = charac_font.render('{}'.format('All characters appearing in this work are fictious.'), True, BLACK)
    charac2 = charac_font.render('{}'.format('Any resemblance to real persons, living or dead, is purely coincidental.'), True, BLACK)
    menu = menu_font.render('{}'.format('Press any button to start!'), True, BLACK)

    window.blit(charac1, (250, 560))
    window.blit(charac2, (120, 585))
    window.blit(menu, (240, 335))

    pygame.display.update()

def end(is_win):
    end_font = pygame.font.SysFont('arial', 48)
    is_end = end_font.render('{}'.format('Thanks for playing'), True, GREEN)
    contact = end_font.render('{}'.format('@noname_td'), True, GREEN)

    if is_win:
        window.blit(win_img, (0, 0))
        pygame.display.update()
        pygame.time.delay(1000)

    window.blit(end_img, (0, 0))
    window.blit(is_end, (100, 280))
    window.blit(contact, (100, 330))
    pygame.display.update()

    pygame.time.delay(1000)

tmp_time = pygame.time.get_ticks()

win = False
def run():
    menu = True
    game = True
    global win

    menu_draw()
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key not in list_of_fbuttons:
                    menu = False
                    if event.key == pygame.K_ESCAPE:
                        game = False

            if event.type == pygame.QUIT:
                menu = False
                game = False

    while game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for improvement in list_of_improvement:
                    if improvement.collidepoint(mouse_pos) and user.score >= improvement.getTotalCost():
                        user.score -= improvement.getTotalCost()
                        improvement.quantity += 1
                        user.updateTotalrps(list_of_improvement)

                if win_button.collidepoint(mouse_pos) and user.score >= win_button.getCost():
                    game = False
                    win = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
                elif event.key == pygame.K_SPACE:
                    user.score += 1
                    putin.animation_state = 1

            if event.type == pygame.QUIT:
                game = False

        draw()

if __name__ == '__main__':
    run()
    end(win)
else:
    pygame.display.set_caption('WAIT, TESTING')
