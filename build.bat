pyinstaller src/main.py
robocopy src/assets dist/main/assets /E
robocopy dist/main bin /E
@RD /S /Q "src/__pycache__"
@RD /S /Q "build"
@RD /S /Q "dist"
@RD /S /Q "main.spec"
del "main.spec"