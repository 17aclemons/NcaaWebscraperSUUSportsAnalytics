# Setup
To run the program

Click the Download Code Button and select download zip

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/download.PNG)


Extract the folder from the zip file
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/extract.PNG)

# Using Anaconda or Miniconda
### Using Anaconda
##### (If you have anaconda already downloaded you can skip this step)

Go to this link https://www.anaconda.com/products/individual#Downloads or search Anaconda in a internet browser and look for individual downloads.
Download the appropriate version for your operating system
(If you don't know what your OS is and your not using a mac, its probably windows)
![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/anaconda.PNG)

Run the Anaconda install you just downloaded (you can usually just click next as the defaults should work for most users)

### Using Miniconda - for those that just Anaconda for this

Go to this link https://docs.conda.io/en/latest/miniconda.html or search Miniconda in a internet brwoser.
Download the appropropriate verison for your operating system
(If you don't know what your operating system is and your not using a Mac, it's probably Windows)

![Image](https://github.com/17aclemons/NcaaWebscraperSUUSportsAnalytics/blob/main/images/miniconda.PNG)

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
Now navigate to the Ncaa folder and run script.bat
*On Windows*
`cd Ncaa`
`script.bat`
hit enter
