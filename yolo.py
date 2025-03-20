import cv2
from ultralytics import YOLO
import pyttsx3
import time

def start():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 

    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    last_spoken = {}
    cooldown = 5 

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)
        annotated_frame = results[0].plot()
        
        current_objects = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls)
                obj_name = model.names[class_id]
                current_objects.append(obj_name)
        
        unique_objects = list(set(current_objects))
        current_time = time.time()
        
        for obj in unique_objects:
            if current_time - last_spoken.get(obj, 0) > cooldown:
                engine.say(f"{obj} detected")
                engine.runAndWait()
                last_spoken[obj] = current_time
        
        cv2.imshow("Object Detection", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()