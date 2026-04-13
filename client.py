import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

# Conecta ao objeto Printer
base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy for Printer")

# Usa as funcoes do Printer
printer.printString("Hello World!")
printer.printUpperCase("hello world in uppercase!")
printer.printRepeat("Repeat this!", 3)

# Conecta ao novo objeto Calculator
baseCalc = communicator.stringToProxy("SimpleCalculator:default -p 11000")
calculator = Demo.CalculatorPrx.checkedCast(baseCalc)
if not calculator:
    raise RuntimeError("Invalid proxy for Calculator")

# Usa as funcoes do Calculator
result1 = calculator.add(10, 25)
print("add(10, 25) = {}".format(result1))

result2 = calculator.multiply(6, 7)
print("multiply(6, 7) = {}".format(result2))

communicator.destroy()
