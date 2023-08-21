#! /Users/reidm/anaconda3/envs/openCV/bin/python

"""
Take Video input and flatten it to individual frames/images
"""

import cv2
import os
import argparse
import pathlib

def flatten_video(vid_path, out_path, base_file):
    os.makedirs(out_path, exist_ok=True)

    current_frame = 0
    video = cv2.VideoCapture(vid_path)

    while True:
        ret, frame = video.read()

        if ret:
            name = os.path.join(out_path, f'{base_file}-frame-{current_frame:010d}.jpg')
            cv2.imwrite(name, frame)
            current_frame += 1
        else:
            break

    video.release()

def process_video_files(input_path, output_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)

            if pathlib.Path(file_path).suffix.lower() == '.mp4':
                base_file = os.path.splitext(file)[0]
                out_path = os.path.join(output_path, base_file)
                print(f"Converting: {file}")
                flatten_video(file_path, out_path, base_file)
            else:
                print(f"Skipping: {file_path}")

def main():
    parser = argparse.ArgumentParser(
        prog='flatten_to_images.py',
        description='Flatten Video to Images'
    )
    parser.add_argument('-i', '--input', required=True, help='Input video directory')
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

    process_video_files(args.input, args.output)

if __name__ == "__main__":
    main()
