conda env create -f environment.yml
conda activate Webscraper
cd Ncaa
scrapy crawl ncaa -O data.json
py sortAndWrite.py

