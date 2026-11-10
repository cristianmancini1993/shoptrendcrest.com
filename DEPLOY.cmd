@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

echo.
echo === homeshopspot.com — деплой на сервер ===
echo.

set TAR=%TEMP%\hss.tar
echo [1/3] Собираю архив...
tar -cf "%TAR%" --exclude=.git --exclude=scripts/__pycache__ .
if errorlevel 1 (
  echo ОШИБКА: tar не смог собрать архив.
  pause
  exit /b 1
)
echo OK: %TAR%
echo.

echo [2/3] Загрузка на сервер (введи пароль root ОДИН раз):
scp "%TAR%" root@179.198.201.118:/tmp/hss.tar
if errorlevel 1 (
  echo ОШИБКА загрузки.
  pause
  exit /b 1
)
echo.

echo [3/3] Распаковка на сайте (пароль root ещё раз):
ssh root@179.198.201.118 "cd /var/www/homeshopspot.com && tar -xf /tmp/hss.tar && grep -q 'Meta Pixel' index.html && echo DEPLOY OK"
if errorlevel 1 (
  echo ОШИБКА на сервере.
  pause
  exit /b 1
)

echo.
echo Готово. Проверь: https://homeshopspot.com/it/leafora/landing.html
echo.
pause
