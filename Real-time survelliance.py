from ultralytics import YOLO

# Load YOLO-World model
model = YOLO("yolo12s.pt")  

# Run tracking on webcam with 720p resolution
results = model.track(
    source=0,         # Default webcam
    show=True,
    imgsz=720         # Sets input image size to 720p (height or width, auto scales)
)