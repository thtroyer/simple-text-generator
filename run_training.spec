# -*- mode: python ; coding: utf-8 -*-


spec_root = os.path.abspath(SPECPATH)
block_cipher = None


a = Analysis(['run_training.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=["pyinstaller_hooks"],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          exclude_binaries=False,
          name='run_training',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

# uncomment to build into dir
#coll = COLLECT(exe,
               #a.binaries,
               #a.zipfiles,
               #a.datas,
               #strip=False,
               #upx=True,
               #upx_exclude=[],
               #name='run_training')
