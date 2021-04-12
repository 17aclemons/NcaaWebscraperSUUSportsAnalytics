# Setup
To run the program

Click the Download Code Button and select download zip

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/download.PNG)

 
Extract the folder from the zip file
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/extract.PNG)

# Using Anaconda or Miniconda
### Using Anaconda
##### (If you have Anaconda already downloaded you can skip this step)

Go to this link https://www.anaconda.com/products/individual#Downloads or search Anaconda in a internet browser and look for individual downloads.
Download the appropriate version for your operating system
(If you don't know what your OS is and your not using a Mac, its probably windows)
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/anaconda.PNG)

 
Run the Anaconda install you just downloaded (you can usually just click next as the defaults should work for most users)

### Using Miniconda - for those that just Anaconda for this

Go to this link https://docs.conda.io/en/latest/miniconda.html or search Miniconda in a internet brwoser.
Download the appropropriate verison for your operating system
(If you don't know what your operating system is and your not using a Mac, it's probably Windows)

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/miniconda.PNG)

 
Run the Miniconda install you just downloaded (you can usually just click next as the defaults should work for most users)

## Completing Install
If you get the screen below, you've successfully installed Anaconda/Miniconda. You can uncheck the two boxes on the screen and click on finish to finish the install

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/miniInstall.PNG)

 
Open the Anaconda Prompt (you can type ananconda into the search bar and it should be there)
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/anacondaPrompt.PNG)

Navigate to NcaaWebscraperSUUSportsAnalytics-main folder

*The code below will work for most Windows Machines*

`cd Downloads\NcaaWebscraperSUUSportsAnalytics-main`

Type  
`conda env create -f environment.yml`

To create a new conda environment. 
Conda environments are like python virtual environments and are used so that package versions don't conflict with each other. If you use python this is considered best practice.

Activate the environment using 

`conda activate Webscraper`

Now that you have the conda environment setup, you need to select what sports and year that you want to scrape for. Open up a File Explorer and navigate to the MySpider.py file in Ncaa\Ncaa\spiders\MySpider.py and open it up with any text editor or python editor you have. (Notepad, Notepad++ will work). 
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/open.PNG)

 
The year and sportCode should be the only variables you change in this file. If you want to scrape for a specific year and sport, delete the pound (#) sign in front of the year and the sport code and then save the file.
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/list.PNG)
 
So in this example, we are scraping all the data from Women's Basketball for the 2002 season. The year and sportCode variables in the MySpider.py file should look like

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/edit.PNG)

Once you save the file, you can now just run the script.bat file and it should scrape automatically for you

*On Windows*

`script.bat`

hit enter

If you screen starts to look similar to this, it means that the program is activilty scraping the Ncaa's website and pulling the data. Look at the HTTP requests, (the circled numbers in the image below). You want it to contain numbers in the 200's and 300's. The 200's mean it succesfull reconnected to the webpage and the 300's are redirects, meaning the information wasn't at that specific page, but its getting sent to the correct one now. This program takes a while to run. We are scraping thousands of webpages automatically and have to delay the process slightly or risk getting our IP address temporarily banned from the website. It takes roughly seven minutes to scrape one season for a single sport, so this process can take a while if you are trying to scrape twenty years of data for multiple sports. 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/work.PNG)

The program is done running when it looks similar to this

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/fin.PNG)

All the scraped data is located in the Scraped folder 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/scraped.PNG)

It contains schedule.csv, which contains the schedule information for the team during that season. Stats.csv contains the team stats for that team for the season (or up until that point if its mid-season). Then each teams player statistics is separate by sport. 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/csv.PNG)

# Problems That Might Arise
