# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata

datas = [('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Camera.ico', '.')]
binaries = [('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\avutil-57.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\CLAllSerial_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\CLProtocol_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\CLSerCOM.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\CLSerHvc.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\CommonParameters.ini', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\D3DCompiler_43.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\d3dcompiler_47.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\d3dx9_43.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\FormatConversion.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\GCBase_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\GenApi_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\libmmd.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\libusb0.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\libwinpthread-1.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\log4cpp_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\Log_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MathParser_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MediaProcess.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\Microsoft.VC90.CRT.manifest', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\Microsoft.VC90.DebugCRT.manifest', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcm90.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcp120.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcp90.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcr100.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcr120.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\msvcr90.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvCameraControl.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvCameraControlGUI.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvCameraControlWrapper.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvCameraPatch.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvCamLVision.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvDSS.ax', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvDSS2.ax', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MVFGControl.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvFGProducerCML.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvFGProducerCXP.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvFGProducerGEV.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvFGProducerXoF.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MVGigEVisionSDK.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvISPControl.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MVMemAlloc.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvProducerGEV.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvProducerU3V.cti', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvProducerVIR.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvRender.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvSDKVersion.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvSerial.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvSerialCtrl.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\MvUsb3vTL.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\NodeMapData_MD_VC120_v3_0_MV.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\pthreadGC2.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\pthreadVC2.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\SuperRender.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\svml_dispmd.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\swscale-6.dll', 'Win64_x64'), ('D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Win64_x64\\XmlParser_MD_VC120_v3_0_MV.dll', 'Win64_x64')]
hiddenimports = ['onnxruntime', 'cv2', 'numpy', 'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'MvCameraControl_class', 'CameraParams_const', 'CameraParams_header', 'MvErrorDefine_const', 'PixelType_header']
datas += copy_metadata('onnxruntime')
datas += copy_metadata('opencv-python')
datas += copy_metadata('numpy')
datas += copy_metadata('PyQt5')
tmp_ret = collect_all('PyQt5')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('cv2')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('onnxruntime')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Camera_entry.py'],
    pathex=[],
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
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Camera',
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
    icon=['D:\\Desktop\\2Camera+2USB+2HIK+2YOLO+Modbus\\Camera.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Camera',
)
