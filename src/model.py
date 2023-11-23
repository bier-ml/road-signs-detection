import torch
from PIL import Image
import requests
import io


class RoadSignsDetectionProcessor:
    def __init__(self, image):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='../models/best.pt')
        self.image = image

    def process(self):
        results = self.model([self.image], size=640)
        results.print()
        results.show()

        print(results)


if __name__ == "__main__":
    url = 'https://ultralytics.com/images/zidane.jpg'
    r = requests.get('https://ultralytics.com/images/zidane.jpg', stream=True)

    img = Image.open(io.BytesIO(r.content))
    p = RoadSignsDetectionProcessor(img)
    p.process()