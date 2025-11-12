# cad_lister_pro.py - P 2,000 (idk if true) Client tool
import os
import pandas as pd         # pd = nickname for pandas but I can name anything
import webbrowser           # opens files in your default app

print("CAD TO EXCEL AUTOMATOR - v2 \n")

# folder = r"C:\Users\Marlou\Desktop\DWG Files\cad" (version 1)
folder = input("Enter CAD folder path: ").strip('"')

if not os.path.exists(folder):
    print("Folder not found.")

else:
    dwg_files = [
        y for y in os.listdir(folder)       # [ OUTPUT for LOOP_VAR in list if condition ]
        if y.lower().endswith(".dwg")
    ]

    # export to excel
    df = pd.DataFrame(dwg_files, columns=["CAD-FILE"])      # df = "DataFrame" = Excel table in Python
    # output_file = input("Enter the name of the file: ").endswith(".xlsx")  - .endswith() returns boolean

#   If i want user input
#   name = input("Enter file name: ")
#   if not name.endswith(".xlsx"):
#       name += ".xlsx"
#   output_file = name

    output_file = "CAD_Report.xlsx"             # if the file aready exist, It overwrites silently

    # Adding timeframe is great
    # import datetime
    # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")    
    # output_file = f"CAD_Report_{timestamp}.xlsx"
    # result - > CAD_Report_20251112_2215.xlsx


    df.to_excel(output_file, index=False)             

    print(f"Success! {len(dwg_files)} files -> {output_file}")
    # print("Check your folder!") - version 1
    webbrowser.open(output_file)            # Auto open excel COOL!!!