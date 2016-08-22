#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# Flask 对象的 route 属性
@app.route("/")   # 据说这货是装饰器 ,教程上说是: 创建index方法，使用app.route装饰器绑定路由规则
def index():
    return "Hello World!"

# 这个 name 是什么鬼 - - , 应该表示的是这个程序本身的一个属性吧? 本身的属性为何等于 main?
if __name__ == "__main__":
    app.run()
