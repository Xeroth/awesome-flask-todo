#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager,Server
# 自己导自己
from app import app

manager = Manager(app)

manager.add_command("runserver",Server(host='0.0.0.0',port=5000, use_debugger=True))

if  __name__ == '__main__':
    manager.run()
