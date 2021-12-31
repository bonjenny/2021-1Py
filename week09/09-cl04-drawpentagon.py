# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:36:21 2021

@author: 엄지희
"""

import turtle as t

t.setup(500, 400)
t.speed(0)

for _ in range(15):
    for _ in range(4):
        for _ in range(5):
            t.fd(100)
            t.lt(72)
        t.lt(90)
    t.lt(6)
