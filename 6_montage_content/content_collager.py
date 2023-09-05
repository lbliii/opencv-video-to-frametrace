import os
import argparse
from bs4 import BeautifulSoup
import shutil

html_template = """
<html>
<head>
<title>Content Collage</title>
<style>
  #collage-container {
    display: flex;
  }

  #originals,
  #edges {
    flex: 1;
    padding: 20px;
    border: 1px solid #ccc;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px; 
  }
</style>
</head>
<body>
<h1>Content collage</h1>
<div id="collage-container">
<div id="originals">
<h2>Original</h2>
</div>
<div id="edges">
<h2>Edges</h2>
</div>
</div>
</body>
</html>
"""

def create_html_page(output_path):
    index_path = os.path.join(output_path, "collage", "index.html")
    
    if not os.path.exists(os.path.join(output_path, "collage")):
        os.makedirs(os.path.join(output_path, "collage"))

    if not os.path.exists(index_path):
        with open(index_path, "w") as f:
            f.write(html_template)

def append_image_to_html_page(output_path, image_path):
    index_path = os.path.join(output_path, "collage", "index.html")

    with open(index_path, "r") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    # if the image path has the word "originals" in it, add it to the originals div
    if "edges" in image_path:
        originals_div = soup.find("div", id="edges")
        if originals_div:
            img_tag = soup.new_tag("img", src=image_path, width="300", style="display: block;")
            originals_div.append(img_tag)

        with open(index_path, "w") as f:
            f.write(str(soup))
    # otherwise, add it to the collage div
    else:
        collage_div = soup.find("div", id="originals")
        if collage_div:
            img_tag = soup.new_tag("img", src=image_path, width="300", style="display: block;")
            collage_div.append(img_tag)

        with open(index_path, "w") as f:
            f.write(str(soup))

def process_content(input_path, output_path):
    try:
        # Create the HTML page
        create_html_page(output_path)

        # Create the output directory /collage/static
        static_output_path = os.path.join(output_path, "collage", "static")
        if not os.path.exists(static_output_path):
            os.makedirs(static_output_path)

        for dirpath, _, files in os.walk(input_path):
            sorted_files = sorted(files)
            for file in sorted_files:
                print(f"Copying {file} to {static_output_path}")
                shutil.copy(os.path.join(dirpath, file), os.path.join(static_output_path, file))
                append_image_to_html_page(output_path, f"./static/{file}")

    except Exception as e:
        print(f"Exception: {e}")

def main():
    parser = argparse.ArgumentParser(
        prog='content_collager.py',
        description='Convert images and gifs into a collage'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input} \nOutput: {args.output}\n")

    try:
        process_content(args.input[0], args.output)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
