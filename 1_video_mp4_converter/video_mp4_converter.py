import cv2
import pathlib
import os
import argparse
import shutil


def video_to_mp4(
    input, output, fps: int = 0, frame_size: tuple = (), fourcc: str = "H264"
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

            # add a 0 to the file name if it doesn't have one
            if file[-5] != '0':
                os.rename(file_path, file_path[:-4] + '0' + file_path[-4:])
                file_path = os.path.join(root, file[:-4] + '0' + file[-4:])

            # if the file is not an mp4, convert it
            if pathlib.Path(file_path).suffix.lower() != '.mp4':
                base_file = os.path.splitext(file)[0]
                out_path = os.path.join(output_path, base_file + ".mp4")
                new_video = video_to_mp4(file_path, output=out_path)
                print(new_video)
                
            else:
                # output the file as is
                out_path = os.path.join(output_path, file)
                print(f"Copying: {file} to {out_path}")
                shutil.copy(file_path, out_path)


def main():
    parser = argparse.ArgumentParser(
        prog='convert_to_mp4.py',
        description='Convert non MP4 videos to MP4'
    )
    parser.add_argument('-i', '--input', required=True, help='Input video directory')
    parser.add_argument('-o', '--output', required=True, help='Output video directory')
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    process_video_files(args.input, args.output)


if __name__ == "__main__":
    main()
