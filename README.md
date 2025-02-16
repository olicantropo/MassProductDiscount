# MassProductDiscount
This Python script updates a CSV file by applying a price reductions to the values in the "price" column while proportionally adjusting the values in the "discountValue" column to maintain the correct discount ratio.

How it Works:

Reads the CSV file: It loads the data from the specified input file (input.csv).
Checks for required columns: Ensures that "price" and "discountValue" columns exist; otherwise, it raises an error.

Processes each row:
Converts the "price" and "discountValue" values to float, handling potential empty or invalid values.
Reduces the "price" by the needed value (price * [value]).
Adjusts "discountValue" proportionally to match the new price.

Handles errors: If a row contains invalid data, it skips the row and prints an error message.
Writes the updated data to a new CSV file (output.csv).

Expected Outcome:
The new CSV file contains updated prices and discount values, ensuring consistency after applying the reduction.
