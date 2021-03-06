# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 happyday
#
# SPDX-License-Identifier: MIT
"""

`adafruit_max30102`
================================================================================
CircuitPython helper library for the MAX30102 pulse oximetry and heart-rate monitor module.

* Author(s): happyday

Based on `whilemind's MAX30100u library for Rasp Pi <https://github.com/whilemind/MAX30100u>`_

Implementation Notes
--------------------

**Hardware:**

* `max30102 module <https://datasheets.maximintegrated.com/en/ds/MAX30102.pdf>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's Bus Device library https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library https://github.com/adafruit/Adafruit_CircuitPython_Register


"""
__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/solarslurpi/max30102.git"


from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct

INT_STATUS = 0x00  # Which interrupts are tripped
INT_ENABLE = 0x01  # Which interrupts are active
FIFO_WR_PTR = 0x02  # Where data is being written
OVRFLOW_CTR = 0x03  # Number of lost samples
FIFO_RD_PTR = 0x04  # Where to read from
FIFO_DATA = 0x05  # Output data buffer
MODE_CONFIG = 0x06  # Control register
SPO2_CONFIG = 0x07  # Oximetry settings
LED_CONFIG = 0x09  # Pulse width and power of LEDs
TEMP_INTG = 0x16  # Temperature value, whole number
TEMP_FRAC = 0x17  # Temperature value, fraction
REV_ID = 0xFE  # Part revision
_PART_ID = 0xFF  # Part ID, normally 11 for the 30100, 21 for the 30102
_MAX30102_ID = 21

_I2C_ADDRESS = 0x57  # I2C address of the MAX30100 device


class MAX30102:
    """Easy access to values in the MAX30102's registers
        """
    _part_id = ROUnaryStruct(_PART_ID, "B")

    def __init__(self, is2c_bus, address=_I2C_ADDRESS):
        self.i2c_device = i2c_device.I2CDevice(is2c_bus, address)
        if self._part_id != _MAX30102_ID:
            raise AttributeError("Cannot find a MAX30102")

    @property
    def part_id(self):
        """The part id of the MAX30102

        :return: The value of the part id stored in the module's PART ID register.
        :rtype: unsigned byte
        """
        return self._part_id
