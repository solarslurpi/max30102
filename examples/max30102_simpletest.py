# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""This is a very simple example for you to start using this library.
    """
# import sys
import board
import busio
import adafruit_max30102

i2c = busio.I2C(board.SCL, board.SDA)
max30102 = adafruit_max30102.MAX30102(i2c)
print(f'The part id is {max30102.part_id}')


# def is_max30102():
#     """Check if the MAX30102 is working as expected.  It will print out the
#     error message set when the error occured.  This example does not use the
#     function.  It is included to show a more robust way of
#     :return: True or False
#     :rtype: bool
#     """
#     try:
#         adafruit_max30102.MAX30102(i2c)
#     except AttributeError as error:
#         print(error)
#         return True
#     return False
