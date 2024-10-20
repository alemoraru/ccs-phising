import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create a DataFrame from the list of counts and country names
data = {
    "Count": [
        74, 28, 2, 44, 8, 68, 2, 1, 8, 5, 620, 110, 1, 3, 1, 384,
        15, 28, 879, 6, 40, 54, 574, 4, 1, 1, 3, 20, 7, 158, 323, 4, 1, 
        6, 1, 72, 3, 12, 31, 79, 13, 68, 66, 18, 371, 1, 77, 1, 1, 48, 
        3, 2, 43, 3, 9, 56, 18, 1, 3, 1, 1, 7, 2, 207, 2, 854, 2, 16, 
        2, 2, 5, 57, 191, 20, 1, 29, 1, 859, 272, 245, 2907, 2, 10, 
        1, 17, 74, 18, 97, 121283, 1, 71, 124
    ],
    "Country Code": [
        "AE", "AG", "AM", "AR", "AT", "AU", "AZ", "BA", "BD", "BE",
        "BG", "BR", "BT", "BY", "BZ", "CA", "CH", "CL", "CN", "CO", "CY", 
        "CZ", "DE", "DK", "DM", "EC", "EE", "ES", "FI", "FR", "GB", "GE", 
        "GI", "GR", "GT", "HK", "HR", "HU", "ID", "IE", "IL", "IN", "IR", 
        "IS", "IT", "JO", "JP", "KG", "KH", "KR", "KZ", "LK", "LT", "LU", 
        "LV", "MA", "MD", "ME", "MN", "MO", "MT", "MU", "MX", "MY", "NG", 
        "NL", "NO", "NP", "NZ", "OM", "PE", "PH", "PL", "PT", "PY", "RO", 
        "RS", "RU", "SC", "SE", "SG", "SI", "SK", "TG", "TH", "TR", "TW", 
        "UA", "US", "UY", "VN", "ZA"
    ],
    "Country Name": [
        "United Arab Emirates", "Antigua and Barbuda", "Armenia",
        "Argentina", "Austria", "Australia", "Azerbaijan", "Bosnia and Herzegovina", 
        "Bangladesh", "Belgium", "Bulgaria", "Brazil", "Bhutan", "Belarus", 
        "Belize", "Canada", "Switzerland", "Chile", "China", "Colombia", 
        "Cyprus", "Czech Republic", "Germany", "Denmark", "Dominica", 
        "Ecuador", "Estonia", "Spain", "Finland", "France", "United Kingdom", 
        "Georgia", "Gibraltar", "Greece", "Guatemala", "Hong Kong", 
        "Croatia", "Hungary", "Indonesia", "Ireland", "Israel", "India", 
        "Iran", "Iceland", "Italy", "Jordan", "Japan", "Kyrgyzstan", 
        "Cambodia", "South Korea", "Kazakhstan", "Sri Lanka", "Lithuania", 
        "Luxembourg", "Latvia", "Morocco", "Moldova", "Montenegro", 
        "Mongolia", "Macau", "Malta", "Mauritius", "Mexico", "Malaysia", 
        "Nigeria", "Netherlands", "Norway", "Nepal", "New Zealand", 
        "Oman", "Peru", "Philippines", "Poland", "Portugal", "Paraguay", 
        "Romania", "Serbia", "Russia", "Seychelles", "Sweden", "Singapore", 
        "Slovenia", "Slovakia", "Togo", "Thailand", "Turkey", "Taiwan", 
        "Ukraine", "United States", "Uruguay", "Vietnam", "South Africa"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
csv_file_path = 'resources/phishtank_country_counts.csv'
df.to_csv(csv_file_path, index=False)

# Create a new category 'Others' for countries beyond the top N
top_n = 10
top_countries = df.nlargest(top_n, 'Count')
others_count = df[~df['Country Name'].isin(top_countries['Country Name'])]['Count'].sum()

# Create a new DataFrame for others
others = pd.DataFrame({'Count': [others_count], 'Country Name': ['Others']})
df_combined = pd.concat([top_countries[['Count', 'Country Name']], others], ignore_index=True)

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Country Name', data=df_combined, palette='viridis')

# Annotate counts on the bars
for index, value in enumerate(df_combined['Count']):
    plt.text(value, index, f'{value}', va='center')

plt.title(f'Top {top_n} Countries with Others Combined')
plt.xlabel('Counts')
plt.ylabel('Country Name')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

if __name__ == '__main__':
    plt.show()
