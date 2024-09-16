# AutoDig and AutoBuyCard for Club Penguin

This project consists of a Python script developed to automate two specific tasks in the game Club Penguin: digging to earn coins (AutoDig) and buying element cards (AutoBuyCard).

## Features

### AutoDig
AutoDig automates the digging process in Club Penguin. It uses user-provided coordinates to locate digging areas and perform the digging action automatically, without manual intervention. This allows players to collect coins more efficiently, quickly, and automatically.

### AutoBuyCard
AutoBuyCard is designed to automate the purchase of cards within the game. With this feature, players can automatically buy element cards multiple times, quickly. This saves time and effort, especially for those looking to spend all their money on cards.

To ensure everything works smoothly, I’ve added a section in the README to highlight the parts of the code where coordinates need to be modified:


## How to Use

1. **Requirements:**
   - Python 3.x installed.
   - Required libraries: PyAutoGUI.
     ```
     pip install pyautogui
     ```
   - Club Penguin installed and running.

2. **Configuration:**
   - Open Club Penguin and navigate to the screen where you want to automate actions.
   - To get the coordinates of the buttons, you can follow this procedure:
     1. Import PyAutoGUI in the Python console.
     2. Use the `pyautogui.displayMousePosition()` function to display the coordinates while moving the mouse over the buttons you want to automate.
     3. Note down the coordinates of the relevant buttons.
   - **AutoDig.py:**
     - The coordinates need to be inserted in the following locations:
       - Line 18: `pyautogui.click(x, y)` - Insert the coordinates of the own profile button.
       - Line 21: `pyautogui.click(x, y)` - Insert the coordinates of the dance button.
       - Line 22: `pyautogui.click(x, y)` - Insert the coordinates of the specific dance button.
       - Line 25: `pyautogui.click(x, y)` - Insert the coordinates of the puffy button.
       - Line 26: `pyautogui.click(x, y)` - Insert the coordinates of the present button.
   - **AutoBuyCard.py:**
     - The coordinates need to be inserted in the following locations:
       - Line 13: `pyautogui.click(x, y)` - Insert the coordinates of the card purchase button.
       - Line 14: `pyautogui.click(x, y)` - Insert the coordinates of the "Yes" button to confirm the purchase.
       - Line 15: `pyautogui.click(x, y)` - Insert the coordinates of the "Ok" button to close the confirmation window.

3. **Execution:**
   - Run the `AutoDig.py` script to use the AutoDig feature.
   - Run the `AutoBuyCard.py` script to use the AutoBuyCard feature.


## License

This project is licensed under the MIT License.
