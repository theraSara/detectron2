import json

with open(r"C:\Users\PC\OneDrive\Documents\SR\smart-recycling-detection\TACO\data\annotations.json", "r") as file:
    annotations = json.load(file)

# Print out some details about the annotations
print(json.dumps(annotations, indent=4))


# Example: Convert annotations to COCO format
coco_format = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "recyclable"}, {"id": 2, "name": "non_recyclable"}]
}

for img_info in annotations['images']:
    coco_format['images'].append({
        'id': img_info['id'],
        'file_name': img_info['file_name'],
        'width': img_info['width'],
        'height': img_info['height']
    })

for ann in annotations['annotations']:
    coco_format['annotations'].append({
        'image_id': ann['image_id'],
        'category_id': ann['category_id'],
        'bbox': ann['bbox'],
        'area': ann['area'],
        'iscrowd': ann['iscrowd']
    })

# Save the COCO formatted annotations
with open("coco_annotations.json", "w") as f:
    json.dump(coco_format, f)

