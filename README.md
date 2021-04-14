# Setup
To run the program

Click the Download Code Button and click Download ZIP

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/download.PNG)

 
Extract the folder from the zip file
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/extract.PNG)

# Using Anaconda or Miniconda
### Using Anaconda
##### (If you have Anaconda already downloaded/installed you can skip this step)

Go to this link https://www.anaconda.com/products/individual#Downloads or search Anaconda in a internet browser and look for individual downloads.
Download the appropriate version for your operating system
(If you don't know what your OS is and you're not using a Mac, it's probably Windows)
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/anaconda.PNG)

 
Run the Anaconda install you just downloaded (you can usually just click next as the defaults should work for most users)

### Using Miniconda - for those that just want to use Anaconda for this

Go to this link https://docs.conda.io/en/latest/miniconda.html or search Miniconda in a internet browser.
Download the appropropriate verison for your operating system
(If you don't know what your operating system is and you're not using a Mac, it's probably Windows)

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

 
The year and sportCode should be the only variables you change in this file. If you want to scrape for a specific year and sport, delete the pound (#) sign in front of the year and the sport code and then save the file. If you don't want that year or sport, make sure there is a pound (#) sign in front of it so that it doesn't get scraped. 
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/list.PNG)
 
So in this example, we are scraping all the data from Women's Basketball for the 2020 season. The year and sportCode variables in the MySpider.py file should look like

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/edit.PNG)

Once you save the file, you can now just run the script.bat file and it should scrape automatically for you

*On Windows*

`script.bat`

Hit enter

If you screen starts to look similar to this, it means that the program is actively scraping the Ncaa's website and pulling the data. Look at the HTTP requests, (the circled numbers in the image below). You want it to contain numbers in the 200's and 300's. The 200's mean it succesfull connected to the webpage and the 300's are redirects, meaning the information wasn't at that specific page, but its getting sent to the correct one now. This program takes a while to run. We are scraping thousands of webpages automatically and have to delay the process slightly or risk getting our IP address temporarily suspended from the website. It takes roughly seven minutes to scrape one season for a single sport, so this process can take a while if you are trying to scrape twenty years of data for multiple sports. 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/work.PNG)

The program is done running when it looks similar to this

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/fin.PNG)

All the scraped data is located in the Scraped folder 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/scraped.PNG)

It contains schedule.csv, which contains the schedule information for the team during that season. Stats.csv contains the team stats for that team for the season (or up until that point if its mid-season). Then each teams player statistics is separate by sport. There is also a <Sport>TeamStats.csv that has the team stats for every season you scraped, sorted by sport

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/403.PNG)

You should move these files to a safe place on your computer or USB. You will have to rename or delete the Scraped folder if you want to run the program again as that is where the csv files will be stored or you risk the data being overwritten.

Lastly, if you don't plan on using this again in the near future, you can uninstall Anaconda or Miniconda (whichever you installed) and deleted the downloaded folders.

# Problems That Might Arise
#### 403 Errors

Scraping webpages is basically visiting multiple webpages faster than a human physically can. If it is done fast enough, it will look like a Denial of Service attack and the website will suspend the IP address or risk having their website crash.

If you are scraping to many pages or scraping them to fast your Anaconda Prompt might start to show 403 errors.

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/list.PNG)

If this does happen, your IP address probably has been suspended and you will need to wait for a while before you start scraping again. Before you try to scrape their data try changing the CONCURRENT_REQUESTS and DOWNLOAD_DELAY in the Ncaa/Ncaa/settings.py file. You can also open this file in Notepad.

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/defaultSettings.PNG)

By default CONCURRENT_REQUESTS is set to 2 and DOWNLOAD_DELAY is set to 0. CONCURRENT_REQUESTS is the number of webpages you are trying to scrape at the same time and DOWNLOAD_DELAY is how long the program waits before it tries to download the data. This is the fastest I could get it to go without getting suspended. 

But, if you are still getting 403 errors, then try setting CONCURRENT_REQUESTS to 1 and DOWNLOAD_DELAY to 5. 

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/modifiedSettings.PNG)

If you are still getting 403 errors, try scraping a fewer number of sports at one time, or fewer years. But these settings should work most of the time.

After you change your settings or the sports or years you are trying to scrape and have waited awhile, all you have to do is run 

`script.bat`

again and the program will start scraping again.

#### Pausing and Resuming a crawl

As of now, there isn't a way to pause the program as it is running, or at least while maintaining data integrity. So you'll have to do the scraping in one sitting. I recommend doing one sport at a time and moving the files to a separate place after each time you run it. 


