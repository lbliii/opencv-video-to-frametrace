## About

This example intakes videos and outputs traced frames. If the videos are not in `.jpg` format, they are converted by the `video_mp4_converter` pipeline before being passed to the `image_flattener` pipeline. The `image_flattener` pipeline then outputs the traced frames to the `output` repo.


## How to Run This Example 

1. Create a project named `video-to-frame-traces`:
   
   ```
   pachctl create project video-to-frame-traces
   pachctl config update context --project video-to-frame-traces
   ```
2. Create a repo named `raw_videos`:
   
   ```
   pachctl create repo raw_videos
   ```
3. Create the video converter pipeline:
   
   ```
   pachctl create pipeline -f 1_video_mp4_converter/video_mp4_converter.yaml 
   ```
4. Create the pipeline:
   
    ```
    pachctl create pipeline -f 2_image_flattener/image_flattener.yaml
    ```
5. Add a movie `pachctl put file raw_videos@master -f movies/cat-sleeping.MOV`


## Attributes

This is based off of [Reid's Pachd_Pipelines repo](https://github.com/dpsi4/pachd_pipelines), which extends the basic OpenCV example to support the conversion of videos to jpg frames.