import pyzed.sl as sl
import numpy
import cv2


def setup(verbose=True):
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.VGA
    init_params.camera_fps = 30
    if verbose:
        init_params.sdk_verbose = 1 
    else:
        init_params.sdk_verbose = 0

    # Open the camera
    err = zed.open(init_params)
    if verbose:
        if err != sl.ERROR_CODE.SUCCESS:
            print("Camera Open : "+repr(err)+". Exit program.")
            exit()
    return zed

def close(zed):
    zed.close()

def get_image(zed, normal=True, verbose=True):
    image = sl.Mat()
    runtime_parameters = sl.RuntimeParameters()
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        # A new image is available if grab() returns SUCCESS
        zed.retrieve_image(image, sl.VIEW.LEFT)
        timestamp = zed.get_timestamp(sl.TIME_REFERENCE.CURRENT)  # Get the timestamp at the time the image was captured
        if verbose:
            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(),
                timestamp.get_milliseconds()))
        a = image.get_data()
        if verbose:
            cv2.imshow('img', a)
            cv2.waitKey(1)
    if normal:
        return a

if __name__ == "__main__":
    zed = setup(verbose=False)
    img = get_image(zed, verbose=False)
    cv2.imshow('a', img)
    cv2.waitKey(0)
    close(zed)
