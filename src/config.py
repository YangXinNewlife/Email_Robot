# -*- coding:utf- 8 -*-
__author__ = 'yx'
import ConfigParser
import sys
import os
reload(sys)
class LocalConfig(object):
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        #parser config.conf
        conf_path = os.path.join(os.path.dirname(__file__), '../config/config.conf')
        cf.read(conf_path)
        #sender
        self.sender_address = self.resolveEnv(cf.get("sender", "account"))
        self.sender_passwd = self.resolveEnv(cf.get("sender", "password"))
        self.sender_server = self.resolveEnv(cf.get("sender","server"))
        #received
        self.received_address = self.resolveEnv(cf.get("received", "account"))


    def reload(self):
        cf = ConfigParser.ConfigParser()
        #parser config.conf
        conf_path = os.path.join(os.path.dirname(__file__), '../config/config.conf')
        cf.read(conf_path)
        #sender
        self.sender_address = self.resolveEnv(cf.get("sender", "account"))
        self.sender_passwd = self.resolveEnv(cf.get("sender", "password"))
        self.sender_server = self.resolveEnv(cf.get("sender","server"))
        #received
        self.received_address = self.resolveEnv(cf.get("received", "account"))

    def resolveEnv(self, con):
        if con.startswith('ENV_'):
            return os.environ.get(con)
        return con

config = LocalConfig()
