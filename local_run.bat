@echo off
setlocal
set PYTHONPATH=%~dp0
REM shift will not work with %*
IF "%PYTHON%" == "" set PYTHON=py
WHERE %PYTHON% >nul 2>&1
IF %ERRORLEVEL% NEQ 0 set PYTHON=
IF "%1" == "-3" (
  if "%PYTHON%" == "py" (
    set "PYTHON=py -3"
  ) else (
    set PYTHON=python3
  )
) else (
  IF "%PYTHON%" == "" set PYTHON=python3
  WHERE %PYTHON% >nul 2>&1
  IF %ERRORLEVEL% NEQ 0 set PYTHON=python
)
%PYTHON% main.py
title ExsNetworkScan
PAUSE