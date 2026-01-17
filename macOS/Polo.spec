# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import sysconfig
from pathlib import Path

from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis

cur_dir = Path().resolve()
print('Current directory: ', cur_dir)
src_dir = cur_dir.joinpath('src')

python_major, python_minor, *dummy = sys.version_info
env_name = os.environ.get('CONDA_DEFAULT_ENV')
print('env_name:', env_name)
site_packages = sysconfig.get_paths()['purelib']
print('site-packages:', site_packages)

datas = [
    (src_dir.joinpath('data'), 'data'),
    (src_dir.joinpath('astor'), 'astor'),
    (src_dir.joinpath('unrar'), 'unrar'),
    (src_dir.joinpath('templates'), 'templates'),
]

block_cipher = None

a = Analysis(
    [src_dir.joinpath('Polo.py')],
    pathex=[src_dir],
    binaries=[],
    datas=datas,
    hiddenimports=['tensorflow', 'pptx'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
    optimize=0,  # Default level: no optimization, __debug__ constant is True, assert statements are active
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# For a macOS bundle created in onedir mode (the default for an app bundle), exclude_binaries=True is generally
# required in the EXE object of your PyInstaller spec file. This is because the binaries are collected by the
# COLLECT object instead.
#
# If you are creating a onefile bundle, exclude_binaries=False (or omitting the argument, as False is the default)
# should be used.

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # True is required for a macOS bundle app
    name='Polo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[cur_dir.joinpath('macOS/application.icns')],
)

coll = COLLECT(
    exe,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Polo',
)

app = BUNDLE(
    coll,
    name='Polo.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        # Add other Info.plist entries as a Python dict here
        'CFBundleDisplayName': 'Polo',
        'CFBundleName': 'Polo',
        'CFBundlePackageType': 'APPL',
        'CFBundleShortVersionString': '0.2.1.1',
        'CFBundleVersion': '0.2.1.1',
        'NSHumanReadableCopyright': 'Copyright (c) 2025, University At Buffalo - Hauptman-Woodward Research Institute. All rights reserved.',
    },
    icon=cur_dir.joinpath('macOS/application.icns'),
    bundle_identifier='edu.buffalo.hwi.polo',
)
