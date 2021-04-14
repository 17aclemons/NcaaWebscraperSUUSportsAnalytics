cd Ncaa
scrapy crawl ncaa -O data.json
py sortAndWrite.py
del /f data.json
cd ..