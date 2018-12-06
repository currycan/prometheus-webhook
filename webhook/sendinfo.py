# coding: utf-8
from models import CmsUser
from alertsendmail import *
from alertsms import *
from alertwechat import wechat_msg


def SendAlert(receiver, alert_content, lev=None):
    toemail_list = list()
    tophone_list = list()
    send_list = CmsUser.objects.filter(group__name=receiver)
    for send_r in send_list:
        print(send_r)
        toemail_list.append(send_r.email.encode('utf8'))
        tophone_list.append(send_r.phone)

    try:
        tomail(toemail_list, alert_content)
    except:
        print 'send mail error'
    try:
        tosms(tophone_list, alert_content)
    except:
        print 'send sms error'


def SendAlert_wechat(receiver, title, alert_content):
    towechat_list = list()
    send_list = CmsUser.objects.filter(group__name=receiver)
    for send_r in send_list:
        print(send_r)
        towechat_list.append(send_r.wechat_id)

    try:
        wechat_msg(towechat_list, title, details=alert_content)
        print(towechat_list)
        print('send wechating')
    except Exception as e:
        print (e)
print 'send wechat error'
