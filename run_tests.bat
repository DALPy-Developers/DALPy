@echo off
@echo running tests
for %%i in (tests/*.py) do start "" /b /wait python "tests/%%i"
pause