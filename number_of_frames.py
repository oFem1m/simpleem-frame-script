from cv2 import cv2


def number_of_frames(path):
    cap = cv2.VideoCapture(path)
    frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frames += 1
        else:
            break
    return frames
