import sys  # gives access to sys.stdin, the keyboard input
import tty  # reads and changes the terminal settings, only exists on Linux/macOS
import termios  # has shortcut functions that change several termios settings at once

def read_input():
    file_descriptor = sys.stdin.fileno()    # returns the file descriptor (usually a small number like 0) for standard input.
                                            # the termios functions need to know it to know which terminal to change
    old_terminal_settings = termios.tcgetattr(file_descriptor) # saves the terminal's current settings to that they can later be restored

    try:
        tty.setcbreak(file_descriptor)      # switches the terminal into cbreak mode. Keys are delivered one at a time without 
                                            # waiting for Enter, and they aren't echoed on screen. Ctrl+c still works.
        single_character = sys.stdin.read(1)  # Waits until a key is pressed and reads one character
        if single_character == '\033':        # '\033' is the Esc character. If the first character is esc, it's the start of an arrow-key sequence, so this reads the
            single_character += sys.stdin.read(2)   # next two characters ([ and A/B/C/D) and adds them on. 

        return single_character               # returns the key, either a single character like 'a' or an arrow sequence like '\033[A'

    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_terminal_settings)  # finally always runs, even if Ctrl+C interrupts the read, so the terminal settings are always
                                                       # restored. TCSADRAIN means "apply the change once any pending output has been written", so 
                                                       # that nothing that's already printed gets cut off.

if __name__ == '__main__':
    print('Press ctrl+c to quit')
    while True:
        print(repr(read_input()))                      # repr() shows the escape character as \x1b (Python's way of writing \033) instead of printing it
                                                       # , so you can see exactly what each key sends. 