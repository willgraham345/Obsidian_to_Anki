"""Namespace for AnkiConnect functions."""

import json
import urllib.request
import os


class AnkiConnect:
    """Namespace for AnkiConnect functions.

    This class provides methods to interact with the AnkiConnect API,
    handling request formatting, invocation, and response parsing.
    """

    def __init__(self, port: int = 8765):
        """Initializes the AnkiConnect instance with a specific port."""
        self.port = port
        self.host = "localhost"
        if os.environ.get("WSL_DISTRO_NAME"):
            self.host = "127.0.0.1"


    def request(self, action: str, **params) -> dict:
        """Formats an action and its parameters into an AnkiConnect-compatible request.

        :param action: The AnkiConnect API action to perform (e.g., "addNote", "findNotes").
        :type action: str
        :param params: Arbitrary keyword arguments representing the parameters for the action.
        :type params: dict
        :returns: A dictionary formatted as an AnkiConnect request.
        :rtype: dict
        """
        return {'action': action, 'params': params, 'version': 6}

    def invoke(self, action: str, **params) -> dict:
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
            self.request(action, **params)
        ).encode('utf-8')
        response = json.load(urllib.request.urlopen(
            urllib.request.Request(f'http://{self.host}:{self.port}', requestJson)))
        return self.parse(response)

    def parse(self, response: dict) -> dict:
        """Parses the received AnkiConnect response.

        This method validates the response structure and extracts the 'result' field.

        :param response: The raw dictionary response received from AnkiConnect.
        :type response: dict
        :returns: The 'result' field from the response.
        :rtype: dict
        :raises Exception: If the response has an unexpected number of fields,
                           is missing required fields ('error' or 'result'),
                           or if the 'error' afindNotesicates an AnkiConnect error.
        """
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']
