from django.shortcuts import HttpResponse, render
import json
import cv2
import base64

cap = cv2.VideoCapture(0)

def capture_webcam_frame():
    # Open the webcam

    # Capture one frame
    ret, frame = cap.read()

    if ret:
        # Convert the frame to base64
        _, buffer = cv2.imencode('.jpg', frame)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        # Create HTML img tag with the base64-encoded data
        # html_img = f'<img src="data:image/jpeg;base64,{img_base64}" alt="Webcam Image">'
        html_img = f'data:image/jpeg;base64,{img_base64}'
        json_data = json.dumps(html_img)
        # Return the HTML img tag
        return json_data

    # finally:
    #     # Release the webcam
    #     cap.release()


def index(r):
    return render(r, "index.html")

def getFrame(r):
    img = capture_webcam_frame()
    return HttpResponse(img)
