# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['../src/Polo.py'],
    pathex=['src'],
    binaries=[],
    datas=[('src/data', 'data'), ('src/astor', 'astor'), ('src/unrar', 'unrar'), ('src/templates', 'templates')],
    hiddenimports=['tensorflow', 'pptx'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

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
    icon=['macOS/application.icns'],
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
    icon='macOS/application.icns',
    bundle_identifier='edu.buffalo.hwi.polo',
)
