import pystray
import SystemCommands
import sys
import time
from pystray import MenuItem as item
from PIL import Image, ImageDraw



state = False

def on_clicked(icon, item):
    global state
    state = not item.checked


def action(icon):
    icon.visible = False 
    icon.stop()
    sys.exit()
    pass

def run():
    
    height = 512
    width = 512

    image = Image.new('RGB', (width, height), 'black')
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill='red')
    dc.rectangle((0, height // 2, width // 2, height), fill='red')

    menu = (item('name', action), item('name', action))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

run()