import pyautogui, time
print("Time to begin >:D")
time.sleep(3)
while True:
    time.sleep(0.1)
    f = open("spamme.txt", "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(3)