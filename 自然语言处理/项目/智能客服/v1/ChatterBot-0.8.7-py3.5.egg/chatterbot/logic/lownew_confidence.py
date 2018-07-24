#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from __future__ import unicode_literals
from chatterbot.conversation import Statement
from .best_match import BestMatch


class LownewConfidenceAdapter(BestMatch):
    """
    Returns a default response with a high confidence
    when a high confidence response is not known.

    :kwargs:
        * *threshold* (``float``) --
          The low confidence value that triggers this adapter.
          Defaults to 0.65.
        * *default_response* (``str``) or (``iterable``)--
          The response returned by this logic adaper.
        * *response_selection_method* (``str``) or (``callable``)
          The a response selection method.
          Defaults to ``get_first_response``.
    """

    def __init__(self, **kwargs):
        super(LownewConfidenceAdapter, self).__init__(**kwargs)

        self.confidence_threshold = kwargs.get('threshold', 0.65)

        default_responses = kwargs.get(
            'default_response', "I'm sorry, I do not understand."
        )

        # Convert a single string into a list
        if isinstance(default_responses, str):
            default_responses = [
                default_responses
            ]

        self.default_responses = [
            Statement(text=default) for default in default_responses
        ]

    def process(self, input_statement):
        """
        Return a default response with a high confidence if
        a high confidence response is not known.
        """
        # Select the closest match to the input statement
        closest_match = self.get(input_statement)
        print("lowclosest_match",closest_match)

        response_list = self.chatbot.storage.filter(
            in_response_to__contains=closest_match.text
        )
        # print("be3response_list",response_list)
        if response_list:
            self.logger.info(
                'Selecting response from {} optimal responses.'.format(
                    len(response_list)
                )
            )
            # print("be3input_statement",input_statement)
            #  print("be3response_list",response_list)

        # Choose a response from the list of options
        if closest_match.confidence > self.confidence_threshold:
            response = self.select_response(input_statement, response_list)
            # response.confidence = closest_match.confidence
            response.confidence = 1
        else:
            response = self.select_response(input_statement, self.default_responses)
            response.confidence = 0

        print("lowresponse",response)
        # print("lowclosest_match.confidence",closest_match.confidence)
        # print("lowself.confidence_threshold",self.confidence_threshold)
        # # Confidence should be high only if it is less than the threshold


        return response
