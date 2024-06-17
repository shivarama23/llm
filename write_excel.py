# Specify the output CSV file path
output_file_path = 'output.csv'

with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write column names as the first row (optional)
    writer.writerow(column_names)

    # Write all rows to the CSV file
    writer.writerows(rows)
