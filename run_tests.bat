:: Batch script for running tests on DALPy. Best to run in command line with ./run_tests.bat
@echo off
@echo running tests
for %%i in (tests/*.py) do (
    echo **** %%i ****
    echo:
    start "" /b /wait python "tests/%%i"
)