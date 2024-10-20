from random import randint

import requests
import csv
import time

# Constants for the API
API_KEY = "#"  # Replace with your API key
BASE_URL = "https://api.aa419.org/fakesites"
HEADERS = {
    "Auth-API-Id": API_KEY
}
PAGE_SIZE = 500  # Number of results per page
TOTAL_PAGES = 3500  # Total number of pages to query

# CSV file to store the results
CSV_FILE = 'resources/aa419_dataset.csv'


# Function to save the data to CSV
def save_to_csv(data, file_name):
    # Get the headers from the data keys on the first call
    keys = data[0].keys()

    # Check if the file exists or not (append or write header)
    file_exists = False
    try:
        with open(file_name, 'r', newline='') as f:
            file_exists = True
    except FileNotFoundError:
        pass

    # Write to CSV file
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        if not file_exists:
            writer.writeheader()  # Write header only once
        writer.writerows(data)


# Main function to query the API and save results
def query_spamhaus():
    STOPPED = 336
    for page_number in range(STOPPED, TOTAL_PAGES + 1):
        print(f"Fetching page {page_number}...")
        params = {
            "pgno": page_number,
            "pgsize": PAGE_SIZE,
            "orderby": "DateAdded"
        }

        try:
            response = requests.get(BASE_URL, headers=HEADERS, params=params)
            print(response.url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()

            if data:
                save_to_csv(data, CSV_FILE)
                print(f"Page {page_number} data saved.")
            else:
                print(f"No data on page {page_number}. Stopping early.")
                break  # Stop if there is no data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_number}: {e}")

        # Add a small delay to avoid rate-limiting issues (random between 1 and 5 seconds)
        time.sleep(randint(1, 5))


if __name__ == "__main__":
    query_spamhaus()