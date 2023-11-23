import csv
import os
from tqdm import tqdm


# def convert_to_yolov5(root, csv_file):
#     with open(csv_file, 'r') as f:
#         reader = csv.DictReader(f)
#         for row in tqdm(reader):
#             image_file = os.path.join(root, row['Path'])
#             txt_file = os.path.splitext(image_file)[0] + '.txt'
#             width = float(row['Width'])
#             height = float(row['Height'])
#
#             x1 = float(row['Roi.X1'])
#             y1 = float(row['Roi.Y1'])
#             x2 = float(row['Roi.X2'])
#             y2 = float(row['Roi.Y2'])
#
#             # convert to center x, center y, width, height and normalize to 0-1
#             dw = 1.0 / width
#             dh = 1.0 / height
#             cx = (x1 + x2) / 2.0 * dw
#             cy = (y1 + y2) / 2.0 * dh
#             w = (x2 - x1) * dw
#             h = (y2 - y1) * dh
#
#             class_id = row['ClassId']
#
#             with open(txt_file, 'w') as tf:
#                 tf.write(f"{class_id} {cx} {cy} {w} {h}\n")


def convert_to_yolov5(root, csv_file):
    with open(csv_file, 'r') as f, open(os.path.join(root, 'test.txt'), 'w') as train_file:
        reader = csv.DictReader(f)
        for row in tqdm(reader):
            image_file = os.path.join(root, row['Path'])
            txt_file = os.path.splitext(image_file)[0] + '.txt'
            width = float(row['Width'])
            height = float(row['Height'])

            x1 = float(row['Roi.X1'])
            y1 = float(row['Roi.Y1'])
            x2 = float(row['Roi.X2'])
            y2 = float(row['Roi.Y2'])

            # convert to center x, center y, width, height and normalize to 0-1
            dw = 1.0 / width
            dh = 1.0 / height
            cx = (x1 + x2) / 2.0 * dw
            cy = (y1 + y2) / 2.0 * dh
            w = (x2 - x1) * dw
            h = (y2 - y1) * dh

            class_id = row['ClassId']

            with open(txt_file, 'w') as tf:
                tf.write(f"{class_id} {cx} {cy} {w} {h}\n")

            # write the image path to train.txt
            train_file.write(f"{image_file}\n")


root = "../data/gtsrb"  # replace with the path to your dataset directory
train_csv = os.path.join(root, "Test.csv")  # path to the Train.csv file

convert_to_yolov5(root, train_csv)
