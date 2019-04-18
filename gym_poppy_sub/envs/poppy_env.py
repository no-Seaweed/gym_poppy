#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:01:10 2019

@author: macbook
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class PoppyEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.__version__ = "0.1.0"
    logging.info("BananaEnv - Version {}".format(self.__version__))
    self.MAX_PRICE = 2.0
  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human'):
    ...
  def close(self):
    ...
