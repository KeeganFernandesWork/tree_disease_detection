import onnxruntime
from PIL import Image
import numpy as np

def model_app(image_path):
    filepath = "model.onnx"
    ort_session = onnxruntime.InferenceSession(filepath)
    input_name = ort_session.get_inputs()[0].name
    ort_inputs = {input_name: np.random.random((1,3,256,256)).astype(np.float32)}
    ort_outs = ort_session.run(None, ort_inputs)
    labels_dict = {
            1:"Apple Scab",
            2:"Apple Black Rot",
            3:"Apple Cedar Rust",
            4:"Apple Cedar Rust",
            5:"Blueberry healthy",
            6:"Cherry healthy",
            7:"Cherry Powdery Mildew",
            8:"Corn Gray Leaf Spot",
            9:"Corn Common Rust",
            10:"Corn healthy",
            11:"Corn Northern Leaf Blight",
            12:"Grape Black Rot",
            13:"Grape Black Measles",
            14:"Grape Healthy",
            15:"Grape Leaf Blight",
            16:"Orange Huanglongbing",
            17:"Peach Bacterial Spot",
            18:"Peach healthy",
            19:"Bell Pepper Bacterial Spot",
            20:"Bell Pepper healthy",
            21:"Potato Early Blight",
            22:"Potato healthy",
            23:"Potato Late Blight",
            24:"Raspberry healthy",
            25:"Soybean healthy",
            26:"Squash Powdery Mildew",
            27:"Strawberry Healthy",
            28:"Tomato Bacterial Spot",
            29:"Tomato Early Blight",
            30:"Tomato Late Blight",
            31:"Tomato Leaf Mold",
            32:"Tomato Septoria Leaf Spot",
            33:"Tomato Two Spotted Spider Mite",
            34:"Tomato Target Spot",
            35:"Tomato Mosaic Virus",
            36:"Tomato Yellow Leaf Curl Virus",
            37:"Tomato healthy"
            }
    img = Image.open(image_path)
    img_a = np.asarray(img).reshape(1,3,256,256).astype(np.float32)
    print(img_a.shape)
    ort_inputs = {input_name: img_a}
    ort_outs = ort_session.run(None, ort_inputs)
    lab = np.argmax(ort_outs[0][0])
    return labels_dict[lab]

