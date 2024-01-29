'''
actions : 
    1. Take screenshot image using the functions in screenshot file
    2. supply this screen shot to extract_products_from_page file functions 
        they extract the bounding boxes of various elements of interest 
        they return a json with each entry having class name , bounding boxes 
    3. Use OCR model to extract the text from the bounding boxes
        - traverse the json , append the necessary data extracted from the bouding box 
          into the same entry
        - ex : a product class elment with bounding boxes will get additional info 
            and results in :
               {
                'class' : 'product'
                'boxes' : xxxx
                'product_name': name
                'brand': abc
                }
        the extra information appended will change depending upon the type of product 
        or element ( ads, bannder , etc)
    4. the new generated json then can be used for analysis or anything else

'''
from page_screenshot import screenshot_fullpage 
from extract_products_from_page import extract_products
import pytesseract
import cv2
import numpy as np
import easyocr
from PIL import Image
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS


url="https://www.flipkart.com/home-furnishing/kitchen-table-linen/table-linen-sets/pr?sid=jra%2Ciwp%2Ctg1&hpid=Kfbq-0RJUqi4GsncVG4D86p7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTk5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiVExTRzc3MkVOQVdYUUdTRyIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlRhYmxlIExpbmVuIFNldHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19"

        


app = Flask(__name__)
CORS(app)

@app.route('/')
def display():
    return render_template('index.html')


@app.route('/submit',methods=['POST','GET']) 
def urlsubmitted():
    data = request.json
    page_url = data.get('url')
    # Process the data (you can customize this part based on your needs)
    image=screenshot_fullpage(page_url)
    # image.show()

    elements_json= extract_products(image=image,model_path='../runs/detect/train/weights/best.pt') 
    # print(elements_json)
    reader = easyocr.Reader(['en'])
    # img = cv2.imread("D:\dark_pattern_hackathon\Code\production\k.png")
    element_details=[]
    index=1
    for element in elements_json:
        x1,y1,x2,y2=element['box'].values()
        region_of_interest = image.crop((x1, y1, x2, y2))
        
        np_image = np.array(region_of_interest)
        # # Convert RGB to BGR (OpenCV uses BGR)
        gray_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2GRAY)
        text = pytesseract.image_to_string(gray_image)
        # print(text)
        element_details.append(text)
        # cv2.imshow("product",gray_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # Return a JSON response
    return jsonify(element_details), 200


if __name__ == '__main__':
    # Run the Flask app on http://127.0.0.1:5000/
    app.run(debug=True)












