#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .input_adapter import InputAdapter
from .microsoft import Microsoft
from .gitter import Gitter
from .hipchat import HipChat
from .mailgun import Mailgun
from .terminal import TerminalAdapter
from .variable_input_type_adapter import VariableInputTypeAdapter
from .sn_terminal import SN_TerminalAdapter

__all__ = (
    'InputAdapter',
    'Microsoft',
    'Gitter',
    'HipChat',
    'Mailgun',
    'TerminalAdapter',
    'VariableInputTypeAdapter',
    'SN_TerminalAdapter'
)
