from io import BytesIO
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR
from b64 import base64_pil
# from img import img_base64
import base64

ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory


def recognize(img_base64):
    # img_path = './imgs_en/img_12.png'

    image = base64_pil(img_base64)
    image = np.array(image.convert('RGB'))

    result = ocr.ocr(image, cls=True)
    # for line in result:
    #   print(line)

    image = Image.open(BytesIO(base64.b64decode(img_base64)))
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]

    print(txts)

    return result


  # recognize(img_base64)


# if __name__ == "__main__":
#     main()