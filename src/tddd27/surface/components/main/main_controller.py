# coding=UTF-8
from datetime import datetime
from tddd27.surface.application import *

class MainController(ApplicationController):
    def index(self):
        self.pushAddChannel("**global_chat")
        return self.render('main.index')
    
    def msg_submit(self):
        return SurfaceResponse("ok")
