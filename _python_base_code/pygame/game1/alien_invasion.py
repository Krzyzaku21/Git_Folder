import sys
import pygame as pg

class AlienInvasion:

    def __init__(self):
        pg.init()
        # window size
        screen_dim = (600, 600)
        self.screen = pg.display.set_mode(screen_dim)
        pg.display.set_caption("Alien Invasion")
        # background color
        self.bg_color = (225, 225, 225) #kolor tła

        # screen rect object
        self.screen_rect = self.screen.get_rect()
        screen_center = self.screen.get_rect.center #center of screen
        # x and y values
        screen_rect.left, screen_rect.right, screen_rect.top, screen_rect.bottom, screen_rect.centerx, screen_rect.centery, screen_rect.width, screen_rect.height
        #tuples
        screen_rect.center
        screen_rect.size
        # screen object create
        bullet_rect = pg.Rect(100, 100, 3, 15)
        color = (100, 100, 100)
        p.draw.rect(screen, color, bullet_rect)
        # Images
        ship = pg.image.load('images/ship/bmp')
        ship_rect = ship.get_rect()
        ship_rect.midbottom = screen_rect.midbottom
        # Draw image on screen
        screen.blit(ship, ship_rect)
    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type  == pg.QUIT:
                    sys.exit
            self.screen.fill(self.bg_color)
            pg.display.flip()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()