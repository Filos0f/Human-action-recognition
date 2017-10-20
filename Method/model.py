from keras.layers import Dense, Flatten, Dropout
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.layers.convolutional import MaxPooling3D, Conv3D
from keras.models import model_from_yaml
from collections import deque
import sys

class Model():
    def __init__(self, classesNumber, sequenseLength, savedModel=None):
        self.featureQueue = deque()
        self.sequenseLength = sequenseLength
        self.saved_model = savedModel
        self.classesNumber = classesNumber

        if self.savedModel is not None:
            print("Loading model %s" % self.savedModel)
            self.model = load_model(self.savedModel)
        elif model == 'Conv3d':
            print("Loading Conv3d model")
            self.shapeOfInput = (sequenseLength, 80, 80, 3)
            self.model = self.Conv3DModelCreate()
        else:
            print("Unknown network model.")
            sys.exit()

        metrics = ['accuracy']
        if self.classesNumber >= 10:
            metrics.append('top_k_categorical_accuracy')

        optimizer = Adam(lr=1e-4, decay=1e-6)

        self.model.compile(loss='binary_crossentropy', optimizer=optimizer,
                           metrics=metrics)

        print(self.model.summary())

    def Conv3DModelCreate(self):
        # According to https://gist.github.com/albertomontesg/d8b21a179c1e6cca0480ebdf292c34d2

        model = Sequential()

        model.add(Conv3D(32, (3,3,3), activation='relu', input_shape=self.shapeOfInput))
        model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2)))
        model.add(Conv3D(64, (3,3,3), activation='relu'))
        model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2)))
        model.add(Conv3D(128, (3,3,3), activation='relu'))
        model.add(Conv3D(128, (3,3,3), activation='relu'))
        model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2)))
        model.add(Conv3D(256, (2,2,2), activation='relu'))
        model.add(Conv3D(256, (2,2,2), activation='relu'))
        model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2)))

        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Dropout(0.5))
        model.add(Dense(1024))
        model.add(Dropout(0.5))
        model.add(Dense(self.nb_classes, activation='softmax'))

        return model

    def LoadWeigths(self, weights_path=None) :
        if weights_path is not None :
            self.model.load_weights(weights_path)
        else :
            print("Error: Can not load the weigths!\n")
        

    def SaveModelYaml(self, modelPath="./Data") :
        model_yaml = self.model.to_yaml()
        with open(modelPath + "/model.yaml", "w") as yaml_file:
            yaml_file.write(model_yaml)
