# ZED-camera-installation
Installation for zed camera

## Preinstall.

```
conda install -c conda-forge gcc
python -m pip install cython numpy
python -m pip install opencv-python pyopengl
```

## Install SDK for ubuntu.

Download file from

```
https://www.stereolabs.com/developers/release#82af3640d775
```

Run file
```
bash /SDK ubuntu/ZED_SDK_Ubuntu22_cuda12.1_v4.0.8.zstd.run
```

You can yes all but if you want to use your own model you can said no to AI module.

## Install ZED camera for environment.

Using conda or dotenv to activate your environment. Run this command for installation code.

```
cd "/usr/local/zed/"
python get_python_api.py
```

Installation code will look like this and you just need to install it like normal pip library installation.

```
pip install --ignore-installed /home/user/pyzed-4.0-cp311-cp311-linux_x86_64.wh
```
