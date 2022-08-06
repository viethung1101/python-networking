#!/usr/bin/env python3
import sys
import pygame
from network import Network


#Set up screen for client player
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    """Redraw windown each update"""

    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    """main loop"""
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0,255,0))
    p2 = Player(0, 0, 100, 100, (255,255,0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x,p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p.move()
        redrawWindow(win, p, p2)
    pygame.quit()

if __name__ == '__main__':
    main()
