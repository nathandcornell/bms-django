from django.db import models

class StringMsg(models.Model):
    protocol_id = models.CharField(max_length=3)
    message_type = models.CharField(max_length=1)
    message_length = models.IntegerField()
    message_id = models.CharField(max_length=255)
    string_id = models.CharField(max_length=3)
    state = models.CharField(max_length=1)
    state_of_charge = models.IntegerField()
    temperature = models.IntegerField()
    voltage = models.IntegerField()
    amperes = models.IntegerField()
    alarm_and_status = models.BigIntegerField()
    bms_assembly_revision = models.IntegerField()
    bms_serial_no = models.CharField(max_length=16)
    bms_master_software_version = models.CharField(max_length=4)
    bms_slave_software_version = models.CharField(max_length=4)
    watt_hours_to_discharge = models.IntegerField()
    watt_hours_to_charge = models.IntegerField()
    min_cell_millivolts = models.IntegerField()
    max_cell_millivolts = models.IntegerField()
    front_power_temperature = models.IntegerField()

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
    bms_self_check_warning = models.BooleanField(default=False)
    under_volt_disable = models.BooleanField(default=False)
    over_volt_disable = models.BooleanField(default=False)
    string_contactor_on = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # SAMPLE_DATA = {
    #     'protocol_id': '001',
    #     'message_type': 'S',
    #     'message_length': '122',
    #     'message_id': '078',
    #     'string_id': '00',
    #     'state': 'I',
    #     'state_of_charge': '053',
    #     'temperature': '020',
    #     'voltage': '025840',
    #     'amperes': '00003',
    #     'alarm_and_status': '80000000', # Temperature Fault only
    #     'bms_assembly_revision': '002',
    #     'bms_serial_no': '1607150018800',
    #     'bms_master_software_version': '887',
    #     'bms_slave_software_version': '842',
    #     'watt_hours_to_discharge': '000509',
    #     'watt_hours_to_charge': '000451',
    #     'min_cell_millivolts': '003664',
    #     'max_cell_millivolts': '003744',
    #     'front_power_temperature': '020'
    # }
