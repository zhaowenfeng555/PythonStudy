# cv 加载： https://blog.csdn.net/qq_41185868/article/details/79675875
# 1、PIL.Image转换成OpenCV格式：
import cv2
from PIL import Image
import numpy as np

path = '/Users/zhaowenfeng/git/MachineLearn/WZH/KMeans/1.jpg'
# .convert("RGB")可不要，默认打开就是RGB
img = Image.open(path).convert("RGB")
img.show()
# 转opencv
# img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
# np.array(PIL.Image.open(path)).shape ==  cv2.imread(path).shape
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV",img)
cv2.waitKey()

# 2、OpenCV转换成PIL.Image格式
import cv2
from PIL import Image
import numpy as np

path = '/Users/zhaowenfeng/git/MachineLearn/WZH/KMeans/1.jpg'
# opencv打开的是BRG
img = cv2.imread(path)
cv2.imshow("OpenCV", img)
image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
image.show()
cv2.waitKey()