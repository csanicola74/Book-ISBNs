import pandas as pd
import requests

# Load the CSV file into a Pandas DataFrame
file_path = "/Users/carolinesanicola/Downloads/Library - Audiobooks - All [19].csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Define a function to fetch the ISBN using the Open Library API
def fetch_isbn(author, title):
    try:
        query = f"author:{author}+title:{title}"
        url = f"https://openlibrary.org/search.json?q={query}"
        response = requests.get(url)
        data = response.json()
        isbn = data['docs'][0]['isbn'][0]  # Get the first ISBN from the search results
        return isbn
    except Exception as e:
        print(f"Error fetching ISBN for {title}: {e}")
        return None

# Fetch the ISBN for each book and update the DataFrame
for index, row in df.iterrows():
    isbn = fetch_isbn(row['Author'], row['Title'])
    df.at[index, 'ISBN'] = isbn

# Save the updated DataFrame to a new CSV file
output_file_path = "path/to/output/csv/file.csv"  # Replace with the desired path for the output CSV file
df.to_csv(output_file_path, index=False)
