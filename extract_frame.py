import cv2
vidcap = cv2.VideoCapture("/ws/data/IMX477_E15.mp4")
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("/ws/data/IMX477_E15_extracted_frame/3.1.1."+"%d.jpg" %count, image)
    success, image = vidcap.read()
    print("Read a new frame", success)
    count += 1

