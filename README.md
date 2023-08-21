## About

This pipeline example uses OpenCV to convert videos and images into edge-detected frames. 

- If the videos are not in `.mp4` format (e.g, `.mov  `), they are converted by the `video_mp4_converter` pipeline before being passed to the `image_flattener` pipeline. Otherwise, they are passed directly to the `image_flattener` pipeline.
- Images from the `image_flattener` output and `raw_videos_and_images` repo are processed by the `edge-detector` pipeline.

### Reference Image

<p align="center">
![pipeline](/pipeline.svg)
</p>

## Quickstart 

```s
gh repo clone lbliii/opencv-video-to-frametrace
cd opencv-video-to-frametrace
pachctl create project video-to-frame-traces
pachctl config update context --project video-to-frame-traces
pachctl create repo raw_videos_and_images
pachctl create pipeline -f 1_convert_videos/video_mp4_converter.yaml 
pachctl create pipeline -f 2_flatten_images/image_flattener.yaml
pachctl create pipeline -f 3_trace_images/image_tracer.yaml
```

## Walkthrough

### 1. Create a Project 

By default, when you first start up an instance, the `default` project is attached to your active context. Create a new project and set attach it to your active pachctl context to avoid having to specify the project name (e.g., `--project video-to-frame-traces` ) in each command. 

```s
pachctl create project video-to-frame-traces
pachctl config update context --project video-to-frame-traces
```

### 2. Create an Input Repo 

At the top of our DAG, we'll need an input repo that will store our raw videos and images. 
   
```s
pachctl create repo raw_videos_and_images
```

### 3. Create the Video Converter Pipeline 

We want to make sure that our DAG can handle videos in multiple formats, so first we'll create a pipeline that will:

   - skip images 
   - skip videos already in the correct format (`.mp4`)
   - convert videos to `.mp4` format

The converted videos will be made available to the next pipeline in the DAG via the `video_mp4_converter` repo by declaring in the user code to save the converted images to `/pfs/out/`. 

```s
pachctl create pipeline -f 1_convert_videos/video_mp4_converter.yaml 
```


### 4. Create the Image Flattener Pipeline

Next, we'll create a pipeline that will flatten the frames of the videos into individual `.png` images. Like the previous pipeline, the user code outputs the frames to `/pfs/out` so that the next pipeline in the DAG can access them in the `image_flattener` repo. 

```s
pachctl create pipeline -f 2_flatten_images/image_flattener.yaml
```

### 5. Create the Image Tracing Pipeline: 

Finally, we'll create a pipeline that will trace the edges of the images. This pipeline will take a `union` of two inputs:
- the `image_flattener` repo, which contains the flattened images from the previous pipeline
- the `raw_videos_and_images` repo, which contains the original images that didn't need to be processed
    
```s
pachctl create pipeline -f 3_trace_images/image_tracer.yaml
```

### 6. Add Videos and Images 


#### Videos (Coming Soon)
```s
pachctl put file raw_videos_and_images@master: -f 

```

### Upload Images
```s
pachctl put file raw_videos_and_images@master:liberty.png -f https://raw.githubusercontent.com/pachyderm/docs-content/main/images/opencv/liberty.jpg

pachctl put file raw_videos_and_images@master:robot.png -f https://raw.githubusercontent.com/pachyderm/docs-content/main/images/opencv/robot.jpg
```


## Attributes

This is based off of [Reid's Pachd_Pipelines repo](https://github.com/dpsi4/pachd_pipelines), which extends the basic OpenCV example to support the conversion of videos to jpg frames.