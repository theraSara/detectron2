import os
import json
import shutil

# Paths
json_path = r"C:\Users\PC\OneDrive\Documents\SR\smart-recycling-detection\TACO\data\annotations.json"
dataset_folder = r"C:\Users\PC\OneDrive\Documents\SR\smart-recycling-detection\taco_dataset\images"
source_folder = r"C:\Users\PC\OneDrive\Documents\SR\smart-recycling-detection\TACO\data"

os.makedirs(dataset_folder, exist_ok=True)

# Load JSON
with open(json_path, "r") as f:
    annotations = json.load(f)
print(json.dumps(annotations, indent=2))  # Pretty-print JSON


print(f"Total images in dataset: {len(annotations['images'])}")

moved_count = 0
for img in annotations["images"]:
    src_path = os.path.join(source_folder, img["file_name"])
    dst_path = os.path.join(dataset_folder, os.path.basename(img["file_name"]))

    # Print paths for debugging
    print(f"Checking: {src_path}")

    if os.path.exists(src_path):
        print(f"✅ Found! Moving: {src_path} -> {dst_path}")
        shutil.move(src_path, dst_path)
        moved_count += 1
    else:
        print(f"⚠️ NOT FOUND: {src_path}")

print(f"✅ Total images moved: {moved_count}")
import os
test_path = r"C:\Users\PC\OneDrive\Documents\SR\smart-recycling-detection\TACO\data\some_image.jpg"
print(f"Exists: {os.path.exists(test_path)}")

