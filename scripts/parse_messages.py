from bus_messages.services.message_parser import MessageParser
import serial

serial_reader = serial.Serial(\
    port='/dev/ttyS0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    xonxoff=True,\
    timeout=0)

while True:
    new_message = serial_reader.readline()
    parser = MessageParser(new_message)
    template = parser.message_template()
    template.createMessage()

serial_reader.close()

# sample_data = ModuleTemplate.SAMPLE_DATA
# parser = MessageParser(','.join(sample_data.values()))
# template = parser.message_template()
# module_args = template.__dict__
# module_message = ModuleMsg(**module_args)
# moduleMsg.save()
# template.createMessage()
