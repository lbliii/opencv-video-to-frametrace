import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import argparse

def make_edges(image, output_path):
    try:
        img = cv2.imread(image)
        if img is None:
            print(f"Error reading image: {image}")
            return
        
        tail = os.path.split(image)[1]
        edges = cv2.Canny(img, 100, 200)
        output_filename = os.path.splitext(tail)[0] + '.png'
        output_filepath = os.path.join(output_path, output_filename)
        plt.imsave(output_filepath, edges, cmap='gray')
        print(f"Processed: {image} -> {output_filepath}")

    except Exception as e:
        print(f"Error processing image: {image}")
        print(f"Error details: {e}")

def process_image_files(input_path, output_path):
    for dirpath, dirs, files in os.walk(input_path):
        total = len(files)
        current = 0
        for file in files:
            current += 1
            print (f"Processing {file}, #{current} of {total}")
            make_edges(os.path.join(dirpath, file), output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='image_tracer.py',
        description='Trace Images'
    )
    parser.add_argument('-i', '--input', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input directory does not exist.")
        return
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    process_image_files(args.input, args.output)

if __name__ == "__main__":
    main()
