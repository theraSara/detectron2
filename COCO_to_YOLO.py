import json
import os
import pandas as pd


batch_images = "TACO/data"
taco_json = "TACO/data/annotations.json"
taco_images = "TACO/data/all_image_urls.csv"
output_dir = "YOLO"

# Load the TACO dataset
csv_df = pd.read_csv(taco_images)

print(csv_df.head())
print(csv_df.columns)

# Ensure column names are correct (make sure it's actually two columns as expected)
csv_df.columns = ["url", "url2"]

with open(taco_json, "r") as f:
    taco_annotations = json.load(f)

# Create a dictionary to map image IDs to file names
os.makedirs(output_dir, exist_ok=True)

# Create a dictionary for fast category_id to class mapping
category_map = {category['id']: category['name'] for category in taco_annotations['categories']}

def convert_to_yolo(image_width, image_height, bbox):
    xmin, ymin, bbox_width, bbox_height = bbox
    x_center = (xmin + bbox_width / 2.0) / image_width
    y_center = (ymin + bbox_height / 2.0) / image_height
    width = bbox_width / image_width
    height = bbox_height / image_height
    return x_center, y_center, width, height

for _, row in csv_df.iterrows():
    image_url = row["url"]
    image_filename = os.path.basename(image_url)

    print(f"CSV filename: {image_filename}")  # Debugging line

    image_info = next((image for image in taco_annotations['images'] if image['file_name'] == image_filename), None)
    print(f"Image info: {image_info}")  # Debugging line

    if not image_info:
        print(f"Image info not found for {image_filename}")  # Debugging line
        continue

    image_width = image_info['width']
    image_height = image_info['height']


    # Create an empty list to hold YOLO annotations
    yolo_annotations = []

    # Find annotations for the image
    for annotation in taco_annotations['annotations']:
        if annotation['image_id'] == image_info['id']:
            print(f"Found annotation for {image_filename}: {annotation}")  # Debugging line

            # Get the class_id and convert it to YOLO format
            category_id = annotation['category_id'] - 1
            bbox = annotation['bbox']
            # Convert bounding box to YOLO format
            x_center, y_center, width, height = convert_to_yolo(image_width, image_height, bbox)

            # Add the annotations in YOLO format
            yolo_annotations.append(f"{category_id} {x_center} {y_center} {width} {height}")

    # Save the YOLO annotations to a text file
    if yolo_annotations:
        print(f"Annotations for {image_filename}: {yolo_annotations}")  # Add this for debugging
        annotation_file = os.path.join(output_dir, image_filename.replace('.jpg', '.txt').replace('.png', '.txt'))
        with open(annotation_file, 'w') as f:
            f.write('\n'.join(yolo_annotations))
        print(f"Annotation saved to: {annotation_file}")  # Confirm file path

print("Annotations converted to YOLO format successfully!")
