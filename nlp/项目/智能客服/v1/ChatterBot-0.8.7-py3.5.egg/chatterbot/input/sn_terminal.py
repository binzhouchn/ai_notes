#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'


from __future__ import unicode_literals
from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.utils import input_function

class SN_TerminalAdapter(InputAdapter):
    """
    A user defined input adpater that allow return variables extracted from request
    """
    def _get_dict(self, request):
        sed = request.form.get('sed')
        qq = request.form.get('qq')
        uiid = request.form.get('uiid', 'default_uiid')  # 可为空
       
        input_dict = {'sed':sed,'qq':qq,'uiid':uiid}
        return input_dict

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        input_message = self._get_dict(args[0])
        return Statement(input_message)
