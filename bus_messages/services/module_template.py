from .message_template import MessageTemplate
from ..models.module_msg import ModuleMsg

class ModuleTemplate(MessageTemplate):
    ATTRIBUTE_KEYS = [
        'protocol_id',
        'message_type',
        'message_length',
        'message_id',
        'string_id',
        'module_id',
        'state',
        'state_of_change',
        'min_cell_temperature',
        'avg_cell_temperature',
        'max_cell_temperature',
        'voltage',
        'min_cell_voltage',
        'avg_cell_voltage',
        'max_cell_voltage',
        'amperes',
        'alarm_and_status',
        'assembly_revision',
        'serial_no',
        'master_software_version',
        'slave_software_version',
        'max_front_power_conn_temp'
    ]

    ALARM_AND_STATUS_BITMASKS = {
        'temperature_warning':               '10000000000000000000000000000000',
        'temperature_fault':                 '01000000000000000000000000000000',
        'high_current_warning':              '00100000000000000000000000000000',
        'high_current_fault':                '00010000000000000000000000000000',
        'high_voltage_warning':              '00001000000000000000000000000000',
        'high_voltage_fault':                '00000100000000000000000000000000',
        'low_voltage_warning':               '00000010000000000000000000000000',
        'low_voltage_fault':                 '00000001000000000000000000000000',
        'low_voltage_non_recoverable_fault': '00000000100000000000000000000000',
        'charge_low_warning':                '00000000000010000000000000000000',
        'communication_error':               '00000000000001000000000000000000',
        'communication_fault':               '00000000000000100000000000000000',
        'under_volt_disable':                '00000000000000001000000000000000',
        'over_volt_disable':                 '00000000000000000100000000000000',
        'cell_0_balancing':                  '00000000000000000000000010000000',
        'cell_1_balancing':                  '00000000000000000000000001000000',
        'cell_2_balancing':                  '00000000000000000000000000100000',
        'cell_3_balancing':                  '00000000000000000000000000010000',
        'cell_4_balancing':                  '00000000000000000000000000001000',
        'cell_5_balancing':                  '00000000000000000000000000000100',
        'cell_6_balancing':                  '00000000000000000000000000000010'
    }

    SAMPLE_DATA = {
        'protocol_id': '001',
        'message_type': 'M',
        'message_length': '122',
        'message_id': '419',
        'string_id': '00',
        'module_id': '00',
        'module_state': 'R',
        'module_state_of_change': '051',
        'min_cell_temperature': '022',
        'avg_cell_temperature': '023',
        'max_cell_temperature': '027',
        'module_voltage': '025709',
        'min_cell_voltage': '003653',
        'avg_cell_voltage': '003672',
        'max_cell_voltage': '003710',
        'module_amperes': '00000',
        'alarm_and_status': '80000000',
        'module_assembly_revision': '000',
        'module_serial_no': '1311250000800',
        'master_software_version': '0501',
        'slave_software_version': '0496',
        'max_front_power_conn_temp': '029'
    }

    def createMessage(self):
        ModuleMsg.objects.create(**self.__dict__)
