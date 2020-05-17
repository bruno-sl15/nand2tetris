import re


class Parser(object):
    def __init__(self):
        self._a_instruction = ''
        self._c_instruction = ''

    def set_a_instruction(self, instruction):
        self._a_instruction = instruction

    def set_c_instruction(self, instruction):
        self._c_instruction = instruction

    def comp(self):
        if '=' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[1]
        else:
            return re.split('[=;]', self._c_instruction)[0]

    def dest(self):
        if '=' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[0]
        else:
            return ''

    def jump(self):
        if ';' in self._c_instruction:
            return re.split('[=;]', self._c_instruction)[-1]
        else:
            return ''

    def number(self):
        return int(self._a_instruction[1:])
