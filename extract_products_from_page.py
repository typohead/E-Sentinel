from ultralytics import YOLO
from PIL import Image
import json
# import json
# print(torch.cuda.is_available())

def extract_products(image,model_path="../runs/detect/train/weights/best.pt", confidence=0.5):
    model = YOLO(model_path)
    # image=cv2.imread('screenshot_page_4.png')
    # model.train(data='data\data.yaml',epochs=2)
    # width,height=image.shape[:2]
    # print(width,height)
    results=model.predict(image,conf=confidence)
    results_json= {}
    for r in results:
        # print(r.orig_shape)
        result_items_str=r.tojson() #returns a json string , need to convert it into json
        result_items_json=json.loads(result_items_str)
        #print(result_items_json)
        #print(type(result_items_json))     # print(results_json_string)
        # im_array = r.plot(line_width=1)  # plot a BGR numpy array of predictions
        # im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        # im.show()  # show image
        # im.save('result.png')
    return result_items_json

# results=extract_products(image='D:\dark_pattern_hackathon\Code\screenshot_page_4.png',confidence=0.5)
# print(results)