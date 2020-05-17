class Parser(object):
    def __init__(self):
        self._a_instruction = ''
        self._c_instruction = ''

    def set_a_instruction(self, instruction):
        self._a_instruction = instruction

    def set_c_instruction(self, instruction):
        self._c_instruction = instruction
