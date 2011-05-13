# coding=UTF-8
from datetime import datetime
from tddd27.surface.application import *

class MainController(ApplicationController):
    def index(self):
        self.pushAddChannel("**global_chat")
        return self.render('main.index')
    
    def msg_submit(self):
        body = self.post.get("body", "-")
        username = self.post.get("username", "John Doe")
        timestamp = datetime.now().strftime("%H:%M")

        message = { "body": body, "username": username, "timestamp": timestamp}
        Push.sendToChannel("**global_chat", "ChatMsgReceived", message)
        return SurfaceResponse("ok")
