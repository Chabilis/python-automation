# cad_lister.py - Your First Automation Tool
import os

print("🔍 CAD File Scanner - Starting...\n")

# Test with Desktop folder (CHANGE LATER)
# variable = r"directory"
folder = r"C:\Users\Marlou\Desktop\DWG files\cad"

if os.path.exists(folder):
    print(f"✅ Scanning: {folder}")
    
    # Find ALL .dwg files
    dwg_files = [f for f in os.listdir(folder) if f.lower().endswith(".dwg")]

    # all_files = os.listdir(variable) gets all the files inside the variable (r"directory")
    # for f in all_files: print(f) = displays all the files inside the folder
    # if f.lower().endswith(".dwg"): = displays all the files that ends ".dwg"
    # f for f in ... = this_file for this_item in os.listdir(folder)
    
    if dwg_files:
        print("📁 FOUND CAD FILES:")
        for file in dwg_files:
            print(f"  📄 {file}")
        print(f"\n🎉 Total: {len(dwg_files)} files")
    else:
        print("ℹ️  No .dwg files found (normal for Desktop)")
        
else:
    print("❌ Folder not found - update the path!")