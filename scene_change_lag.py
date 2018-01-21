import cv2
import numpy

frameWidth = 640
frameHeight = 360

max_index = 256

cap = cv2.VideoCapture('C:\\Users\\shudson\\Dropbox\\Movie.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:\\Users\\shudson\\Dropbox\\Movie_NoMotion.mp4', fourcc, 30.0, (640, 360))

histo = [[[0 for k in range(max_index)] for j in range(frameHeight)] for i in range(frameWidth)]
index = 0
count = 0

while cap.isOpened():
    frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', frame)

    print('frame=%d' % count)
    count += 1

    for x in range(frameWidth):
        for y in range(frameHeight):
            pelValue = frame[y][x]
            histo[x][y][index] = pelValue
            frame[y][x] = int(numpy.median(histo[x][y]))

    index += 1
    if index >= max_index:
        index = 0

    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    cv2.imshow('processed', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count > 5120:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
