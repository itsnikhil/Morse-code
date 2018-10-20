import winsound
import re
import time

winsound.PlaySound('1.wav', winsound.SND_FILENAME)
coded = {
    "a": "10111",
    "b": "111101010",
    "c": "1111011110",
    "d": "1111010",
    "e": "10",
    "f": "101011110",
    "g": "11111110",
    "h": "10101010",
    "i": "1010",
    "j": "10111111111",
    "k": "11110111",
    "l": "101111010",
    "m": "111111",
    "n": "11110",
    "o": "111111111",
    "p": "1011111110",
    "q": "11111110111",
    "r": "1011110",
    "s": "101010",
    "t": "111",
    "u": "1010111",
    "v": "101010111",
    "w": "10111111",
    "x": "1111010111",
    "y": "11110111111",
    "z": "1111111010",
    "1": "10111111111111",
    "2": "1010111111",
    "3": "101010111111",
    "4": "10101010111",
    "5": "1010101010",
    "6": "11110101010",
    "7": "111111101010",
    "8": "1111111111010",
    "9": "11111111111110",
    "0": "111111111111111",
    ".": "101111011110111",
    ",": "1111111010111111",
    "?": "10101111111010",
    "": "00",
    " ": "000000",
}


def morse_to_bin(msg):
    morse_msg = ""
    msg = msg.lower()
    for char in msg:
        try:
            morse_msg += coded[char]
        except:
            print(char + " is not defined in morse code!")
    print(msg + " ==> " + morse_msg)
    temp = morse_msg
    while(temp != ""):
        try:
            if(temp.index("000000") == 0):
                time.sleep(6)
                temp = temp[6:]
                continue
        except:
            pass
        try:
            if(temp.index("00") == 0):
                time.sleep(2)
                temp = temp[2:]
                continue
        except:
            pass
        try:
            zero_search = temp.index("0")
            if (zero_search == 1):
                winsound.PlaySound('short_beep.wav', winsound.SND_FILENAME)
                time.sleep(1)
                temp = temp[zero_search + 1:]
            else:
                winsound.PlaySound('long_beep.wav', winsound.SND_FILENAME)
                time.sleep(1)
                temp = temp[3:]
        except:
            winsound.PlaySound('long_beep.wav', winsound.SND_FILENAME)
            time.sleep(1)
            temp = temp[3:]


def bin_to_morse(msg):
    pass


morse_to_bin(input("Enter text you want to convert to morse: "))
