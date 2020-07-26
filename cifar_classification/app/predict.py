from tensorflow import keras
import numpy as np

model = keras.models.load_model('cifar_model.h5')

look_up=['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

def predict_image(img):
    onehot = model.predict(img/255)[0]
    no = np.argmax(onehot)
    prob = onehot[no]*100
    return f"{look_up[no]} | Confidence: {prob:.2f}"
