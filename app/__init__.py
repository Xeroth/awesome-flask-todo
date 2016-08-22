#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import config #http://stackoverflow.com/questions/20723713/py-test-import-error-config-not-found

app = Flask(__name__)
# 这是干嘛??
app.config.from_object("config")

from app import views,models
