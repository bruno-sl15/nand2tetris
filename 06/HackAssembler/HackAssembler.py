from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys


# This implementation assumes that the given asm file has no sintax errors
class HackAssembler:
    def __init__(self, file_name):
        self._parser = Parser()  # Parser object
        self._code = Code()  # Code object
        self._symbol_table = SymbolTable()  # SymbolTable object
        asm_file = open(file_name, 'r')  # open the asm file
        self._instructions = asm_file.read().split('\n')  # initialize a list with the assembly instructions
        asm_file.close()  # close the asm file
        self._hack_file_name = file_name.split('.asm')[0] + '.hack'  # name of the output hack file
        self._machine_code = []  # initialize a list for the output hack instructions
        self._first_pass()
        self._second_pass()

    # iterate to search for label declarations and put this labels in the symbol table
    def _first_pass(self):
        pc = 0  # program counter
        for line in self._instructions:
            # increase the pc only if the pass find a real instruction
            if self._is_instruction(line):
                pc += 1
            elif self._is_label_declaration(line):
                # extract the label name from the instruction line
                label = self._remove_comment(line).replace('(', '').replace(')', '')
                # add the label to the symbol table
                self._symbol_table.add(label, pc)
        # now that the symbol table has all labels, we set the symbol table to the Code object
        self._code.set_symbol_table(self._symbol_table)

    # iterate and translate each assembly instruction to hack machine code
    def _second_pass(self):
        for line in self._instructions:
            # translate if the current line is a real instruction
            if self._is_instruction(line):
                instruction = self._remove_comment(line)
                if self._is_c_instruction(instruction):  # translate a C-Instruction
                    comp, dest, jump = self._translate_c_instruction(instruction)
                    out = '111' + comp + dest + jump
                else:  # translate a A-Instruction
                    value = self._translate_a_instruction(instruction)
                    out = '0' + value  # op_code + value
                self._machine_code.append(out+'\n')
        self._hack_file = open(self._hack_file_name, 'w')  # open the output hack file
        self._hack_file.writelines(self._machine_code)  # write the machine code instructions in the file
        self._hack_file.close()

    # receive an assembly A-Instruction and return the 15-bits address
    def _translate_a_instruction(self, instruction):
        self._parser.set_a_instruction(instruction)
        v = self._parser.value()
        return self._code.value(v)

    # receive an assembly C-Instruction and return a tuple with the 3 layers of machine language
    def _translate_c_instruction(self, instruction):
        self._parser.set_c_instruction(instruction)
        c = self._parser.comp()
        d = self._parser.dest()
        j = self._parser.jump()
        cc = self._code.comp(c)
        dd = self._code.dest(d)
        jj = self._code.jump(j)
        return cc, dd, jj

    def _is_label_declaration(self, line):
        instruction = line.replace(' ', '')
        return instruction != '' and instruction[0] == '('

    # return True if the current line is a assembly instruction
    # return False if the current line is a blank line or a comment line
    def _is_instruction(self, line):
        instruction = line.replace(' ', '')
        return instruction != '' and instruction[0:2] != '//' and instruction[0] != '('

    # remove the in-line comments of a assembly instruction
    def _remove_comment(self, line):
        instruction = line.replace(' ', '')
        return instruction.split('//')[0]

    # return True if the instruction argument is a C-Instruction
    # return False if the instruction argument is a A-Instruction
    def _is_c_instruction(self, instruction):
        return instruction[0] != '@'


def main():
    try:
        for file_name in sys.argv[1:]:
            HackAssembler(file_name)
    except FileNotFoundError:
        print('The files must be in the same directory of HackAssembler.py ')


main()
