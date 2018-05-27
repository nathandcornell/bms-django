import abc

class MessageTemplate(metaclass=abc.ABCMeta):
    # Override these in child classes
    ATTRIBUTE_KEYS = []
    ALARM_AND_STATUS_BITMASKS = {}
    SAMPLE_DATA = {}

    # Pass an options dict to instantiate.
    def __init__(self, options={}):
        for key in self.ATTRIBUTE_KEYS:
            setattr(self, key, options[key].strip())

        setattr(self, 'alarm_and_status', int(options["alarm_and_status"].strip(), 16))

        for key in self.ALARM_AND_STATUS_BITMASKS:
            setattr(self, key, self.parse_alarm_or_status_by_name(key))

    def parse_alarm_or_status_by_name(self, code):
        bitmask = int(self.ALARM_AND_STATUS_BITMASKS[code], 2)
        return (bitmask & self.alarm_and_status) > 0

    @abc.abstractmethod
    def createMessage(self):
        """ Create the associated message type """
        return
