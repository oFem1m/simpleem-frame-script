from cv2 import cv2
import os
import number_of_frames as nof


def screenshots(person_name, emotion):
    # get full_name of file
    full_name = person_name + '.mp4'
    # get path
    path = r'data\{0}\{1}'.format(emotion, full_name)
    cap = cv2.VideoCapture(path)
    # we find such a frame rate to take about 50 screenshots
    freq = nof.number_of_frames(path) // 50
    currentframe = 0
    
    # create a new folder <emotion>_img where we will store the resulting screenshots
    emotion_img_dir = emotion + '_img'
    if not os.path.exists(r'data\{0}'.format(emotion_img_dir)):
        os.makedirs(r'data\{0}'.format(emotion_img_dir))

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # if video is still left continue creating images
            if currentframe % freq == 0:
                name = os.path.join(r'data\{0}'.format(emotion_img_dir), person_name + '(' + str(currentframe//6) + ')' + '.jpg')
                print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
        if not cv2.waitKey(1):
            break

    # Release all space and windows once done
    cap.release()
    cv2.destroyAllWindows()
