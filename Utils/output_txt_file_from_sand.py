import xlwings as xw
import sys
from tqdm import tqdm
import time

def xlsm_to_txt(xlsm_file, sheet_name, txt_file):

    print(f"Attempting to read {xlsm_file}")
    # Connect to Excel application
    app = xw.App(visible=False)
    wb = app.books.open(xlsm_file)

    # Select the specific sheet
    sheet = wb.sheets[sheet_name]

    # Get the number of rows
    num_rows = sheet.used_range.last_cell.row
    time.sleep(5)

    # Open a text file for writing
    with open(txt_file, 'w') as txt:
        # Iterate through rows in the sheet
        for row_idx in tqdm(range(1, num_rows + 1), desc="Reading"):
            row_values = sheet.range(f"A{row_idx}").expand('right').value
            if row_values is not None:  # Check if row_values is not None
                # Check if all cells in the row are None (empty)
                if all(cell is None for cell in row_values):
                    # Write an empty line to the text file
                    txt.write('\n')
                else:
                    # Write each row's content to the text file
                    txt.write('\t'.join(str(cell) if cell is not None else '' for cell in row_values) + '\n')
            else:
                # Write an empty line to the text file if row_values is None
                txt.write('\n')


    # Close Excel application
    wb.close()
    app.quit()

    print(f"Contents of '{sheet_name}' sheet from '{xlsm_file}' have been written to '{txt_file}'.")

if __name__ == "__main__":
    # Check if xlsm file path is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <xlsm_file_path> [<sheet_name>] [<txt_file_path>]")
        sys.exit(1)

    # Get xlsm file path from command line
    xlsm_file = sys.argv[1]

    # Set default values for sheet name and output text file path
    sheet_name = "ToDataFile"
    txt_file = f"{xlsm_file[:-4]}TXTconverted.txt"

    # If provided, get sheet name from command line
    if len(sys.argv) >= 3:
        sheet_name = sys.argv[2]

    # If provided, get output text file path from command line
    if len(sys.argv) >= 4:
        txt_file = sys.argv[3]

    # Call the function
    xlsm_to_txt(xlsm_file, sheet_name, txt_file)
