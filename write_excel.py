# Specify the output CSV file path
output_file_path = 'output.csv'

with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write column names as the first row (optional)
    writer.writerow(column_names)

    # Write all rows to the CSV file
    writer.writerows(rows)


# Create a workbook and add a worksheet
workbook = Workbook()
sheet = workbook.active
sheet.title = "Data"

# Write column names to the first row (optional)
for col_num, column_title in enumerate(column_names, 1):
    sheet.cell(row=1, column=col_num, value=column_title)

# Write data rows to the Excel file
for row_num, row in enumerate(rows, 2):
    for col_num, cell_value in enumerate(row, 1):
        sheet.cell(row=row_num, column=col_num, value=cell_value)

# Save the workbook
output_file_path = 'output.xlsx'
workbook.save(output_file_path)

# Close the cursor and connection
cursor.close()
connection.close()
