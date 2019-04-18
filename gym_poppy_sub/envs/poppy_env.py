#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:01:10 2019

@author: Shukai
"""

import logging.config
import gym
import cfg_load
from gym import error, spaces, utils
from gym.utils import seeding
import pkg_resources

path = 'config.yaml'  # always use slash in packages
filepath = pkg_resources.resource_filename('gym_banana', path)
config = cfg_load.load(filepath)
logging.config.dictConfig(config['LOGGING'])

class PoppyEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.__version__ = "0.1.0"
    logging.info("hello")
    self.MAX_PRICE = 2.0
  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human'):
    ...
  def close(self):
    ...

