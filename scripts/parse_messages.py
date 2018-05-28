import serial
from bus_messages.services.message_parser import MessageParser
from bus_messages.services.unknown_message_type_error import UnknownMessageTypeError

def run(*args):
    serial_reader = serial.Serial(\
        port='/dev/ttyS0',\
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        xonxoff=True)

    while True:
        try:
            new_message = serial_reader.readline()
            parser = MessageParser(new_message)
            template = parser.message_template()
            template.createMessage()
        except UnknownMessageTypeError as e:
            print('##MessageParser## Warning:')
            print(e.args)
        except Exception as e:
            print('##MessageParser## ERROR:')
            print(e.args)

    serial_reader.close()
