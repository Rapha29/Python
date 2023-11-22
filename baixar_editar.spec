# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['d:/Repositorio/Python/YoutubeTools/baixar_editar.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tkinter', 'pytube', 'moviepy', 'os', 're', 'webbrowser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='baixar_editar',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
