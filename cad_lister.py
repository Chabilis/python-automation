# cad_lister.py - Your First Automation Tool
import os

print("🔍 CAD File Scanner - Starting...\n")

# Test with Desktop folder (CHANGE LATER)
folder = r"C:\Users\Marlou\Desktop\DWG files\cad"

if os.path.exists(folder):
    print(f"✅ Scanning: {folder}")
    
    # Find ALL .dwg files
    dwg_files = [f for f in os.listdir(folder) if f.lower().endswith(".dwg")]
    
    if dwg_files:
        print("📁 FOUND CAD FILES:")
        for file in dwg_files:
            print(f"  📄 {file}")
        print(f"\n🎉 Total: {len(dwg_files)} files")
    else:
        print("ℹ️  No .dwg files found (normal for Desktop)")
        
else:
    print("❌ Folder not found - update the path!")