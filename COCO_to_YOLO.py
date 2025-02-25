import json
import os

# Define paths
taco_json = "TACO/data/annotations.json"
output_dir = "YOLO"

# Load the TACO annotations
with open(taco_json, "r") as f:
    taco_annotations = json.load(f)

# Ensure YOLO output directory exists
os.makedirs(output_dir, exist_ok=True)

# Create a dictionary to map category_id to class names
category_map = {category['id']: category['name'] for category in taco_annotations['categories']}

# Function to convert COCO bbox format to YOLO
def convert_to_yolo(image_width, image_height, bbox):
    xmin, ymin, bbox_width, bbox_height = bbox
    x_center = (xmin + bbox_width / 2.0) / image_width
    y_center = (ymin + bbox_height / 2.0) / image_height
    width = bbox_width / image_width
    height = bbox_height / image_height
    return x_center, y_center, width, height

# Process each image in the annotations
for image_info in taco_annotations['images']:
    image_filename = image_info['file_name']  # Example: "batch_1/000006.jpg"
    image_width = image_info['width']
    image_height = image_info['height']

    # Extract batch folder name (if present)
    batch_folder = os.path.dirname(image_filename)  # Extracts "batch_1"

    # Ensure we don't duplicate batch folder
    batch_output_dir = os.path.join(output_dir, batch_folder) if batch_folder else output_dir

    # Ensure batch folder exists
    os.makedirs(batch_output_dir, exist_ok=True)

    # Find annotations for this image
    yolo_annotations = []
    for annotation in taco_annotations['annotations']:
        if annotation['image_id'] == image_info['id']:
            category_id = annotation['category_id'] - 1  # YOLO class index starts from 0
            bbox = annotation['bbox']

            # Convert bounding box to YOLO format
            x_center, y_center, width, height = convert_to_yolo(image_width, image_height, bbox)
            yolo_annotations.append(f"{category_id} {x_center} {y_center} {width} {height}")

    # Save YOLO annotations to the correct batch folder
    if yolo_annotations:
        annotation_file = os.path.join(batch_output_dir, os.path.basename(image_filename).replace('.jpg', '.txt').replace('.png', '.txt'))
        
        # Write the annotations
        with open(annotation_file, 'w') as f:
            f.write('\n'.join(yolo_annotations))

print("TACO dataset successfully converted to YOLO format!")

