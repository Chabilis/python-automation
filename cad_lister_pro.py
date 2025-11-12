# cad_lister_pro.py - P 2,000 (idk if true) Client tool
import os
import pandas as pd         # what is 'pd'
import webbrowser           # what is this for?

print("CAD TO EXCEL AUTOMATOR - v2 \n")

# folder = r"C:\Users\Marlou\Desktop\DWG Files\cad" (version 1)
folder = input("Enter CAD folder path: ").strip('"')

if not os.path.exists(folder):
    print("Folder not found.")

else:
    dwg_files = [
        y for y in os.listdir(folder)       # I change to 'y' because it 'this_file' is not defined
        if y.lower().endswith(".dwg")
    ]

    # export to excel
    df = pd.DataFrame(dwg_files, columns=["CAD-FILE"])      # what is this?
    # output_file = input("Enter the name of the file: ").endswith(".xlsx")  - I tried this one but didnt work.
    output_file = "CAD_Report.xlsx"             # What happens if the file aready exist?
    df.to_excel(output_file, index=False)             

    print(f"Success! {len(dwg_files)} files -> {output_file}")
    # print("Check your folder!") - version 1
    webbrowser.open(output_file)            # Auto open excel COOL!!!