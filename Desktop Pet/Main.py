import subprocess
import sys

def install_package(package_name):
    print(f"Installing {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(f"{package_name} installed!")
try:
    import pygame
except ImportError:
    install_package('pygame')
    import pygame
try:
    import win32gui
except ImportError:
    install_package('pywin32')
import win32gui
import win32con
import ctypes
import threading
import time
import os
import random
MAINDIR = os.path.dirname(__file__)
WINDOW = pygame.display.set_mode((400,700))



script_path = os.path.join(MAINDIR,"Pet.py")

try:
    subprocess.run(['python', script_path], check=True)
    print(f"Successfully ran {script_path}")
except subprocess.CalledProcessError as e:
    print(f"Error running {script_path}: {e}")
except FileNotFoundError:
    print(f"Error: Python interpreter or the file '{script_path}' was not found.")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()

            
