import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    txt = font.render("hello", True, (255, 255, 255))
    screen.blit(txt, [300, 200])
    #img = pg.image.load("fig/3.png")
    screen.blit(img, [300, 200])
    pg.display.update()
    img_rct = img.get_rect()
    img_rct.center = 300, 200
    screen.blit(img, img_rct)

    enn = pg.Surface((200, 200))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [370, 200])
        screen.blit(enn, [400, 400])
        pg.display.update()
        tmr += 1      
        clock.tick(10)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()