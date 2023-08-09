#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369481094:AAGbL35ASqPlst9MtSJr-bqFRmjvPB9-p6M")
    API_ID = int(os.environ.get("API_ID", "28715814"))
    API_HASH = os.environ.get("API_HASH", "16144a759c3872187bb9663e66036685")
    AUTH_USERS = "6156231018"

