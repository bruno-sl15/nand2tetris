import re


#  Unpack each instruction into its underlying fields
class Parser:
    def __init__(self):
        self._a_instruction = ''
        self._c_instruction = ''

    def set_a_instruction(self, instruction):
        self._a_instruction = instruction

    def set_c_instruction(self, instruction):
        self._c_instruction = instruction

    # return the computation field of the current C-Instruction
    def comp(self):
        if '=' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[1]
        else:
            return re.split('[=;]', self._c_instruction)[0]

    # return the destination field of the current C-Instruction
    def dest(self):
        if '=' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[0]
        else:
            return ''

    # return the jump field of the current C-Instruction
    def jump(self):
        if ';' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[-1]
        else:
            return ''

    # return the value of the current A-Instruction
    def value(self):
        return self._a_instruction[1:]
