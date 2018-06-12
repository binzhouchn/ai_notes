from __future__ import unicode_literals
from .logic_adapter import LogicAdapter


class SpecificResponseAdapter(LogicAdapter):
    """
    Return a specific response to a specific input.

    :kwargs:
        * *input_text* (``str``) --
          The input text that triggers this logic adapter.
        * *output_text* (``str``) --
          The output text returned by this logic adapter.
    """

    def __init__(self, **kwargs):
        super(SpecificResponseAdapter, self).__init__(**kwargs)
        from bak_chatterbot.conversation import Statement

        self.input_text = kwargs.get('input_text')
        print("self.input_text",self.input_text)
        output_text = kwargs.get('output_text')
        print("output_text",output_text)
        self.response_statement = Statement(output_text)
        print("self.response_statement",self.response_statement)

    def can_process(self, statement):
        if statement == self.input_text:
            return True

        return False

    def process(self, statement):
        print("statement",statement)

        if statement == self.input_text:
            self.response_statement.confidence = 1
        else:
            self.response_statement.confidence = 0
        print("self.response_statement2:",self.response_statement)

        return self.response_statement
