import board
import busio
import time
from DFRobot_Oxygen import *


i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
COLLECT_NUMBER = 10              # collect number, the collection range is 1-100


'''
  The first  parameter is to select iic0 or iic1
  The second parameter is the iic device address
  The default address for iic is ADDRESS_3
  ADDRESS_0                 = 0x70
  ADDRESS_1                 = 0x71
  ADDRESS_2                 = 0x72
  ADDRESS_3                 = 0x73
'''

oxygen = DFRobot_Oxygen_IIC(i2c, OZONE_ADDRESS_3)


while True:
    oxygen_data = oxygen.get_oxygen_data(COLLECT_NUMBER)
    print("oxygen concentration is %4.2f %%vol" % oxygen_data)
    time.sleep(1)
