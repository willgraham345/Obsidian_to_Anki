@echo off
setlocal

:: Ask the user if they are at work
set /p atWork="Are you at work? (Y/N): "

:: Define source and destination paths
set "source=%CD%"
set "dest1=%CD%\..\Will_projects"
set "dest2=%CD%\..\SpaceDynamicsLab"

:: Confirm action
echo This script will copy:
echo - .obsidian
echo - zz_Templates
echo From: %source%
echo To: %dest1%
if /I "%atWork%"=="Y" echo And also to: %dest2%
set /p confirm="Proceed? (Y/N): "

if /I NOT "%confirm%"=="Y" (
    echo Operation canceled.
    exit /b
)

:: Copy folders to Work
xcopy "%source%\.obsidian" "%dest1%\.obsidian" /E /I /Y
xcopy "%source%\zz_Templates" "%dest1%\zz_Templates" /E /I /Y
echo Files copied to Work.

:: Copy folders to SpaceDynamicsLab only if at work
if /I "%atWork%"=="Y" (
    xcopy "%source%\.obsidian" "%dest2%\.obsidian" /E /I /Y
    xcopy "%source%\zz_Templates" "%dest2%\zz_Templates" /E /I /Y
    echo Files copied to SpaceDynamicsLab.
)

echo Copy operation complete!
pause
