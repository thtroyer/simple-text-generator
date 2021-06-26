# -*- mode: python ; coding: utf-8 -*-
spec_root = os.path.abspath(SPECPATH)
block_cipher = None

a = Analysis(['simple-text-generator-ui.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[
                ('templates/*', 'templates')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=["textgenrnn", "h5py", "numpy", "six", "scikit-learn", "joblib", "numpy", "scipy", "numpy", "threadpoolctl", "tensorflow", "absl-py", "six", "astunparse", "six", "wheel", "flatbuffers", "gast", "google-pasta", "six", "grpcio", "six", "h5py", "numpy", "six", "keras-preprocessing", "numpy", "six", "numpy", "opt-einsum", "numpy", "protobuf", "six", "six", "tensorboard", "absl-py", "six", "google-auth", "cachetools", "pyasn1-modules", "pyasn1", "rsa", "pyasn1", "setuptools", "six", "google-auth-oauthlib", "google-auth", "cachetools", "pyasn1-modules", "pyasn1", "rsa", "pyasn1", "setuptools", "six", "requests-oauthlib", "oauthlib", "requests", "certifi", "chardet", "idna", "urllib3", "grpcio", "six", "markdown", "numpy", "protobuf", "six", "requests", "certifi", "chardet", "idna", "urllib3", "setuptools", "tensorboard-data-server", "tensorboard-plugin-wit", "werkzeug", "wheel", "tensorflow-estimator", "termcolor", "typing-extensions", "wheel", "wrapt", "tqdm"],
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
          name='simple-text-generator-ui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
