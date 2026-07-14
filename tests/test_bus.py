"""
Test EduMCU Core function

"""

# To import the EduMCU Core from root file
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(__file__)
    )
)



from bus import Bus
from bus_device import BusDevice


class DummyDevice(BusDevice):

    def __init__(self):

        super().__init__(0x5000, 16)

        self.value = 0


    def read(self, address):

        print("Lecture :", hex(address))

        return self.value


    def write(self, address, value):

        print("Ecriture :", hex(address), value)

        self.value = value



class Dummy2(BusDevice):

    def __init__(self):

        super().__init__(0x5010,16)

    def read(self,address):

        return 999

    def write(self,address,value):

        pass


class BadDevice(BusDevice):

    def __init__(self):

        super().__init__(0x5008,16)

    def read(self,address):

        return 0

    def write(self,address,value):

        pass





bus = Bus()

device = DummyDevice()

bus.attach(device)

print(bus)

print(len(bus))

print(
    bus.read(0x5000)
)

bus.write(
    0x5000,
    1234
)

print(
    bus.read(0x5000)
)

bus.attach(
    Dummy2()
)

print(
    bus.read(0x5010)
)

##bus.attach(
##    BadDevice()
##)

bus.read(
    0x7000
) # AN ERROR IS EXECTED BECAUSE IT READS A NON MAPPED MEMEORY ADDRESS (IT IS PART OF THE FUNCTIONNAL TEST)


