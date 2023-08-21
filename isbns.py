import pandas as pd
import requests

# Load the CSV file into a Pandas DataFrame
# Replace with the actual path to your CSV file
file_path = "/Users/carolinesanicola/Downloads/Library - Audiobooks - All [19].csv"
df = pd.read_csv(file_path)

# Define a function to fetch the ISBN using the Open Library API


def fetch_isbn(author, title):
    try:
        query = f"author:{author}+title:{title}"
        url = f"https://openlibrary.org/search.json?q={query}"
        response = requests.get(url)
        data = response.json()
        if 'docs' in data and len(data['docs']) > 0 and 'isbn' in data['docs'][0] and len(data['docs'][0]['isbn']) > 0:
            # Get the first ISBN from the search results
            isbn = data['docs'][0]['isbn'][0]
            return isbn
        else:
            print(f"No ISBN found for {title} by {author}")
            return None
    except Exception as e:
        print(f"Error fetching ISBN for {title}: {e}")
        return None


# Fetch the ISBN for each book and update the DataFrame
for index, row in df.iterrows():
    isbn = fetch_isbn(row['Author'], row['Title'])
    df.at[index, 'ISBN'] = isbn

# Save the updated DataFrame to a new CSV file
# Replace with the desired path for the output CSV file
output_file_path = "/Users/carolinesanicola/Downloads/Library - Audiobooks - All [19]_ISBNS.csv"
df.to_csv(output_file_path, index=False)
