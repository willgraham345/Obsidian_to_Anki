"""Namespace for AnkiConnect functions."""

import json
import urllib.request

class AnkiConnect:
    """Namespace for AnkiConnect functions.

    This class provides static methods to interact with the AnkiConnect API,
    handling request formatting, invocation, and response parsing.
    """

    def request(action: str, **params) -> dict:
        """Formats an action and its parameters into an AnkiConnect-compatible request.

        :param action: The AnkiConnect API action to perform (e.g., "addNote", "findNotes").
        :type action: str
        :param params: Arbitrary keyword arguments representing the parameters for the action.
        :type params: dict
        :returns: A dictionary formatted as an AnkiConnect request.
        :rtype: dict
        """
        return {'action': action, 'params': params, 'version': 6}

    def invoke(action: str, **params) -> dict:
        """Invokes an AnkiConnect API action with the specified parameters.

        This method handles the serialization of the request, sends it to the AnkiConnect
        server, and parses the received response.

        :param action: The AnkiConnect API action to perform.
        :type action: str
        :param params: Arbitrary keyword arguments representing the parameters for the action.
        :type params: dict
        :returns: The 'result' field from the AnkiConnect response if successful.
        :rtype: dict
        :raises Exception: If there is an error in the AnkiConnect response or
                           if the response format is unexpected.
        """
        requestJson = json.dumps(
            AnkiConnect.request(action, **params)
        ).encode('utf-8')
        response = json.load(urllib.request.urlopen(
            urllib.request.Request('http://localhost:8765', requestJson)))
        return AnkiConnect.parse(response)

    def parse(response: dict) -> dict:
        """Parses the received AnkiConnect response.

        This method validates the response structure and extracts the 'result' field.

        :param response: The raw dictionary response received from AnkiConnect.
        :type response: dict
        :returns: The 'result' field from the response.
        :rtype: dict
        :raises Exception: If the response has an unexpected number of fields,
                           is missing required fields ('error' or 'result'),
                           or if the 'error' field indicates an AnkiConnect error.
        """
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']
