class SymbolTable:
    def __init__(self):
        self._symbol_table = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
                              'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
                              'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
                              'SCREEN': 16384, 'KBD': 24576,
                              'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}
        self._variable_address = 16  # variable address counter

    # add a new symbol to the table
    def add(self, key, value):
        self._symbol_table[key] = value

    # returns the value of a given symbol
    def get(self, key):
        # if the key is not in the table, it means that it is a variable that was not added yet
        if key not in self._symbol_table:
            # add the new variable in the table with the current address counter value
            self.add(key, self._variable_address)
            # increase the counter so the next new variable will get the next available address
            self._variable_address += 1
        return self._symbol_table[key]
