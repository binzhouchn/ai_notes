"""
__title__ = '__init__.py'
__author__ = 'Zhoubin'
__mtime__ = '2018/6/8'
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.sn_utils import *
import logging
from flask import Flask
from flask import request
from flask import make_response,Response
from flask import jsonify
from sn_com.robot_init import *
import datetime

# logging.basicConfig(level=logging.INFO)

# 抛出flask异常类
class CustomFlaskErr(Exception):

    # 自己定义了一个 responseCode，作为粗粒度的错误代码
    def __init__(self, responseCode=None):
        Exception.__init__(self)
        self.responseCode = responseCode
        self.J_MSG = {9704: '参数不合法',9999:'系统内部异常'}

    # 构造要返回的错误代码和错误信息的 dict
    def get_dict(self):
        rv = dict()
        # 增加 dict key: response code
        rv['responseCode'] = self.responseCode
        # 增加 dict key: responseMsg, 具体内容由常量定义文件中通过 responseCode 转化而来
        rv['responseMsg'] = self.J_MSG[self.responseCode]
        return rv

class HelloChat():
    def __init__(self):
        self.chatbot = ChatBot('Hello Bot',
                               storage_adapter='chatterbot.storage.SQLStorageAdapter',
                               logic_adapters=[
                                   # {
                                   #     'import_path': 'chatterbot.logic.LownewConfidenceAdapter',
                                   #     'threshold': 0.5,
                                   #     'default_response': '正在学习中'
                                   # }
                                   #     {
                                   #         'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                                   #         'input_text': '你好好',
                                   #         'output_text': '我很好，您好！有什么可以帮您？'
                                   #     },
                                   {
                                       'import_path': 'chatterbot.logic.RobotbestMatch'
                                   },
                               ],
                               input_adapter='chatterbot.input.SN_TerminalAdapter',
                               output_adapter='chatterbot.output.SN_TerminalAdapter',
                               database='./chatterbot_data/database.sqlite3',
                               read_only=True
                               )
        ## 已经在自己修改的logic中训练了加入内存了；如果走机器人默认的则需要把注释去掉
        # self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        # self.chatbot.train('C:/Users/16121360/Desktop/chatterboot/chatterbot/sn_data/sn_ori_data/finance.yml')

    def get_response(self, info,source):
        print("info:", info)
        return self.chatbot.sn_get_response(info,source)

if __name__ == '__main__':
    
    chat = HelloChat()

    app = Flask(__name__)
	app.config['JSON_AS_ASCII'] = False

    @app.route('/')
    def get_simple_test():
        return 'BINZHOU TEST'

    @app.route('/req_message', methods=['POST'])
    def req_message():
        if request.method == 'POST':
            receive_dict = sn_receive(request.form)
            logger_robot.debug("接收报文时间：{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            logger_robot.info('接收报文：{}'.format(receive_dict))
            if not sn_get_flag(receive_dict):
                logger_robot.info('参数不合法：{}'.format(9704))
                raise CustomFlaskErr(responseCode=9704)
            bot_answer = chat.get_response(request, receive_dict['source'])
            if 'err_code' in bot_answer.keys():
                logger_robot.info('系统内部异常：{}'.format(9999))
                raise CustomFlaskErr(responseCode=9999)
            result = sn_result(receive_dict, bot_answer)
            logger_robot.info('发送报文：{}'.format(result))
            return jsonify(result)

    @app.errorhandler(CustomFlaskErr)
    def handle_flask_error(error):
        # response 的 json 内容为自定义错误代码和错误信息
        response = jsonify(error.get_dict())
        response.responseCode = error.responseCode
        return response
    app.run(threaded=True,host='0.0.0.0',
port=5000)

