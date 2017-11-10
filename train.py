from keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping, CSVLogger
from model import Model
from dataSetModel import DataSetModel
import time
from keras.utils import np_utils
import os

#MODEL_NAME = 'Conv3d'
MODEL_NAME = 'Conv3dBLSTM'
#MODEL_NAME = 'LSTM'
SAVED_MODEL = None
SEQ_LENGTH = 40
IMAGE_SHAPE = (80, 80, 3)

DATA_TYPE = 'Images'
DATA_PATH = './Workspace/'

CHECKPOINT_PATH = DATA_PATH + 'checkpoints/' + MODEL_NAME + '.{epoch:03d}-{val_loss:.3f}.hdf5'

EPOCH_NUMBER = 5
BATCH_SIZE = 10

FEATURE_LENGTH = 4096

def train(concat=False):

    if not os.path.exists(DATA_PATH + 'checkpoints'):
        os.makedirs(DATA_PATH + 'checkpoints')
    # Creating the callbacks
    # 1. Save the model.
    #checkpointer = ModelCheckpoint(filepath=CHECKPOINT_PATH, verbose=1, save_best_only=True)
    checkpointer = ModelCheckpoint(filepath=CHECKPOINT_PATH, monitor='val_acc', verbose=0,
                                 save_best_only=False, save_weights_only=True,
                                 mode='auto', period=1)

    # 2. TensorBoard
    tb = TensorBoard(log_dir=DATA_PATH+'logs')

    # 3. Stop when we stop learning.
    early_stopper = EarlyStopping(patience=100000)

    # 4. Save results to logger.
    timestamp = time.time()

    if not os.path.exists(DATA_PATH + 'logs'):
        os.makedirs(DATA_PATH + 'logs')
    csv_logger = CSVLogger(DATA_PATH + 'logs/' + MODEL_NAME + '-' + 'training-' + str(timestamp) + '.log')

    if IMAGE_SHAPE is None:
        data = DataSetModel(seq_length=SEQ_LENGTH, data_type=DATA_TYPE)
    else:
        data = DataSetModel(seq_length=SEQ_LENGTH, data_type=DATA_TYPE, image_shape=IMAGE_SHAPE)        

    conv3dModel = Model(len(data.classes), MODEL_NAME, SEQ_LENGTH, SAVED_MODEL, FEATURE_LENGTH)

    # Get data.
    X, y = data.LoadSequencesToMemory('Train')
    X_test, y_test = data.LoadSequencesToMemory('Test')
    
    conv3dModel.model.fit(
        X,
        y,
        batch_size=BATCH_SIZE,
        validation_data=(X_test, y_test),
        verbose=1,
        callbacks=[tb, early_stopper, csv_logger, checkpointer],
        epochs=EPOCH_NUMBER)

def main():
    print ("run train script")
    train(concat=False)

if __name__ == '__main__':
    main()