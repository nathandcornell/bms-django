import csv
from io import BytesIO
from .string_template import StringTemplate
from .module_template import ModuleTemplate
from .unknown_message_type_error import UnknownMessageTypeError

class MessageParser:
    STRING_TYPE = 'S'
    MODULE_TYPE = 'M'
    
    message_array_memo = []
    reader_memo = None

    def __init__(self, message_string):
        self.message_string = BytesIO(message_string).read().decode('ascii')

    def reader(self):
        if self.reader_memo is None:
            self.reader_memo = csv.reader([self.message_string], delimiter=',')
        return self.reader_memo

    def message_array(self):
        if len(self.message_array_memo) <= 0:
            self.message_array_memo = next(self.reader())
        return self.message_array_memo

    def message_type(self):
        return self.message_array()[1].strip()

    def message_dict(self):
        if self.message_type() == self.STRING_TYPE:
            return dict(zip(StringTemplate.ATTRIBUTE_KEYS, self.message_array()))
        elif self.message_type() == self.MODULE_TYPE:
            return dict(zip(ModuleTemplate.ATTRIBUTE_KEYS, self.message_array()))

    def message_template(self):
        if self.message_type() == self.STRING_TYPE:
            return StringTemplate(self.message_dict())
        elif self.message_type() == self.MODULE_TYPE:
            return ModuleTemplate(self.message_dict())
        else:
            raise UnknownMessageTypeError("Unknown message type: " + self.message_type)
