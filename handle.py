#-*- coding:utf-8 -*-
# filename:handle.py

import hashlib
import web
import reply
import receive
import urllib2
import json

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is",webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                data = urllib2.urlopen('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+recMsg.Content)
                a = data.read()
                print 'data.read()'
                d = json.loads(a)
                content = d['content'].encode('utf-8')
                replyMsg = reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()
            else:
                print "暂不处理"
                return "success" # 返回成功
        except Exception,Argment:
			print Argment
			return Argment

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
               return "Hello,this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "zhaogongzuo2019"
    
            list = [token,timestamp,nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update,list)
            hashcode = sha1.hexdigest()
            print "handle/GET func:hashcode,signature:",hashcode,signature
            if hashcode == signature:
                return echostr
            else:    
                return ""
        except Exception,Argument:
            return Argument

