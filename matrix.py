#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matrix.py
#  
# MIT License
#
# Copyright (c) 2017 Jean Vincent
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sense_hat import SenseHat


class Matrix(SenseHat):
    """
    Class containing additional methods for operating the LED matrix
    """

    def __init__(self):
        SenseHat.__init__(self)

    def set_column(self, col, pixel_list):
        """
        Accepts a column number and a list of 8 pixels and sets	the pixels
        in this column to the values in the list (from bottom to top)
        """
        for x in range(8):
            self.set_pixel(x, col, pixel_list[x])
            
            
    def mode_one(self, intensity):
        if intensity > 255:
            intensity = 255
        px = [intensity, intensity // 2, intensity // 2]
        pixels = [px, px, px, px, px, px, px, px]
        return pixels
        
        
    def mode_two(self, intensity):
        if intensity > 255:
            intensity = 255
        pixels = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        n = (8 * intensity / 255)
        for i in range(n):
            pixels[i-n] = [intensity, intensity // 3, intensity // 2]
        return pixels
        
        
    def mode_three(self, intensity):
        if intensity > 255:
            intensity = 255
        pixels = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if intensity > 32:
            pixels[7] = [intensity, intensity // 3, intensity // 2]
        if intensity > 64:
            pixels[6] = [intensity, intensity // 3, intensity // 2]
        if intensity > 96:
            pixels[5] = [intensity, intensity // 3, intensity // 2]
        if intensity > 128:
            pixels[4] = [intensity, intensity // 3, intensity // 2]
        if intensity > 160:
            pixels[3] = [intensity, intensity // 3, intensity // 2]
        if intensity > 192:
            pixels[2] = [intensity, intensity // 3, intensity // 2]
        if intensity > 224:
            pixels[1] = [intensity, intensity // 3, intensity // 2]
        if intensity == 255:
            pixels[0] = [intensity, intensity // 3, intensity // 2]
        return pixels
            
