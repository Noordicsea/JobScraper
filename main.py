import requests
import os
import json
from bs4 import BeautifulSoup

BASE_URL = "https://willrobotstakemyjob.com"

def scrape_directory(url):
    json_filename = "directory.json"
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as f:
            return json.load(f)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_divs = soup.find_all('div', style=lambda value: value and 'margin-bottom:10px' in value)
    categories = []
    for cat_div in categories_divs:
        anchor = cat_div.find('a')
        if anchor:
            category_text = anchor.get_text(strip=True)
            category_link = anchor.get('href')
            categories.append((category_text, category_link))
    with open(json_filename, 'w') as f:
        json.dump(categories, f)
    return categories
    json_filename = "directory.json"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_divs = soup.find_all('div', style=lambda value: value and 'margin-bottom:10px' in value)
    categories = []
    for cat_div in categories_divs:
        anchor = cat_div.find('a')
        if anchor:
            category_text = anchor.get_text(strip=True)
            category_link = anchor.get('href')
            categories.append((category_text, category_link))
    # Save to JSON file
    with open(json_filename, 'w') as f:
        json.dump(categories, f)
    return categories
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_divs = soup.find_all('div', style=lambda value: value and 'margin-bottom:10px' in value)
    categories = []
    for cat_div in categories_divs:
        anchor = cat_div.find('a')
        if anchor:
            category_text = anchor.get_text(strip=True)
            category_link = anchor.get('href')
            categories.append((category_text, category_link))
    return categories

def scrape_job_categories(category_url_end):
    json_filename = f"{category_url_end.split('/')[-1]}.json"
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as f:
            return json.load(f)
    full_url = BASE_URL + category_url_end
    response = requests.get(full_url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {full_url}, status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    main_title = soup.find('h1').text.strip()
    sub_categories = []
    current_h2 = None
    current_sub_category = []
    for element in soup.find_all(['h2', 'h3', 'div']):
        if element.name == 'h2':
            if current_h2 is not None:
                sub_categories.append((current_h2, current_sub_category))
                current_sub_category = []
            current_h2 = element.get_text(strip=True)
        elif element.name == 'div' and 'margin-left:20px' in element.get('style', ''):
            anchor = element.find('a')
            if anchor:
                job_link = anchor.get('href')
                job_name = anchor.get_text(strip=True)
                job_url = BASE_URL + job_link
                job_details = get_job_details(job_url)
                risk_percentage, polling_percentage, number_of_votes, growth_percentage, wages, volume = job_details
                current_sub_category.append((job_name, job_link, risk_percentage, polling_percentage, number_of_votes, growth_percentage, wages, volume))
    if current_h2 is not None:
        sub_categories.append((current_h2, current_sub_category))
    with open(json_filename, 'w') as f:
        json.dump((main_title, sub_categories), f)
    return main_title, sub_categories

def get_job_details(job_url):
    response = requests.get(job_url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {job_url}, status code: {response.status_code}")
        return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
    job_soup = BeautifulSoup(response.text, 'html.parser')
    # Get risk percentage
    risk_div = job_soup.find('div', style=lambda value: value and 'font-size: 30px;font-weight:700' in value)
    risk_percentage = risk_div.get_text(strip=True) if risk_div else "N/A"
    # Get polling information
    polling_div = job_soup.find('div', id='PanelPolling')
    polling_percentage = "N/A"
    number_of_votes = "N/A"
    if polling_div:
        percentage_div = polling_div.find('div', style=lambda value: value and 'font-size: 30px;font-weight:700' in value)
        votes_div = polling_div.find('div', style=lambda value: value and 'font-size:15px;font-weight:300' in value)
        polling_percentage = percentage_div.get_text(strip=True) if percentage_div else "N/A"
        number_of_votes = votes_div.get_text(strip=True) if votes_div else "N/A"
    # Get the 'GROWTH' information
    growth_panel = job_soup.find('div', id='PanelGrowth')
    growth_percentage = "N/A"
    if growth_panel:
        growth_value_div = growth_panel.find('div', style=lambda value: value and 'font-size: 30px;font-weight:700' in value)
        if growth_value_div:
            growth_percentage = growth_value_div.get_text(strip=True)
    # Get the 'WAGES' information
    wages_panel = job_soup.find('div', id='PanelWages')
    wages = "N/A"
    if wages_panel:
        wages_div = wages_panel.find('div', style=lambda value: value and 'font-size:30px;font-weight:700' in value)
        if wages_div:
            wages = wages_div.get_text(strip=True)
    # Get the 'Volume' information
    volume_panel = job_soup.find('div', id='PanelVolume')
    volume = "N/A"
    if volume_panel:
        volume_div = volume_panel.find('div', style=lambda value: value and 'font-size:30px;font-weight:700' in value)
        if volume_div:
            volume = volume_div.get_text(strip=True)
    return risk_percentage, polling_percentage, number_of_votes, growth_percentage, wages, volume

def display_directory(categories):
    for i, (category_text, _) in enumerate(categories, 1):
        print(f"{i}. {category_text}")

def display_scraped_data(main_title, sub_categories, console_width):
    print(main_title)
    for sub_cat_name, jobs in sub_categories:
        print(f"\n{sub_cat_name}:")
        for job_tuple in jobs:
            # Unpack the job details
            job_name, _, risk_percentage, polling_percentage, number_of_votes, growth, wages, volume = job_tuple
            # Prepare the information to display
            display_text = (
                f"{job_name}\n"
                f"- Risk: {risk_percentage}\n"
                f"- Polling: {polling_percentage} ({number_of_votes})\n"
                f"- Growth: {growth}\n"
                f"- Wages: {wages}\n"
                f"- Volume: {volume}\n"
            )
            print(display_text)

def main():
    while True:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        # Scrape directory first
        url_to_scrape = 'https://willrobotstakemyjob.com/directory'
        occupation_categories = scrape_directory(url_to_scrape)
        # Display the directory
        display_directory(occupation_categories)
        # Get user input
        choice = input("\nChoose a category number to view its sub-categories and links, or 'exit' to quit: ")
        # Check if the user wants to exit
        if choice.strip().lower() == 'exit':
            break
        # Validate the user's choice
        if not choice.isdigit() or not (0 < int(choice) <= len(occupation_categories)):
            print("Invalid choice!")
            input("Press Enter to continue...")
            continue
        choice = int(choice) - 1
        # Retrieve and display the selected category's data
        _, category_link = occupation_categories[choice]
        main_title, sub_categories = scrape_job_categories(category_link)
        # Get the width of the console to align the risk percentages properly
        console_width = os.get_terminal_size().columns
        display_scraped_data(main_title, sub_categories, console_width)
        input("\nPress Enter to return to the main directory or type 'exit' to quit.")  # Wait for user action
    while True:
        # CLear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        # Scrape directory first
        url_to_scrape = 'https://willrobotstakemyjob.com/directory'
        occupation_categories = scrape_directory(url_to_scrape)
        # Display the directory
        display_directory(occupation_categories)
        # Get user input
        choice = input("\nChoose a category number to view its sub-categories and links, or 'exit' to quit: ")
        # Check if the user wants to exit
        if choice.strip().lower() == 'exit':
            break
        # Validate the user's choice
        if not choice.isdigit() or not (0 < int(choice) <= len(occupation_categories)):
            print("Invalid choice!")
            input("Press Enter to continue...")
            continue
        choice = int(choice) - 1
        # Retrieve and display the selected category's data
        _, category_link = occupation_categories[choice]
        main_title, sub_categories = scrape_job_categories(category_link)
        # Get the width of the console to align the risk percentages properly
        console_width = os.get_terminal_size().columns
        display_scraped_data(main_title, sub_categories, console_width)

        input("\nPress Enter to return to the main directory or type 'exit' to quit.")  # Wait for user action

if __name__ == "__main__":
    main()
