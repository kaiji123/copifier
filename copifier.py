import pyperclip
import time
from collections import deque
import keyboard

class ClipboardMonitor:
    def __init__(self, max_items=10000):
        self.clipboard_history = deque(maxlen=max_items)
        self.last_clipboard_text = ""

    def run(self):
        while True:
            
            clipboard_text = pyperclip.paste()

            if clipboard_text != self.last_clipboard_text:
                self.clipboard_history.appendleft(clipboard_text)
                self.last_clipboard_text = clipboard_text
                print(self.clipboard_history)
            if keyboard.is_pressed('ctrl+v'):
                time.sleep(0.05)
                if len(self.clipboard_history) > 0:
                    last_item = self.clipboard_history.popleft()
                    print(last_item)
                    pyperclip.copy(last_item)
                    time.sleep(0.01)
                    

                    
                    
    
            

if __name__ == "__main__":
    monitor = ClipboardMonitor()

    try:
        monitor.run()
    except KeyboardInterrupt:
        print("Clipboard monitor stopped.")
