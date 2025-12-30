import keyboard #keyboard
import mouse #Mouse

ctrl_pressed = False #key pressed status

def press_ctrl(e):
    global ctrl_pressed 
    if not ctrl_pressed:
        ctrl_pressed = True
        mouse.press("left")   # Hold down left mouse button
        #print("Left Ctrl pressed → Mouse button down")

def release_ctrl(e):
    global ctrl_pressed
    if ctrl_pressed:
        ctrl_pressed = False
        mouse.release("left") # Release left mouse button
        #print("Left Ctrl released → Mouse button up")

# Bind Left Ctrl press/release
keyboard.on_press_key("ctrl", press_ctrl)
keyboard.on_release_key("ctrl", release_ctrl)

# Keep the program running
keyboard.wait("esc")  # Press Esc to exit

#change the button from left ctrl to user defined buttons in the gui and cli versions
#Add a toggle button to activate or deactivete service in the background.