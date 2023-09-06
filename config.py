#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6496204791:AAEnwkdPmvO-jpL-Or0GcMFhG8c4_alWsS8")
    API_ID = int(os.environ.get("API_ID", "9816169"))
    API_HASH = os.environ.get("API_HASH", "036f0ec50e2a1f943e55a71a7c3feffb")
    AUTH_USERS = "6465999303"

