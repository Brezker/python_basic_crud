import sys
# here you have to put your path app folder
sys.path.insert(1,'.')
from datos.conexBD import *
from Menu import showMenu

print('This software has been created by Julian Rodriguez Lopez. (Brezker)')
print('Using Python as the programming language and SQLite as database manager with layers architecture.')
# print('Coded entirely on Linux as Operative System with Manjaro, an Arch based distro.')
# print('It has been preconfigured with a Window Manager to avoid the mouse use the most posible.')
# print('Using neovim as the main code editor, an alternative to the notepad from Windows.')
print('I desided to use SQLite because I wanted to create the database in the data layer by default.')
print('THE ENTIRE DATABASE IS CREATED AT THE EXECUTION OF THE SOFTWARE')
# print('This has been developed with Linux in mind, but it can be used changing the app path folder.')
# print('By the way using neovim to improve my touchtiping and code velosity.')
# print('The mouse has been touched only 2 times during the coding session.')
# print('Any keyboard has been damaged during the filming.')
print('All rights recerved Brezker.\n')
table()
showMenu()
