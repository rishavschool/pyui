class Printer():
  def __init__(self):
    pass

  def print(self, msg: str = "Hello world!"):
    print(msg)


my_printer = Printer()
my_printer.print()
my_printer.print("special message")