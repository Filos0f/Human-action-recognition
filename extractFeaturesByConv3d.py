from model import Model
from dataSetModel import DataSetModel, GetArrayFromImage
from tqdm import tqdm
import os
import os.path
import glob
import numpy as np
from keras import backend as K
from keras.models import Model as KModel

SEQ_LENGTH = 20
IMAGE_SHAPE = (80, 80, 3)
MODEL_NAME_FOR_EXTRUCTION = 'Conv3d'
SAVED_MODEL = "./Workspace/checkpoints/Conv3d.002-0.196.hdf5"

def extructFeatures() :
    # Get the dataset.
    data = DataSetModel(seq_length=SEQ_LENGTH, image_shape=IMAGE_SHAPE)

    conv3dModel = Model(len(data.classes), MODEL_NAME_FOR_EXTRUCTION, SEQ_LENGTH, None)
    conv3dModel.LoadWeigths(SAVED_MODEL)

    intermediate_layer_model = KModel(inputs=conv3dModel.model.layers[0].input,
                                 outputs=conv3dModel.model.get_layer('fc6').output)

    pbar = tqdm(total=len(data.data))
    for video in data.data:
        # Get the path to the sequence for this video.
        path = './Workspace/sequences/' + video[2] + '-' + str(SEQ_LENGTH) + '-Features.txt'
        
        if os.path.isfile(path):
            pbar.update(1)
            continue

        frames = DataSetModel.GetFramesFromSample(video)
        img_arr = [GetArrayFromImage(x, IMAGE_SHAPE) for x in frames]
        x = []
        start = 0
        end = SEQ_LENGTH
        for _ in range(len(img_arr) // SEQ_LENGTH) :
            x.append(img_arr[start : end])
            start = end
            end = end + SEQ_LENGTH

        x = np.array(x)

        sequence = intermediate_layer_model.predict(x)

        # Save the sequence.
        np.savetxt(path, sequence)
        pbar.update(1)
    pbar.close()

extructFeatures()