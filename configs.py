#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:25:58 2021
Provides a few Objects to play with and a function simplifing placing an object
onto a simulation field.

@author: dkappe
"""
import numpy as np


def insert_pattern(base, pattern, offset=None):
    """
    Takes a base simulation field and places a given pattern with an offset
    onto it. When offset is None, the object is placed into the middle

    Parameters
    ----------
    base : numpy.ndarray
        The base simulation field. Can already hold objects.
    pattern : numpy.ndarray
        The pattern to be placed. Should fit onto the simulation field
    offset : (offset_x, offset_y), optional
        offset in the x and y directions, from the middle. The default is None.

    Raises
    ------
    ValueError
        Error is raised, if the pattern does not fit onto the simulation field.

    Returns
    -------
    field : TYPE
        The simulation field with the pattern placed.
    """
    if type(pattern) != np.ndarray:
        pattern = np.array(pattern)

    print("calculate offset")
    offset_x = int(base.shape[0] / 2 - (pattern.shape[0] / 2))
    offset_y = int(base.shape[1] / 2 - (pattern.shape[1] / 2))
    if offset is not None:
        (offset_add_x, offset_add_y) = offset
        offset_x += offset_add_x
        offset_add_y += offset_add_y
    for ind_x in range(pattern.shape[0]):
        for ind_y in range(pattern.shape[1]):
            base[offset_x + ind_x][offset_y + ind_y] = pattern[ind_x][ind_y]

    return base


BLINKER = [[1, 1, 1]]

BEACON = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

PULSER = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

GOSPER = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]