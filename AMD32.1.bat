set APTIOV_X_TOOS=D:\BuildTools\Aptio_5.x_TOOLS_32.1
set COMPILERTOOLS=D:\BuildTools\WINDDK\7600.16385.1\bin\x86


set CCX86DIR=%COMPILERTOOLS%\x86
set CCX64DIR=%COMPILERTOOLS%\amd64
set TOOLS_DIR=%APTIOV_X_TOOS%\BuildTools

set PATH=%APTIOV_X_TOOS%\BuildTools;%COMPILERTOOLS%;%PATH%

START %APTIOV_X_TOOS%\VisualeBios\VisualeBios.exe
;fix thi bug1
