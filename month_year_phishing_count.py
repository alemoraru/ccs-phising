import pandas as pd
import matplotlib.pyplot as plt
import argparse


def count_phishing_submissions_by_month_year(year: int, file: str) -> None:
    """
    Given a dataset of times when phishing submissions were made, this function counts
    the number of occurrences of phishing submissions for each month of a given year
    and plots the results as a bar chart.

    :param year: The year to count the number of phishing submissions for
    :param file: The file to read the phishing submissions from
    :return: None
    """

    # Load the date entries from the file
    with open(file, 'r') as file:
        date_list = file.read().splitlines()

    # Convert the list of date strings to a pandas DataFrame
    df = pd.DataFrame(date_list, columns=['submission_time'])

    # Convert 'submission_time' column to datetime format
    df['submission_time'] = pd.to_datetime(df['submission_time'])

    # Filter data for a specific year (e.g., 2024)
    df_filtered = df[df['submission_time'].dt.year == year]

    # Group by month and count the number of entries per month within that year
    monthly_counts = df_filtered.groupby(df_filtered['submission_time'].dt.month).size()

    # Plot the results
    plt.figure(figsize=(10, 6))
    monthly_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Number of Online Verified Phishing Entries per Month in {year}')
    plt.xlabel('Month Number')
    plt.ylabel('Number of Online Verified Phishing Reports')
    plt.xticks(rotation=0)
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='month_year_phishing_count.py',
        description='Count the number of online verified phishing submissions for months of a given year'
    )

    # Define the allowed script parameters
    parser.add_argument(
        "-y", "--year", type=int, help="Enter the year to count the number of phishing submissions for", required=True
    )
    parser.add_argument(
        "-f", "--file", type=str, help="Enter the file to read the phishing submissions from", required=True
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to count the phishing submissions by month and year
    count_phishing_submissions_by_month_year(args.year, args.file)
