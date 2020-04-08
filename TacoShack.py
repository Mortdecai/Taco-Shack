import keyboard as kb;
import time;
import random as r;

i = 0;

def main():
    global i;

    time_add = r.randint(0, 30);

    kb.write("!tips");
    kb.press_and_release('Enter');

    if ((i % 2) == 0):
        kb.write("!work");
        kb.press_and_release('Enter');

    i += 1;
    time.sleep(300 + time_add);
    main();

main();

