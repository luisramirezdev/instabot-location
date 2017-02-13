#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="usuario_instagram", password="constraseña_instagram",
               like_per_day=400,
               comments_per_day=0,
               tag_list=['girl', 'car', 'cat'],
               max_like_for_one_tag=5,
               follow_per_day=60   ,
               follow_time=5*60*60,
               unfollow_per_day=20,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0)

bot.new_auto_mod()