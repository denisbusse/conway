#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:31:37 2021
Provides the ConwayBase class and an implementation of said class.

@author: dkappe
"""

from abc import ABC, abstractclassmethod


import numpy as np


class ConwayBase(ABC):
    """
    ConwayBase is an abstract base class with all of the Game's logic missing.
    Any class based on it has to implement the methods:
     * update_field()
     * show_field()

    Parameters
    ----------
    start_field : numpy.ndarray
        Simulation field at the start of the Game.
    
    Properties
    ----------
    start_field: numpy.ndarray
        Simulation field at the start of the Game.
    current_field: numpy.ndarray
        Current state of the Simulation field.
    size: int
        Size of the start_field numpy.ndarray
    shape: (int, int)
        Shape of the start_field numpy.ndarray
    is_empty: bool
        Checks whether there are any points left on the simulation field.
    """
    def __init__(self, start_field: np.ndarray):
        self.start_field = start_field
        self.reset_field()
        self.size = self.current_field.size
        self.shape = self.current_field.shape
        
    @abstractclassmethod
    def update_field(self):
        """
        Class method providing the Game logic. Here the current_field has to be
        updated for the next frame.
        """
        pass
    
    @abstractclassmethod
    def show_field(self) -> np.ndarray:
        """
        Class method returning the image to be displayed. The Image can either
        be a 2D numpy array with shape (width, height) or a 3D numpy array with
        shape (width, height, color), where color are RGB values

        Returns
        -------
        numpy.ndarray
            The image to be drawn.

        """
        pass
    
    def reset_field(self):
        """
        Resets the simulation field to the starting configuration.
        """
        self.current_field = np.array(self.start_field, copy=True)
    
    @property
    def is_empty(self) -> bool:
        """
        Checks and returns, if current_field has no non-zero values.
        """
        return np.sum(self.current_field) == 0


class Conway(ConwayBase):
    def __init__(self, start_field, border:bool = True,
                 fade: tuple = (1, 1, 1), gauss_sigma: tuple = (0, 0, 0)):
        super().__init__(start_field)
        pass
    
    def update_field(self):
        shape = self.current_field.shape
        new_field = np.array(self.current_field)
        for col in range(shape[0]):
            for row in range(shape[1]):
                # calculate living neighbors
                living_neighbors = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (not (i == 0 and j == 0)) and 0 <= col+i < shape[0] and 0 <= row+j < shape[1]:
                            # ignore the field itself and don't try to read out of bounds.
                            living_neighbors += self.current_field[col+i, row+j]
                # calculate
                if self.current_field[col, row]:
                    # living
                    if living_neighbors < 2 or living_neighbors > 3:
                        new_field[col, row] = 0
                else:
                    # dead
                    if living_neighbors == 3:
                        new_field[col, row] = 1
        self.current_field = new_field

    def show_field(self) -> np.ndarray:
        return np.array([p * 0xFF0000 for p in self.current_field])