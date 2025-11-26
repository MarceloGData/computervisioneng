@echo off
REM Delete all .git folders in subdirectories, except the current directory

for /d /r %%G in (.git) do (
    REM %%~dpG is the path of the found .git folder, with trailing backslash
    REM Compare with "%CD%\.git\"
    if /I not "%%~fG"=="%CD%\.git" (
        if exist "%%G" (
            echo Deleting "%%G"
            rmdir /s /q "%%G"
        )
    )
)
echo All .git folders (except current directory) deleted.
