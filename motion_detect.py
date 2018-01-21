import cv2
import datetime

cap = cv2.VideoCapture(0)

four_cc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', four_cc, 20.0, (640, 480))
ret, frame0_color = cap.read()

while cap.isOpened():

    ret, frame1_color = cap.read()
    frame0_gray = cv2.cvtColor(frame0_color, cv2.COLOR_RGB2GRAY)
    frame1_gray = cv2.cvtColor(frame1_color, cv2.COLOR_RGB2GRAY)
    frame_gray_diff = cv2.absdiff(frame0_gray, frame1_gray)
    frame_gray_thresholded = cv2.threshold(frame_gray_diff, 55, 255, cv2.THRESH_BINARY)[1]

    if frame_gray_thresholded.sum(0).sum(0) > 0:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame0_color, datetime.datetime.now().strftime("%I:%M:%S%p %B %d, %Y"),
                    (10, 50), font, 1, (255, 255, 255), 2)
        out.write(frame0_color)
        cv2.imshow('frame', frame_gray_thresholded)

        frame0_color = frame1_color
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
