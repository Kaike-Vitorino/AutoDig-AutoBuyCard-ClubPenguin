import pyautogui

times = 40

while True:
    times = times - 1

    print(times)

    if times == 0:
        break

    pyautogui.click(1187,758)
    pyautogui.click(852,735)
    pyautogui.click(940,729)