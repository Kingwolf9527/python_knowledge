@echo off

cd\

F:

cd "GitExtensions_python\project_spider\scrapy_project\Biquyun"

python -m scrapy genspider -t crawl biquyun_spider "biquyun.com/"

@cmd.exe

pause