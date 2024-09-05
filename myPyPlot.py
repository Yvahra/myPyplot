import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as font_manager
import os


fontpath = os.path.join(os.path.dirname(__file__), 'fonts/')
font_files = font_manager.findSystemFonts(fontpaths=[fontpath, ])
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
mpl.rcParams['font.family'] = 'Ubuntu'

def customBars(x, y):
    plt.bar(x,y)
    plt.show()