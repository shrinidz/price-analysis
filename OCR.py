from PIL import Image  # Importing the Image class from PIL library
import pytesseract  # Importing pytesseract for OCR (Optical Character Recognition)
import os  # Importing os module for operating system functionalities
import re  # Importing re module for regular expressions
import csv  # Importing csv module for CSV handling

# Path to the directory containing images
directory_path = "D:/python projects/hindi book price analysis/pythonProject/screen_shots"

# Path to store the CSV file
csv_file_path = "D:/python projects/hindi book price analysis/pythonProject/product_prices.csv"

# CSV header
csv_header = ["Product Name", "Price", "Ratings"]

try:
    # Open the CSV file in 'write' mode with newline=''
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)  # Create a CSV writer object
        writer.writerow(csv_header)  # Write the header to CSV

        # Iterating over each file in the directory
        for filename in os.listdir(directory_path):
            image_path = os.path.join(directory_path, filename)  # Full path to the image file

            # Opening the image file using PIL's Image class
            with Image.open(image_path) as image:
                # Using pytesseract to extract text from the image
                text = pytesseract.image_to_string(image, lang='eng')  # Specify language if necessary

                # Extracting product name (assuming it's the first line of text)
                lines = text.splitlines()
                if lines:
                    product_name = lines[0].strip()
                else:
                    product_name = "Unknown"  # If no text found, use "Unknown" as product name

                # Extracting price using regular expression
                price_match = re.search(r'\$(\d+)', text)
                if price_match:
                    price = price_match.group().split('$')[-1]
                else:
                    price = None  # Set price to None if no match found

                # Extracting ratings using regular expression
                ratings_match = re.search(r'(\d+)\s+ratings', text)
                if ratings_match:
                    ratings = ratings_match.group(1)  # Use group(1) to get only the digits
                else:
                    ratings = None  # Set ratings to None if no match found

                # Writing to CSV: product name, price, ratings
                writer.writerow([product_name, price, ratings])

                # Printing extracted details for each image (optional)
                print(f"Product Name: {product_name}, Price: {price}, Ratings: {ratings}")

    print(f"CSV file '{csv_file_path}' created successfully.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please check if the directory path '{directory_path}' is correct or exists.")

except Exception as e:
    print(f"Error: {e}. An unexpected error occurred while processing the images or writing to CSV.")

