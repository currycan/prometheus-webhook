# coding:utf8
from models import Wechat_Config, Wechat_Log
import requests
import json
from datetime import datetime


def get_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        'corpid': Wechat_Config.objects.get(pk=2).wechat_id,
        'corpsecret': Wechat_Config.objects.get(pk=2).wechat_key,
       }
    req = requests.post(url, params=values)
    data = json.loads(req.text)
    return data["access_token"]


def wechat_msg(w_id, title, details="hello"):
    url = ("https://qyapi.weixin.qq.com/cgi-bin/message/send"
          "?access_token={}").format(get_token())
    for i in w_id:
        values = {
           "touser": i,
           "msgtype": "text",
           "agentid": Wechat_Config.objects.get(pk=2).wechat_agent_id,
           #  'title': u"标题: Prometheus警报信息",
           "text": {
               "content": u"标题: %s \n 详情: %s" %
                          (title, details)
               }
           }
    rs = Wechat_Log.objects.create(wechat=w_id, content=details)
    rs.save()


