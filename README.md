## About

This example intakes videos and outputs edge-detected frames. If the videos are not in `.mp4` format (e.g, `.mov  `), they are converted by the `video_mp4_converter` pipeline before being passed to the `image_flattener` pipeline. Otherwise, they are passed directly to the `image_flattener` pipeline.

## Quickstart 

```s
gh repo clone lbliii/opencv-video-to-frametrace
cd opencv-video-to-frametrace
pachctl create project video-to-frame-traces
pachctl config update context --project video-to-frame-traces
pachctl create repo raw_videos
pachctl create pipeline -f 1_convert_videos/video_mp4_converter.yaml 
pachctl create pipeline -f 2_flatten_images/image_flattener.yaml
pachctl create pipeline -f 3_trace_images/image_tracer.yaml
```
## Walkthrough

1. Create a project named `video-to-frame-traces`:
   
   ```s
   pachctl create project video-to-frame-traces
   pachctl config update context --project video-to-frame-traces
   ```
2. Create a repo named `raw_videos`:
   
   ```s
   pachctl create repo raw_videos
   ```
3. Create the video converter pipeline:
   
   ```s
   pachctl create pipeline -f 1_convert_videos/video_mp4_converter.yaml 
   ```s
4. Create the image flattener pipeline:
   
    ```s
    pachctl create pipeline -f 2_flatten_images/image_flattener.yaml
    ```
5. Create the image tracing pipeline: 
    
    ```s
    pachctl create pipeline -f 3_trace_images/image_tracer.yaml
    ```
6. Add a movie `pachctl put file raw_videos@master -f movies/cat-sleeping.MOV`


## Attributes

This is based off of [Reid's Pachd_Pipelines repo](https://github.com/dpsi4/pachd_pipelines), which extends the basic OpenCV example to support the conversion of videos to jpg frames.