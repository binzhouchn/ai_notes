#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from __future__ import unicode_literals
from .output_adapter import OutputAdapter


class SN_TerminalAdapter(OutputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the terminal.
    """

    def process_response(self, statement, session_id=None):
        """
        Print the response to the user's input.
        """
        return statement
