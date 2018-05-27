from django.db import models

class ModuleMsg(models.Model):
    protocol_id = models.Charfield()
    message_type = models.Charfield(max_length=1)
    message_length = models.IntegerField()
    message_id = models.Charfield()
    string_id = models.Charfield()
    module_id = models.Charfield()
    module_state = models.Charfield(max_length=1)
    module_state_of_change = models.IntegerField()
    min_cell_temperature = models.IntegerField()
    avg_cell_temperature = models.IntegerField()
    max_cell_temperature = models.IntegerField()
    module_voltage = models.IntegerField()
    min_cell_voltage = models.IntegerField()
    avg_cell_voltage = models.IntegerField()
    max_cell_voltage = models.IntegerField()
    module_amperes = models.IntegerField()
    alarm_and_status = models.IntegerField()
    module_assembly_revision = models.Charfield()
    module_serial_no = models.Charfield()
    master_software_version = models.Charfield()
    slave_software_version = models.Charfield()
    max_front_power_conn_temp = models.IntegerField()

    # Flags
    temperature_warning = models.BooleanField(default=False)
    temperature_fault = models.BooleanField(default=False)
    high_current_warning = models.BooleanField(default=False)
    high_current_fault = models.BooleanField(default=False)
    high_voltage_warning = models.BooleanField(default=False)
    high_voltage_fault = models.BooleanField(default=False)
    low_voltage_warning = models.BooleanField(default=False)
    low_voltage_fault = models.BooleanField(default=False)
    low_voltage_non_recoverable_fault = models.BooleanField(default=False)
    charge_low_warning = models.BooleanField(default=False)
    module_communication_error = models.BooleanField(default=False)
    module_communication_fault = models.BooleanField(default=False)
    under_volt_disable = models.BooleanField(default=False)
    over_volt_disable = models.BooleanField(default=False)
    cell_0_balancing = models.BooleanField(default=False)
    cell_1_balancing = models.BooleanField(default=False)
    cell_2_balancing = models.BooleanField(default=False)
    cell_3_balancing = models.BooleanField(default=False)
    cell_4_balancing = models.BooleanField(default=False)
    cell_5_balancing = models.BooleanField(default=False)
    cell_6_balancing = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTime(auto_now_add=True)
    updated_at = models.DateTime(auto_now=True)

    # SAMPLE_DATA = {
    #     'protocol_id': '001',
    #     'message_type': 'M',
    #     'message_length': '122',
    #     'message_id': '419',
    #     'string_id': '00',
    #     'module_id': '00',
    #     'module_state': 'R',
    #     'module_state_of_change': '051',
    #     'min_cell_temperature': '022',
    #     'avg_cell_temperature': '023',
    #     'max_cell_temperature': '027',
    #     'module_voltage': '025709',
    #     'min_cell_voltage': '003653',
    #     'avg_cell_voltage': '003672',
    #     'max_cell_voltage': '003710',
    #     'module_amperes': '00000',
    #     'alarm_and_status': '80000000', # Temperature Fault only
    #     'module_assembly_revision': '000',
    #     'module_serial_no': '1311250000800',
    #     'master_software_version': '0501',
    #     'slave_software_version': '0496',
    #     'max_front_power_conn_temp': '029'
    # }
