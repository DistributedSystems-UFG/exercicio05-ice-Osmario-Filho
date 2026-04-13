import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printUpperCase(self, s, current=None):
        print(s.upper())

    def printRepeat(self, s, count, current=None):
        for i in range(count):
            print(s)

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        result = a + b
        print("add({}, {}) = {}".format(a, b, result))
        return result

    def multiply(self, a, b, current=None):
        result = a * b
        print("multiply({}, {}) = {}".format(a, b, result))
        return result

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")

printerObj = PrinterI()
adapter.add(printerObj, communicator.stringToIdentity("SimplePrinter"))

calculatorObj = CalculatorI()
adapter.add(calculatorObj, communicator.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()
