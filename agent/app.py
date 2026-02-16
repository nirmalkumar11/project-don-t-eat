from agent import start
from paddleocr import PaddleOCR
import cv2 as cv

cam=cv.VideoCapture(0)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

ok=False
while True:
    ret, frame = cam.read()
    cv.imshow("press q to capture", frame)

    key = cv.waitKey(1) & 0xFF  # Only ONE waitKey call

    if key == ord('q'):
        captured_frame = frame.copy()
        cv.imshow('press "o" to accept OR "n" to reject', captured_frame)

        # Wait for the user's decision
        while True:
            key2 = cv.waitKey(0) & 0xFF

            if key2 == ord('n'):      # Reject
                cv.destroyWindow('press "o" to accept OR "n" to reject')
                ok=False
                break  # Go back to camera loop

            if key2 == ord('o'):      # Accept
                ok=True
                cv.destroyWindow('press "o" to accept OR "n" to reject')
                cv.destroyWindow('press q to capture')
                break  # Exit entire program
        if ok:
            break 
cam.release()
cv.destroyAllWindows()

result = ocr.predict(captured_frame)
a=" ".join(result[0]['rec_texts'])
res=start(a)
print(res)
#deactivate cd donot_eat/agent python3 app.py
