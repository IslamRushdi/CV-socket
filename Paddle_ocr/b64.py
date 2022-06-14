import base64
from io import BytesIO
from PIL import Image

def base64_pil(base64_str:str)->Image:
  image = base64.b64decode(base64_str)
  image = BytesIO(image)
  image = Image.open(image)
  return image.rotate(-90)

# def image_to_base64(file_name:str)->str:
#     with open(file_name , "rb") as image_file :
#         data = base64.b64encode(image_file.read())
#     return data.decode('utf-8')