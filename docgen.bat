@echo off
echo generating docs
pdoc3 --html --config show_source_code=False -o ./docs ./src/dalpy --force
echo moving up docs
copy docs\dalpy\* docs\
echo removing duplicates
rmdir /q /s docs\dalpy
pause