# 3D Gaussian Splatting

## Prepare own data

1. capturing a view through around an object

2. using `ffmpeg -i video.mp4 -r 2 -f image2 input/%06d.jpg`

- `-i` input video
- `-r` frame: fps -- control the number the the output images
- `input/%60d.jpg`: set the image name always is format as "000001.jpg"
- output folder: `input/`

> .mov to .mp4: `ffmpeg -i gz.mov -vcodec copy -acodec copy gz.mp4 `

3. Using Colmap (windows) to generate camera params

- Run `COLMAP.bat`
- Click `Reconstruction` Select `Automatic reconstruction`
  - "Workspace folder": Select a project folder
  - "Image folder": Select the input image folder
- Click `Run`


> Download COLMAP: [here](https://github.com/colmap/colmap/releases)

4. Sparse reconstruction result can get: 
```
<location>
|---input
|   |---<image 0>
|   |---<image 1>
|   |---...
|---colmap
|   |---sparse
|       |---0
|           |---cameras.bin
|           |---images.bin
|           |---points3D.bin
|   |---database.db
```

5. Final File Structure 
```
<location>
|---images
|   |---<image 0>
|   |---<image 1>
|   |---...
|---sparse
    |---0
        |---cameras.bin
        |---images.bin
        |---points3D.bin
```

## Train Own Data
  
`python train.py --grad_thresh 0.000004 --debug 1 --ssim_weight 0.1 --lr 0.002 --use_sh_coeff 0 --grad_accum_method mean --grad_accum_iters 300 --split_thresh 0.08`

`CUDA_VISIBLE_DEVICES=1 python train.py --exp train --data /223010087/SimonWorkspace/3dgs/data/tandt/train/`

## Rendering

`python train.py --ckpt default/ckpt.pth --gui 1 --test 1`