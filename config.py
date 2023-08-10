#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369481094:AAGbL35ASqPlst9MtSJr-bqFRmjvPB9-p6M")
    API_ID = int(os.environ.get("API_ID", "12678902"))
    API_HASH = os.environ.get("API_HASH", "1d8ba7b8e7a94affb6b4e4f6e9fd1f29")
    AUTH_USERS = "6156231018"

