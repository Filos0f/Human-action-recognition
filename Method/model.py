from keras.layers import Dense, Flatten, Dropout, ZeroPadding3D
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import MaxPooling3D, Conv3D
from keras.models import model_from_yaml
from collections import deque
import sys
from keras.preprocessing import image
import numpy as np

from dataSetModel import DataSetModel, GetArrayFromImage
from keras.applications.inception_v3 import InceptionV3, preprocess_input

class Model():
    def __init__(self, classesNumber, modelName, sequenseLength, savedModel=None, featuresLength=2048):
        self.featureQueue = deque()
        self.sequenseLength = sequenseLength
        self.savedModel = savedModel
        self.classesNumber = classesNumber

        if self.savedModel is not None:
            print("Loading model %s" % self.savedModel)
            self.model = load_model(self.savedModel)
        elif modelName == 'Conv3d':
            print("Loading Conv3d model")
            self.shapeOfInput = (sequenseLength, 80, 80, 3)
            self.model = self.Conv3DModelCreate()
        elif modelName == 'LSTM' :
            print("Loading LSTM model")
            self.shapeOfInput = (sequenseLength, featuresLength)
            self.model = self.LSTMModelCreate()
        else:
            print("Unknown network model.")
            sys.exit()

        metrics = ['accuracy']
        if self.classesNumber >= 10:
            metrics.append('top_k_categorical_accuracy')

        optimizer = Adam(lr=1e-4, decay=1e-6)

        self.model.compile(loss='binary_crossentropy', optimizer=optimizer,
                           metrics=metrics)

        #print(self.model.summary())

    def Conv3DModelCreate(self):
        # According to https://gist.github.com/albertomontesg/d8b21a179c1e6cca0480ebdf292c34d2

        model = Sequential()
        # 1st layer group
        model.add(Conv3D(64, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv1',
                                subsample=(1, 1, 1), 
                                input_shape=self.shapeOfInput)) # 40 80 80 3
        model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2), 
                               border_mode='valid', name='pool1'))
        # 2nd layer group
        model.add(Conv3D(128, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv2',
                                subsample=(1, 1, 1)))
        model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), 
                               border_mode='valid', name='pool2'))
        # 3rd layer group
        model.add(Conv3D(256, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv3a',
                                subsample=(1, 1, 1)))
        model.add(Conv3D(256, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv3b',
                                subsample=(1, 1, 1)))
        model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), 
                               border_mode='valid', name='pool3'))
        # 4th layer group
        model.add(Conv3D(512, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv4a',
                                subsample=(1, 1, 1)))
        model.add(Conv3D(512, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv4b',
                                subsample=(1, 1, 1)))
        model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), 
                               border_mode='valid', name='pool4'))
        # 5th layer group
        model.add(Conv3D(512, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv5a',
                                subsample=(1, 1, 1)))
        model.add(Conv3D(512, 3, 3, 3, activation='relu', 
                                border_mode='same', name='conv5b',
                                subsample=(1, 1, 1)))
        model.add(ZeroPadding3D(padding=(0, 1, 1)))
        model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), 
                               border_mode='valid', name='pool5'))
        model.add(Flatten())
        # FC layers group
        model.add(Dense(4096, activation='relu', name='fc6'))
        model.add(Dropout(.5))
        model.add(Dense(4096, activation='relu', name='fc7'))
        model.add(Dropout(.5))
        model.add(Dense(20, activation='softmax', name='fc8'))

        return model

    def LSTMModelCreate(self):
        # Simple LSTM model
        model = Sequential()
        model.add(LSTM(2048, return_sequences=True, input_shape=self.shapeOfInput,
                       dropout=0.5))
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(self.classesNumber, activation='softmax'))

        return model

    def LoadWeigths(self, weights_path=None) :
        if weights_path is not None :
            self.model.load_weights(weights_path)
        else :
            print("Error: Can not load the weigths!\n")

    def MakeModelForExtructiongFeatures(self) :
        self.model.layers.pop()
        self.model.layers.pop()  # two pops to get to pool layer
        self.model.outputs = [self.model.layers[-1].output]
        self.model.output_layers = [self.model.layers[-1]]
        self.model.layers[-1].outbound_nodes = [] 
        

    def SaveModelYaml(self, modelPath="./Data") :
        model_yaml = self.model.to_yaml()
        with open(modelPath + "/model.yaml", "w") as yaml_file:
            yaml_file.write(model_yaml)

    def ExtractFeaturesFromImage(self, x):
        features = self.model.predict(x)
        print(features)
        features = features[0]

        return features