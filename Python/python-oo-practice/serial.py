"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        "Create a serial generator that generates serial numbers starting from the given start value"
        self.start = start
        self.increment = 0
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start+self.increment}>"

    def generate(self):
        "Return a new serial number, incremented by 1, each time it is called."
        new_serial = self.start + self.increment
        self.increment+=1
        return new_serial

    def reset(self):
        "Resets the serial numbers generated to begin from the start value again."
        self.increment = 0


