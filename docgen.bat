@echo off
echo generating docs
pdoc3 --html --config show_source_code=False -o ./docs ./src/cormen_lib --force
echo moving up docs
copy docs\cormen_lib\* docs\
echo removing duplicates
rmdir /q /s docs\cormen_lib
pause