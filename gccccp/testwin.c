#include <unistd.h>
#include <stdlib.h>
#include <curses.h>

int main()
{
    initscr();

    move(5,15);
    printw("%s","Hello world!");
    refresh();



    sleep(10);

    endwin();
    exit(EXIT_SUCCESS);

}
