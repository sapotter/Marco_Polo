#!/bin/bash

# py2app borked on missing libpython3.7m.dylib. Even this fix worked
# but the build failed regardless.

# pyinstall is quite happy without it.

#POLO_ENV=/usr/local/Caskroom/miniconda/base/envs/polo
#
#if [ ! -e $POLO_ENV/lib/libpython3.7.a ]; then
#  pushd $POLO_ENV/lib && ln -s libpython3.7m.a libpython3.7.a && popd || exit 1;
#fi
#if [ ! -e $POLO_ENV/lib/libpython3.7.dylib ]; then
#  pushd $POLO_ENV/lib && ln -s libpython3.7m.dylib libpython3.7.dylib && popd || exit 1;
#fi

declare -i errors=0
if [ "$(basename "$(pwd)")" != "Marco_Polo" ]; then
    echo "ERROR: pyinstaller-macos.sh must be run in the Marco_Polo project root directory."
    _=$((errors++))
fi
if [ "${CONDA_DEFAULT_ENV:-notpolo}" = "notpolo" ]; then
    echo "ERROR: activate required conda environment with : conda activate polo"
    _=$((errors++))
fi
[ $((errors)) -gt 0 ] && exit 1
PYINSTALLER_INSTALLED=$(conda list -c pyinstaller | awk '/pypi\/pypi::pyinstaller-[[:digit:]]/ { print $0 }')
if [ "${PYINSTALLER_INSTALLED:-notinstalled}" = "notinstalled" ]; then
    echo "Install pyinstaller with: pip install pyinstaller"
    exit 1
fi

pyinstaller --collect-all tensorflow \
--hidden-import pptx \
--add-data ../src/data:data --add-data ../src/astor:astor \
--add-data ../src/unrar:unrar --add-data ../src/templates:templates \
--icon ../macOS/appplication.icns \
--clean \
-y \
--specpath macOS \
src/Polo.py
