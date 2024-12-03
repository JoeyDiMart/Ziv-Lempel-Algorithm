'''
Get a basic understanding of compressing data
'''


class LZBasic:
    def __init__(self, message, substr_dict=None):
        if substr_dict is None:
            substr_dict = {}
        self._message = message
        self._substr_dict = substr_dict

    # define getters/setters so I can call using dot notation
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def substr_dict(self):
        return self._substr_dict

    @substr_dict.setter
    def substr_dict(self, substr_dict):
        self._substr_dict = substr_dict
