import argparse
from pynput import keyboard
import time

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key to repeat",default='j')
parser.add_argument("--stopkey", help="key to stop repeat",default='x')
parser.add_argument("--interval", help="interval of key press",type=float,default=5)
args = parser.parse_args()

def on_press_start(key):
    return False

def on_press_loop(key):
    if hasattr(key,'char') and key.char==args.stopkey:
        return False

def ctrl_w(delay):
    time.sleep(delay)
    key_ctrl=keyboard.Controller()
    key_ctrl.press(keyboard.Key.ctrl)
    key_ctrl.press('w')
    time.sleep(0.1)
    key_ctrl.release(keyboard.Key.alt)
    key_ctrl.release('w')

def task_switch():
    key_ctrl=keyboard.Controller()
    key_ctrl.press(keyboard.Key.alt)
    key_ctrl.press(keyboard.Key.tab)
    time.sleep(0.1)
    key_ctrl.release(keyboard.Key.alt)
    key_ctrl.release(keyboard.Key.tab)

key_ctrl=keyboard.Controller()

with keyboard.Listener(on_press=on_press_start) as listener:
    key_ctrl.press(args.key)#start
    task_switch()
    listener.join()


with keyboard.Listener(on_press=on_press_loop) as listener:
    while True:
        key_ctrl.press(args.key)
        time.sleep(args.interval)
        if not listener.running:
            break

task_switch()
ctrl_w(0.5)
