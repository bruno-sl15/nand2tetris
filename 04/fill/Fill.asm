// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite x that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(RESTART)
    @KBD
    D = M
    @NOT_PRESSED
    D ; JEQ // if RAM[KBD] == 0 goto NOT_PRESSED

    (PRESSED)
        @pixels
        M = -1 // pixels = 1111111111111111
        @DRAW
        0 ; JMP // goto DRAW

    (NOT_PRESSED)
        @pixels
        M = 0 // pixels = 0000000000000000

    (DRAW)
        @SCREEN
        D = A
        @addr
        M = D // addr = SCREEN

        (LOOP)
            @addr
            D = M
            @KBD
            D = A - D
            @RESTART       
            D ; JEQ // if addr == last_word goto RESTART

            @pixels
            D = M
            @addr
            A = M
            M = D // RAM[addr] = pixels
            
            @addr
            M = M + 1 // addr = addr + 1

            @LOOP
            0 ; JMP // goto x


        