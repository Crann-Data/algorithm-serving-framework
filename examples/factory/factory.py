import torchvision
from algorithm_factory.factory import ObjectDetector
from PIL import Image

if __name__ == "__main__":
    image = Image.open("test/test-image.jpg")
    image = image.convert('RGB')
    image = image.resize((1920, 1080))

    convert_to_tensor = torchvision.transforms.ToTensor()
    image = convert_to_tensor(image)

    image = image.unsqueeze(0)
    image = image.to(device="cuda")

    od = ObjectDetector("testing", image, "test/")