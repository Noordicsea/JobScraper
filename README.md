# JobScraper
This script is a Python-based scraper used for collecting data on various job categories and their potential of being automated in the future. 

The data is scraped from "https://willrobotstakemyjob.com".

Features

    Scrapes job categories and individual job data, including risk of automation percentages, growth prospects, wages, volume, and public opinion (polling).
    Stores the scraped data in JSON files for offline access and analysis.
    Interactive console application to browse through job categories and view detailed information about each job.

Requirements

    Python 3.6 or higher
    Libraries: requests, beautifulsoup4, and json (these can be installed using pip, see below)

Installation

First, clone the repository or download the script. Then, install the necessary Python packages using pip. Navigate to the directory where you've cloned the repository or saved the script and use the following command:

bash

pip install -r requirements.txt

Note: You can manually install the dependencies by running: pip install requests beautifulsoup4.

Usage

To execute the script, navigate to its directory in the command-line interface and run (go to the folder you cloned this to, delete the path at the top, type cmd, press enter then tpye):

python main.py

After launching the script, it will scrape the directory of job categories from the source website and display them. You can then interact with the script as follows:

    Choose a category number to view its sub-categories and job details.
    View detailed information about each job, including automation risk, growth, wages, and more.
    Return to the main directory by pressing Enter or exit the script by typing 'exit'.

Important:

    The script checks for the existence of JSON files corresponding to the directory and individual categories. If these files exist, the script loads data from them instead of re-scraping the website, allowing for quicker access and reduced unnecessary network requests. If you want to refresh the data, you can delete the existing JSON files.
    The script handles network errors and scraping issues by providing error messages and failsafes to ensure a smooth user experience.

Customization

You can modify or extend the script by editing the main.py file. Possible customizations include changing the source URL, adjusting the data points to scrape, or transforming the script into a more comprehensive application or data service.

Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

License
Distributed under the MIT License. See LICENSE for more information.

Acknowledgements:
This script is not affiliated with "https://willrobotstakemyjob.com" and was created for educational purposes. Please use responsibly and ethically.
