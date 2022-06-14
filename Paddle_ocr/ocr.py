from paddleocr import PaddleOCR
# from b64 import base64_pil
import os
import numpy as np
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
def get_words(X):
    ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
    # img_path = 'C:/Graduation_project/Graduation-project/Python/Paddle-ocr/imgs_en/ascsac.jpg'
    X = np.array(X)
    result = ocr.ocr(X, cls=True)
    txts = [line[1][0] for line in result if line[1][1] > 0.8]
    return txts


# # draw result
# from PIL import Image
# import matplotlib.pyplot as plt
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# # im_show = Image.fromarray(im_show)
# # im_show.save('result.jpg')
# plt.imshow(im_show)
# plt.axis('off')
# plt.show()