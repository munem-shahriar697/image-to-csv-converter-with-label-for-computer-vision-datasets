from PIL import Image
import numpy as np
import os
import csv
import cv2

# image resizing to 28*28 pixels
# it also saves the resized images according to the file hierarchy
i = 1
for i in range(1, 63):
    print("resizing file no: " + str(i))
    j = str(i)
    k = str(i - 1)
    # selecting image folder path
    # this if is not mandatory. i used it because of my file naming convention. chage this according to yours
    if i < 10:
        input_folder = "E:\\EnglishFnt.tgz\\image_resizer_test\\input\\Sample00" + j
        output_folder = "E:\\EnglishFnt.tgz\\image_resizer_test\\output\\" + k
    else:
        input_folder = "E:\\EnglishFnt.tgz\\image_resizer_test\\input\\Sample0" + j
        output_folder = "E:\\EnglishFnt.tgz\\image_resizer_test\\output\\" + k

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # selecting image file type. change this according your file extension
    for filename in os.listdir(input_folder):
        if not filename.endswith(".png"):
            continue

        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

        # print("Original Dimensions: ", img.shape)

        # Define the target size
        width = 28
        height = 28
        dim = (width, height)

        # Resize the image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # print("Resized Dimensions: ", resized.shape)

        # Modify the output filename to use the .jpg extension
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_filename)

        # Save the resized image in JPEG format with a quality of 90 (adjust as needed)
        cv2.imwrite(output_path, resized, [cv2.IMWRITE_JPEG_QUALITY, 90])
        i += 1
    print("resizing done")

print("Your CSV has been written...")
i = 1
output_folder = "E:\\EnglishFnt.tgz\\image_resizer_test\\outputCSV.csv"
for i in range(1, 63):
    j = str(i)
    k = str(i - 1)

    folder_path = "E:\\EnglishFnt.tgz\\image_resizer_test\\output\\" + k

    with open(output_folder, "a", newline="") as f:
        writer = csv.writer(f)
        print("CSV being written...")
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                image_path = os.path.join(folder_path, filename)
                img = Image.open(image_path)

                # Convert image to NumPy array
                arr = np.asarray(img)

                # Flatten the 2D array
                flattened = arr.flatten()

                # adding label in the begining
                flattened_with_label = np.insert(flattened, 0, k)

                # Write the flattened data to the CSV file
                writer.writerow(flattened_with_label)
    print("Current label being written: label->" + k)
