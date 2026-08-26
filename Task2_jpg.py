import os
import shutil

source_fol = 'source_images'  # Source folder
dest_fol = 'destination_images'  # Destination folder
moved_files = 0  # Counter for moved files

# Check if source folder exists
if not os.path.exists(source_fol):
    print(f"❌ Error: Source folder '{source_fol}' not found!")
    print("Please create the folder and add .jpg files.")
    exit()

# Create destination folder if it doesn't exist
if not os.path.exists(dest_fol):
    os.makedirs(dest_fol)
    print(f"Created folder: {dest_fol}")

print("\n╔════════════════════════════╗")
print("║     MOVING JPG FILES       ║")
print("╚════════════════════════════╝")

# Get list of files
all_files = os.listdir(source_fol)
jpg_files = [f for f in all_files if f.lower().endswith('.jpg')]

if not jpg_files: 
    print(f"\n📭 No .jpg files found in '{source_fol}'")
    exit()

print(f"\n🔍 Found {len(jpg_files)} .jpg file(s) in '{source_fol}'")
print("═" * 40)

# Process each .jpg file
for file_name in jpg_files:
    full_file_name = os.path.join(source_fol, file_name)
    
    # Ensure it's a file, not a folder
    if os.path.isfile(full_file_name):
        try:
            shutil.move(full_file_name, dest_fol)
            print(f"✓ Moved: {file_name}")
            moved_files += 1
        except PermissionError:
            print(f"✗ Skipped {file_name} (permission denied)")
        except Exception as e:
            print(f"✗ Error with {file_name}: {e}")
    else:
        print(f"⚠ Skipped {file_name} (not a file)")

# Final summary
print("\n" + "═" * 40)
print("PROCESSING SUMMARY")
print("═" * 40)
print(f"✅ Successfully moved {moved_files} file(s)")
print(f"📁 From: {source_fol}")
print(f"📁 To: {dest_fol}")
print("═" * 40)

# Show what's left in source folder
if os.path.exists(source_fol):
    remaining_files = [f for f in os.listdir(source_fol) if f.lower().endswith('.jpg')]
    if remaining_files:
        print(f"📊 Remaining .jpg files in '{source_fol}': {len(remaining_files)}")
    else:
        print(f"📊 All .jpg files moved from '{source_fol}'")
else:
    print(f"📊 Source folder '{source_fol}' no longer exists")