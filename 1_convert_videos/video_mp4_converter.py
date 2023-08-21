import cv2
import pathlib
import os
import argparse
import shutil

def video_to_mp4(
    input, output, fps: int = 0, frame_size: tuple = (), fourcc: str = "XVID"
):

    print(f"Converting video: {input}")
    vidcap = cv2.VideoCapture(input)
    if not fps:
        fps = round(vidcap.get(cv2.CAP_PROP_FPS))
    success, arr = vidcap.read()
    if not frame_size:
        height, width, _ = arr.shape
        frame_size = width, height
    writer = cv2.VideoWriter(
        output,
        apiPreference=0,
        fourcc=cv2.VideoWriter_fourcc(*fourcc),
        fps=fps,
        frameSize=frame_size,
    )
    frame_count = 0
    while success:
        frame_count += 1
        writer.write(arr)
        success, arr = vidcap.read()
    writer.release()
    vidcap.release()

    print(f"Converted {frame_count} frames")


def process_video_files(input_path, output_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip non-video files
            if not file_path.lower().endswith(('.mp4', '.avi', '.mov')):
                print(f"Skipping: {file_path}")
                return

            # Convert video files to MP4
            if file_path.lower().endswith(('.avi', '.mov')):
                base_file = os.path.splitext(file)[0]
                out_path = os.path.join(output_path, base_file + ".mp4")
                video_to_mp4(file_path, output=out_path)
                print(f"Converted: {file} to {out_path}")
                
            else:
                # Copy existing MP4 files
                out_path = os.path.join(output_path, file)
                print(f"Copying: {file} to {out_path}")
                shutil.copy(file_path, out_path)


def main():
    parser = argparse.ArgumentParser(
        prog='convert_to_mp4.py',
        description='Convert non-MP4 videos to MP4'
    )
    parser.add_argument('-i', '--input', required=True, help='Input video directory')
    parser.add_argument('-o', '--output', required=True, help='Output video directory')
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
