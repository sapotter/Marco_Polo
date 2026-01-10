# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import collect_all

cur_dir = Path().resolve()
print('Current directory: ', cur_dir)
src_dir = cur_dir.joinpath('src')

block_cipher = None

datas = [
    (src_dir.joinpath('data'), 'data'),
    (src_dir.joinpath('astor'), 'astor'),
    (src_dir.joinpath('unrar'), 'unrar'),
    (src_dir.joinpath('templates'), 'templates'),
]

binaries = []
hiddenimports = []

tmp_ret = collect_all('tensorflow')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

tmp_ret = collect_all('pptx')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

a = Analysis(
    [src_dir.joinpath('Polo.py')],
    pathex=[src_dir],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
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
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Polo',
)

app = BUNDLE(
    coll,
    name='Polo.app',
    icon=cur_dir.joinpath('macOS/application.icns'),
    bundle_identifier='org.hauptman-woodward.polo',
)
