import os
import shutil
import xml.etree.ElementTree as ET

# Paths to XML files and images
xml_folder = 'C:/Users/USER OS/OneDrive/Desktop/train'  
image_folder = 'C:/Users/USER OS/OneDrive/Desktop/train' 

# Create the "Annotation" directory if it doesn't exist
annotation_folder = os.path.join(xml_folder, 'Annotation')
os.makedirs(annotation_folder, exist_ok=True)

# Iterate over XML files
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_folder, xml_file)
        
        # Parse the XML file to get image filename and label data
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        image_filename = root.find('filename').text
        label_data = ET.tostring(root.find('object'), encoding='unicode')
        
        # Find the corresponding image in the image folder
        image_path = os.path.join(image_folder, image_filename)
        if os.path.exists(image_path):
            # Create "images" and "labels" directories inside "Annotation"
            images_dir = os.path.join(annotation_folder, 'images')
            labels_dir = os.path.join(annotation_folder, 'labels')
            os.makedirs(images_dir, exist_ok=True)
            os.makedirs(labels_dir, exist_ok=True)
            
            # Copy the image to "images" folder
            new_image_path = os.path.join(images_dir, image_filename)
            shutil.copy(image_path, new_image_path)
            
            # Write label data to a corresponding text file in "labels" folder
            label_filename = os.path.splitext(image_filename)[0] + '.txt'
            label_path = os.path.join(labels_dir, label_filename)
            with open(label_path, 'w') as label_file:
                label_file.write(label_data)

print("Data organization completed.")
