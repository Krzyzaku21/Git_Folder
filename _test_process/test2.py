from urllib.request import urlopen
from PIL import Image

img = Image.open(urlopen('https://kpbs.media.clients.ellingtoncms.com/img/photos/2019/04/25/AP_19115564116496_t800.jpg'))
img