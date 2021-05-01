#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:31:15 2021

@author: dkappe
"""
from time import sleep
import pygame
from pygame import surfarray
from pygame.locals import KEYDOWN, K_BACKSPACE, QUIT, HWSURFACE, DOUBLEBUF


from conway import Conway


def pygame_loop(conway: Conway, screen_size: tuple = (1600, 800), fps: int = 30):
    """
    Function to display the evolution of Conway's Game of Life or any other
    simulation with a 2D output.

    Parameters
    ----------
    conway : Conway
        Any class providing the attributes
         * shape
         * is_empty
        and the methods
         * show_field() -> numpy.ndarray
         * update_field()
         * reset_field()
    screen_size : Tuple(int, int), optional
        Size of the Screen to be displayed. The default is (1600, 800).
    fps : int, optional
        Frames per second goal to achieve. The default is 30.
    """
    pygame.init()
    screen = pygame.display.set_mode(screen_size, HWSURFACE | DOUBLEBUF)
    running = True
    clock = pygame.time.Clock()
    while running:
        pygame.display.update()
        conway.update_field()
        arr = conway.show_field()
        surf = pygame.Surface(conway.shape)
        surfarray.blit_array(surf, arr)
        surf = pygame.transform.scale(surf, screen_size)
        screen.blit(surf, (0, 0))
        clock.tick(fps)
        pygame.display.set_caption(f"Conway's Game of Life | fps: {clock.get_fps():.3}")
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
            elif event.type == QUIT:
                running = False
                pygame.quit()
        if conway.is_empty:
            sleep(0.5)
            conway.reset_field()


if __name__ == '__main__':
    import numpy as np
    from configs import *
    base = np.zeros((100, 100))
    start_config = base
    #start_config = insert_pattern(base, PULSER).T
    start_config = insert_pattern(base, GOSPER).T
    #start_config = insert_pattern(start_config, BLINKER, offset=(7, 5))
    #start_config = insert_pattern(start_config, BLINKER, offset=(-7, 5))
    #start_config = insert_pattern(start_config, BLINKER, offset=(7, -5))
    #start_config = insert_pattern(start_config, BLINKER, offset=(-7, -5))
    screen_size = np.array(start_config.shape) * 10
    conway = Conway(start_config)
    pygame_loop(conway, screen_size=screen_size, fps=30)
