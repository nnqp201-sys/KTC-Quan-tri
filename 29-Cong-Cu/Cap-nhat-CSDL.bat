@echo off
chcp 65001 >nul
rem Ghi CSDL theo doi nhiem vu tu tep CSV moi nhat do skill ktc-ioffice (Claude in Chrome) xuat ra.
rem Bam dup tep nay. Them tham so --thu de chay thu: Cap-nhat-CSDL.bat --thu
set "DL=%USERPROFILE%\Downloads"
set "CSV="
for /f "delims=" %%f in ('dir /b /o-d "%DL%\ioffice-quet_*.csv" 2^>nul') do if not defined CSV set "CSV=%%f"
if not defined CSV (
  echo Khong thay tep ioffice-quet_*.csv trong %DL%. Chay skill ktc-ioffice trong Chrome truoc.
  pause & exit /b 1
)
echo Tep dau vao: %CSV%
echo Hay DONG tep CSDL trong Excel truoc khi tiep tuc.
pause
python "%~dp0cap_nhat_csdl.py" %1 "%DL%\%CSV%" --nhan-file "%DL%"
echo.
echo Buoc tiep: trich nhiem vu chi tiet bang skill ktc-trich-nhiem-vu (Claude Code tren may).
pause
