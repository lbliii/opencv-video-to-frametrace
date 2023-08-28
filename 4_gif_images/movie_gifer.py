import cv2
import os
import argparse
import imageio

def make_gifs(directory, input_path, output_path):
    try:
    
        # Create output folder if it doesn't exist
        relative_dir = os.path.relpath(directory, input_path)
        output_folder = os.path.join(output_path, relative_dir)
        os.makedirs(output_folder, exist_ok=True)

        # Get all the images in the provided directory
        images = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]

        # Sort the pngs so they are in order
        images.sort()

        # Create the output filename
        tail = os.path.split(directory)[1]
        base_filename = os.path.splitext(tail)[0]

        if 'tracer' in input_path:
           suffix = 'edges'
        else:
            suffix = 'original'
        output_filename = f'{base_filename}_{suffix}.gif'
        output_filepath = os.path.join(output_folder, output_filename)

        # Create the gif
        gif_images = [cv2.imread(i)[:, :, ::-1] for i in images]  # Convert BGR to RGB
        imageio.mimsave(output_filepath, gif_images, duration=0.1)

        print(f"Processed: {directory} -> {output_filepath}")

    except Exception as e:
        print(f"Error processing directory: {directory}")
        print(f"Error details: {e}")

def process_image_directories(input_path, output_path):
    # For each directory of images, make a gif
    for dirpath, dirs, files in os.walk(input_path):
        total = len(dirs)
        current = 0
        for dir in dirs:
            current += 1
            print(f"Processing {dir}, #{current} of {total}")
            make_gifs(os.path.join(dirpath, dir), input_path, output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='movie_gifer.py',
        description='Convert images to gifs'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    for input_path in args.input:
        if not os.path.exists(input_path):
            print(f"Input directory does not exist: {input_path}")
        else:
            print(f"Processing images in: {input_path}")
            process_image_directories(input_path, args.output)

    print("Done.")

if __name__ == "__main__":
    main()
