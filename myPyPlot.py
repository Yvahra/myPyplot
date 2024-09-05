import sys

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as font_manager
import os

print(os.path.dirname(sys.executable))

font_dir = [os.path.join(os.path.dirname(__file__), 'fonts/')]
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)
mpl.rcParams['font.family'] = 'Ubuntu'

def customBars(x, y):
    plt.bar(x,y)
    plt.show()