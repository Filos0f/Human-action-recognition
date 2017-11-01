from keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping, CSVLogger
from model import Model
from dataSetModel import DataSetModel
import time
from keras.utils import np_utils

MODEL_NAME = 'Conv3d'
SAVED_MODEL = None
SEQ_LENGTH = 40
IMAGE_SHAPE = (80, 80, 3)

DATA_TYPE = 'Images'
DATA_PATH = './Data/'

CHECKPOINT_PATH = DATA_PATH + 'checkpoints/' + MODEL_NAME + '.{epoch:03d}-{val_loss:.3f}.hdf5'

EPOCH_NUMBER = 5
BATCH_SIZE = 32

def train(concat=False):
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
    csv_logger = CSVLogger(DATA_PATH+'logs/' + MODEL_NAME + '-' + 'training-' + str(timestamp) + '.log')

    if IMAGE_SHAPE is None:
        data = DataSetModel(seq_length=SEQ_LENGTH, data_type=DATA_TYPE)
    else:
        data = DataSetModel(seq_length=SEQ_LENGTH, data_type=DATA_TYPE, image_shape=IMAGE_SHAPE)        

    conv3dModel = Model(len(data.classes), MODEL_NAME, SEQ_LENGTH, SAVED_MODEL)

    # Get data.
    X, y = data.LoadSequencesToMemory('Train')
    X_test, y_test = data.LoadSequencesToMemory('Test')

    y = np_utils.to_categorical(y, 20)
    y_test = np_utils.to_categorical(y_test, 20)

    print(X.shape)
    print(y.shape)
    return
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