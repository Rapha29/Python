# meu_script.spec

# Módulos a serem incluídos
hiddenimports=['tkinter', 'pytube', 'moviepy', 'os', 're', 'webbrowser']

# Arquivo principal do seu script
a = Analysis(['baixar_editar.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='meu_script',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)