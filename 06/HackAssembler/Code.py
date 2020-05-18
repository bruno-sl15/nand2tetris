# Translates each fields into its corresponding binary value
class Code:
    _comp_codes = {'0': '0101010',
                   '1': '0111111',
                   '-1': '0111010',
                   'D': '0001100',
                   'A': '0110000', 'M': '1110000',
                   '!D': '0001101',
                   '!A': '0110001', '!M': '1110001',
                   '-D': '0001111',
                   '-A': '0110011', '-M': '1110011',
                   'D+1': '0011111',
                   'A+1': '0110111', 'M+1': '1110111',
                   'D-1': '0001110',
                   'A-1': '0110010', 'M-1': '1110010',
                   'D+A': '0000010', 'D+M': '1000010',
                   'D-A': '0010011', 'D-M': '1010011',
                   'A-D': '0000111', 'M-D': '1000111',
                   'D&A': '0000000', 'D&M': '1000000',
                   'D|A': '0010101', 'D|M': '1010101'}

    _dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']

    _jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def __init__(self):
        self._symbol_table = None

    def set_symbol_table(self, symbol_table):
        self._symbol_table = symbol_table

    # return the computation bits of a given C-instruction comp field
    def comp(self, c):
        # get in the _comp_codes dictionary the corresponding binary value of the given computation field
        return self._comp_codes[c]

    # return the destination bits of a given C-instruction dest field
    def dest(self, d):
        # get the index of the dest_codes array and coverts it to binary
        # which is the corresponding binary value of the given destination field
        return bin(self._dest_codes.index(d)).replace('0b', '').replace('-0b', '').zfill(3)

    # return the jump bits of a given C-instruction jump field
    def jump(self, j):
        # same logic of dest()
        return bin(self._jump_codes.index(j)).replace('0b', '').replace('-0b', '').zfill(3)

    # return the 15-bits value of a A-Instruction
    def value(self, value):
        try:
            # return the 15-bits binary value corresponding to the given decimal value
            return bin(int(value)).replace('0b', '').replace('-0b', '').zfill(15)
        except ValueError:
            # if value is not a decimal then it's a symbol
            # consult the symbol table to obtain the corresponding value and call value again
            # but now with a proper decimal value
            return self.value(self._symbol_table.get(value))
