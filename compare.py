import csv  # Importing the csv module for CSV handling

# Dummy data for extracted OCR prices (replace with actual data)
image_prices = ['208', '300']

# Dictionary to store results
result_dict = {"matching_prices": [], "price_discrepancies": []}

try:
    # Reading book details from CSV file
    with open("book_details.csv", newline='') as file:
        csv_reader = csv.DictReader(file)  # Creating a CSV reader object
        extracted_data = []  # List to store extracted data

        # Iterating through each row in the CSV file
        for row in csv_reader:
            extracted_data.append(row)  # Appending each row to extracted_data list

    # Comparing OCR-extracted prices with Selenium-scraped prices
    for i, row in enumerate(extracted_data):
        try:
            # Extracting OCR price and expected price from CSV
            ocr_price = image_prices[i]  # Assuming OCR-extracted price (replace with actual OCR logic)
            price = row["Price"].split('₹')[-1]  # Extracting expected price from CSV row

            # Comparing OCR price with expected price
            if ocr_price == price:
                result_dict["matching_prices"].append({
                    "Name": row["Name"],
                    "Price": row["Price"],
                    "Rating": row["Rating"]
                })
            else:
                result_dict["price_discrepancies"].append({
                    "Name": row["Name"],
                    "Price": price,
                    "OCR_Price": ocr_price,
                    "Rating": row["Rating"]
                })

        except IndexError:
            break  # Break the loop if index error occurs (more OCR prices than rows in CSV)

    # Writing results to a new CSV file
    output_csv_file = "comparison_results.csv"
    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Name", "Price", "OCR_Price", "Rating", "Result Type"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Writing items with matching prices
        for item in result_dict["matching_prices"]:
            item["Result Type"] = "Matching Price"
            writer.writerow(item)

        # Writing items with price discrepancies
        for item in result_dict["price_discrepancies"]:
            item["Result Type"] = "Price Discrepancy"
            writer.writerow(item)

    print(f"Comparison results written to '{output_csv_file}' successfully.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please check if the CSV file 'book_details.csv' exists.")

except Exception as e:
    print(f"Error: {e}. An unexpected error occurred while processing the CSV file.")

