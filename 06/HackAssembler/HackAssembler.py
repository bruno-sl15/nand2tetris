from .Parser import Parser
from .Code import Code
import sys


class HackAssembler(object):
    def __init__(self, file_name):
        self._parser = Parser()  # Parser object
        self._code = Code()  # Code object
        asm_file = open(file_name, 'r')  # open the asm file
        self._instructions = asm_file.read().split('\n')  # initialize a list with the assembly instructions
        asm_file.close()  # close the asm file
        self._line = 0  # assembly instructions line counter
        self._hack_file_name = file_name.split('.asm')[0] + '.hack'  # name of the output hack file
        self._hack_file = open(self._hack_file_name, 'w')  # opens the output hack file in writing mode
        self._hack_file = open(self._hack_file_name, 'r')  # opens the output hack file in reading mode
        self._machine_code = self._hack_file.readlines()  # initialize a list for the output hack instructions
        self._pass()

    # recursively iterate and translate each assembly instruction to hack machine code
    def _pass(self):
        # keep iterating if there still remain instructions
        if self._line < len(self._instructions):
            # translate if the current line is a real instruction
            if self._is_instruction():
                instruction = self._remove_comment()
                if self._is_c_instruction(instruction):  # translate a C-Instruction
                    self._parser.set_c_instruction(instruction)
                    c = self._parser.comp()
                    d = self._parser.dest()
                    j = self._parser.jump()
                    cc = self._code.comp(c)
                    dd = self._code.dest(d)
                    jj = self._code.jump(j)
                    out = '111' + cc + dd + jj
                else:  # translate a A-Instruction
                    self._parser.set_a_instruction(instruction)
                    n = self._parser.number()
                    nn = self._code.number(n)
                    out = '0' + nn
                self._machine_code.append(out)
            self._line += 1  # increment the line counter
            self._pass()  # move to the next recursive iteration
        else:  # finish the iterations
            self._hack_file = open(self._hack_file_name, 'w')
            self._hack_file.writelines(self._machine_code)
            self._hack_file.close()

    # return True if the current line (instructions[line]) is a assembly instruction
    # return False if the current line is a blank line or a comment line
    def _is_instruction(self):
        instruction = self._instructions[self._line].replace(' ', '')
        return instruction != '' and instruction[0:2] != '//' and instruction[0] != '('

    # remove the in-line comments of a assembly instruction
    def _remove_comment(self):
        instruction = self._instructions[self._line].replace(' ', '')
        return instruction.split('//')[0]

    # return True if the instruction argument is a C-Instruction
    # return False if the instruction argument is a A-Instruction
    @staticmethod
    def _is_c_instruction(instruction):
        return instruction[0] != '@'


def main():
    if len(sys.argv) != 2:
        print('Usage: HackAssembler Xxx.asm')
    else:
        file_name = sys.argv[1]
        HackAssembler(file_name)


main()
