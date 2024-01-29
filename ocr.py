import cv2 
import pytesseract

img = cv2.imread("D:\dark_pattern_hackathon\Code\production\k.png")
# cv2.imshow("abc",img)
# cv2.waitKey(0)
# cv2.distroyAllWindows()
# Adding custom options
# custom_config = r'--oem 3 --psm 6'
string=pytesseract.image_to_string(img)
print(string)