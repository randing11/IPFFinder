# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect data files and submodules for xgboost
datas = collect_data_files('xgboost')
hiddenimports = collect_submodules('xgboost')


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[
        ('C:\\Users\\admin\\Desktop\\mfe\\mfe_venv_09\\Lib\\site-packages\\xgboost\\lib\\xgboost.dll', 'lib'),
        ('C:\\Users\\admin\\Desktop\\mfe\\mfe_venv_09\\Lib\\site-packages\\xgboost\\VERSION', 'xgboost'),
    ],
    datas=[
        ('static/simhei.ttf', 'static'),
        ('./data/model_data.csv', 'data'),
        ('./data/protein_models.pkl', 'data'),
    ],
    hiddenimports=hiddenimports+['win32timezone'],
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
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
