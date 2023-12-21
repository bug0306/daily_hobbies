# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run.py','tree.py'],
    pathex=['D:\\codefiles\\vscode\\pythons\\chrismas\\1-christmas-wishing-project-python'],
    binaries=[],
    datas=[('images\\christmas.ico','images'),
            ('bells\\bell*.gif','bells'),
            ('santas\\santa*.gif','santas'),
            ('system-files\\cur_sonud.mp3','system-files'),
            ('system-files\\finish-sound.mp3','system-files'),
            ('wishes\\wish*.gif','wishes'),
            ('text\\wish.txt','text'),],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='christmasTree',
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
    icon='D:\\codefiles\\vscode\\pythons\\chrismas\\1-christmas-wishing-project-python\\images\\christmas.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
