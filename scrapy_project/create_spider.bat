
@echo off

cd\

F:

cd "GitExtensions_python\project_spider\scrapy_project\ASMR"

python -m scrapy genspider asmr "asmrv.com"

@cmd.exe

pause

