#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

import datetime

def sn_get_flag(r):
    """
    返回True or False来raise error9704报文
    """
    return r['sed'] and r['qq']

def sn_receive(rf):
    '''
    :param rf: request.form
    :return: receive message dict
    '''
    sed = rf.get('sed')
    qq = rf.get('qq')
    uiid = rf.get('uiid', 'default_uiid')  # 可为空
    
    return {'sed':sed,'uiid':uiid,'qq':qq}

def sn_result(receive_dict, bot_answer):
    if 'intentionCode' in bot_answer.keys():
        result = {
            'sed': receive_dict['sed'],
            'qq': receive_dict['qq'],
            'uiid': receive_dict['uiid'],
            'intentionCode': bot_answer['intentionCode'],
            'responseCode': '200',
            'responseMsg': 'success',
            'responseTime': datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        }
    else:
        result = {
            'sed': receive_dict['sed'],
            'qq': receive_dict['qq'],
            'uiid': receive_dict['uiid'],
            'answer': bot_answer['answer'],
            'responseCode': '200',
            'responseMsg': 'success',
            'responseTime': datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        }
    return result