@echo off
pyinstaller --onefile --windowed --icon="icon.ico" --add-data "icon.ico;." --add-data "rbbx.png;." gui_tester.pyw

