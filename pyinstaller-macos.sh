#!/bin/bash

 pyinstaller --collect-all tensorflow \
 --hidden-import pptx \
 --add-data src/data:data --add-data src/astor:astor \
 --add-data src/unrar:unrar --add-data src/templates:templates \
 --icon ~/Marco_Polo/icon.icns \
 --clean \
 -y \
 --name polox src/Polo.py