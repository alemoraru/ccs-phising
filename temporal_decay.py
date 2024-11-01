import pandas as pd
import matplotlib.pyplot as plt
import argparse
from typing import Optional


def time_window_to_string(time_window: str) -> str:
    """
    Converts a time window string to a string that can be used as an index in a DataFrame.
    For example, 'W' becomes 'Week', 'ME' becomes 'Month', and 'D' becomes 'Day'.

    :param time_window: The time window string to convert
    :return: The string representation of the time window
    """
    if time_window == 'W':
        return 'Week'
    elif time_window == 'ME':
        return 'Month'
    elif time_window == 'D':
        return 'Day'
    else:
        return 'Invalid'
    
def years_back_to_string(years_back: Optional[int]) -> str:
    """
    Converts a number of years back to a string representation that can be used in a title.
    For example, 1 becomes '1 Year', 2 becomes '2 Years', and so on.

    :param years_back: The number of years back
    :return: The string representation of the number of years back
    """
    if years_back is None:
        return ''
    else:
        return ' over ' + (f'for {years_back} year' if years_back == 1 else f'{years_back} years')

def temporal_decay(file: str, time_window: str, years_back: Optional[int]=None) -> None:
    """
    Given a dataset containing online verified phishing submissions, this function
    will plot the number of submissions over time to illustrate how the more we look back
    in time, the fewer submissions we find, due to the fact that phishing URLs are taken down
    relatively quickly.

    The dataset is a json array containing the following fields:
    - phish_id: The unique identifier of the phishing submission
    - url: The URL that was submitted
    - phish_detail_url: The URL that shows the details of the phishing submission (on PhishTank)
    - submission_time: The time when the phishing submission was made
    - verified: Whether the phishing submission was verified or not
    - verification_time: The time when the phishing submission was verified
    - online: Whether the phishing submission was online or not
    - target: The target of the phishing submission (i.e. the company being impersonated)
    - details: The details of the phishing submission which is an array that contains the following fields:
        - ip_address: The IP address of the phishing site
        - cidr_block: The CIDR block of the IP address
        - announcing_network: The network announcing the IP address
        - rir: The Regional Internet Registry of the IP address
        - country: The country where the phishing site is hosted
        - detail_time: The time when the details were recorded

    :param file: The file to read the phishing submissions from
    :param time_window: The time window to resample the data by (e.g., 'W' for weekly, 'ME' for monthly, 'D' for daily)
    :param years_back: The number of years to look back in time
    """

    # Load the phishing submissions from the file
    df = pd.read_json(file)

    # Convert 'submission_time' to datetime if not already
    df['submission_time'] = pd.to_datetime(df['submission_time'], errors='coerce')

    # Drop rows with missing or invalid submission times
    df = df.dropna(subset=['submission_time'])

    # Filter to include only data from the last x years if specified
    if years_back is not None:
        # Get the current time with the same timezone as 'submission_time'
        current_time = pd.Timestamp.now(tz='UTC')
        x_years_ago = current_time - pd.DateOffset(years=years_back)
        
        # Ensure 'submission_time' is in datetime format with the same timezone
        df['submission_time'] = pd.to_datetime(df['submission_time']).dt.tz_convert('UTC')
        
        # Filter the DataFrame
        df = df[df['submission_time'] >= x_years_ago]

    # Set the index to 'submission_time' for easier resampling
    df.set_index('submission_time', inplace=True)

    # Resample data by chosen time window (you can also choose 'W' for weekly, 'D' for daily, etc.)
    if (time_window not in ['W', 'ME', 'D']):
        print('Invalid time window. Please choose a valid time window (e.g., W, ME, D)')
        return
    
    time_window_submissions = df.resample(time_window).size()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(time_window_submissions.index, time_window_submissions.values, label='Phishing Submissions Over Time')
    
    # Add titles and labels
    plt.title(f'Phishing Submissions Over Time (Temporal Decay{years_back_to_string(years_back)}) Indexed by {time_window_to_string(time_window)}')
    plt.ylabel('Number of Valid Online Submissions', fontsize=10)
    
    # Show grid for better readability
    plt.grid(True)
    
    # Display the plot
    plt.tight_layout()
    plt.show()
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='temporal_decay.py',
        description='See how the number of phishing submissions decay over time'
    )

    # Define the allowed script parameters
    parser.add_argument(
        "-f", "--file", type=str, help="Enter the file to read the phishing submissions from", required=True
    )
    parser.add_argument(
        "-t", "--time_window", type=str, help="Enter the time window to resample the data by (e.g., 'W' for weekly, 'ME' for monthly, 'D' for daily)", required=True
    )
    parser.add_argument(
        "-y", "--years_back", type=int, help="Enter the number of years to look back in time (default looks at all data)", required=False
    )

    # Parse the arguments
    args = parser.parse_args()

    temporal_decay(args.file, args.time_window, args.years_back)
