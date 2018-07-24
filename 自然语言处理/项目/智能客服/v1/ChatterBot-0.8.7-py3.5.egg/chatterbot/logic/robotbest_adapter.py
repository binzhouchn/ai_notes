from __future__ import unicode_literals
#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from chatterbot.logic.logic_adapter import LogicAdapter
import sys
sys.path.append('./chatterbot/')
from sn_semantic.semantic_analysis import *


class RobotbestMatch(LogicAdapter):
    """
    A logic adapter that returns a response based on known responses to
    the closest matches to the input statement.
    """

    def get(self, input_statement):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """

        closest_match = input_statement
        closest_match.confidence = 0
        # print("rrclosest_match.text",closest_match.text)
        # semantic_analysis = Semantic_Analysis()
        simi_question=sn_robotbest_match(question=closest_match.text)
        # print("simi_question",simi_question)
        # simi_question=semantic_analysis.word2vec_wmdistance(text=closest_match.text)
        if simi_question['type']==0:
            closest_match.text=simi_question['answer']['answare_text']
            closest_match.confidence=simi_question['Confidence']
        else:
            pass
        return closest_match

    def can_process(self, statement):
        """
        Check that the chatbot's storage adapter is available to the logic
        adapter and there is at least one statement in the database.
        """
        return self.chatbot.storage.count()

    def process(self, input_statement):
        #print("be3input_statement",input_statement)
        # Select the closest match to the input statement
        closest_match = self.get(input_statement)
        #print("be3closest_match",closest_match)
        self.logger.info('Using "{}" as a close match to "{}"'.format(
            input_statement.text, closest_match.text
        ))

        # Get all statements that are in response to the closest match
        response_list = self.chatbot.storage.filter(
            in_response_to__contains=closest_match.text
        )
        #print("be3response_list",response_list)
        if response_list:
            self.logger.info(
                'Selecting response from {} optimal responses.'.format(
                    len(response_list)
                )
            )
            #print("be3input_statement",input_statement)
            #print("be3response_list",response_list)
            response = self.select_response(input_statement, response_list)
            response.confidence = closest_match.confidence
            #print("be3response",response)
            #print("be3response.confidence",response.confidence)
            self.logger.info('Response selected. Using "{}"'.format(response.text))
        else:
            response = self.chatbot.storage.get_random()
            #print("be3response",response)
            self.logger.info(
                'No response to "{}" found. Selecting a random response.'.format(
                    closest_match.text
                )
            )

            # Set confidence to zero because a random response is selected
            response.confidence = 0

        return response
