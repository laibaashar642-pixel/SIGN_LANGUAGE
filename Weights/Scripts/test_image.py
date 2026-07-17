from ultralytics import YOLO

model = YOLO("Weights/best_sign.pt")
results = model.predict(source="images (1).jpg", conf=0.1)
print(results[0].boxes)