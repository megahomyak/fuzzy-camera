import cv2, PySimpleGUI as sg, numpy as np
window = sg.Window('fuzzy camera', [[sg.Image(filename='', key='image')]], size=(800, 800), resizable=True)
cap = cv2.VideoCapture(0)
while window(timeout=20)[0] is not None:
    frame = cap.read()[1]
    lightness = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    activation_mask = lightness > np.random.randint(0, 255, size=lightness.shape, dtype=np.uint8)
    frame[:] = 0
    frame[activation_mask] = 255
    window['image'](data=cv2.imencode('.png', frame)[1].tobytes())
