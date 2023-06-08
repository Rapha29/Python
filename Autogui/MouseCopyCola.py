import pyautogui
from pynput import mouse

copied_text = ""
double_click_count = 0

def on_click(x, y, button, pressed):
    global copied_text, double_click_count

    if button == mouse.Button.left and pressed:
        double_click_count += 1

        if double_click_count == 2:
            if copied_text:
                pyautogui.hotkey("ctrl", "v")
                double_click_count = 0
                copied_text = ""

    elif button == mouse.Button.left and not pressed:
        if double_click_count == 1 and not copied_text:
            pyautogui.hotkey("ctrl", "c")
            double_click_count = 0

# Cria um listener para eventos do mouse
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
