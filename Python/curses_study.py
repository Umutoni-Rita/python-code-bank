import curses
from curses import wrapper

#backslash : \\\\\

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello \nWelcome the game! HAHAHAHAA \nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
