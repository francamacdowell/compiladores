class VariableObject(object):

    def __init__(self):
        self.exec_string = ""

    def transpile(self, name, operator, value):
        # Build the python executable string from parser
        self.exec_string += name + " " + operator + " " + value + "\n"
        return self.exec_string