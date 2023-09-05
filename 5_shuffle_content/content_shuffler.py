import argparse
import os
import shutil

def shuffle_content(input_path, output_path):
    # create an originals and edges directory in the output path
    originals_output_path = f"{output_path}/originals"
    if not os.path.exists(originals_output_path):
        os.makedirs(originals_output_path)

    edges_output_path = f"{output_path}/edges"
    if not os.path.exists(edges_output_path):
        os.makedirs(edges_output_path)

    for dirpath, dirs, files in os.walk(input_path):
        for file in files:
            if "frame" and "edges" not in file:
                # Copy the original image to the originals directory
                shutil.copy(f"{dirpath}/{file}", originals_output_path)
            elif "frame" not in file and "edges" in file:
                # Copy the images and gifs to the edges directory
                shutil.copy(f"{dirpath}/{file}", edges_output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='content_collager.py',
        description='Convert images and gifs into a collage'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input} \nOutput: {args.output}\n")

    total_inputs = len(args.input)
    current_input = 0
    for input_path in args.input:
        try:
            current_input += 1
            print(f"{input_path}; {current_input}/{total_inputs}")
            shuffle_content(input_path, args.output)
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    main()
