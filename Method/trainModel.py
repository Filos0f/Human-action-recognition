from keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping, CSVLogger
from model import Model
from dataSetModel import DataSetModel
import time

MODEL_NAME = "Conv3d"
SAVED_MODEL = None
SEQ_LENGTH = 40
IMAGE_SHAPE = (80, 80, 3)

DATA_PATH = './Data/'

CHECKPOINT_PATH = DATA_PATH + 'checkpoints/' + MODEL_NAME + '.{epoch:03d}-{val_loss:.3f}.hdf5'

EPOCH_NUMBER = 2
BATCH_SIZE = 32

def train(concat=False):
    # Creating the callbacks

    # 1. Save the model.
    checkpointer = ModelCheckpoint(filepath=CHECKPOINT_PATH, verbose=1, save_best_only=True)

    # 2. TensorBoard
    tb = TensorBoard(log_dir=DATA_PATH+'logs')

    # 3. Stop when we stop learning.
    early_stopper = EarlyStopping(patience=100000)

    # 4. Save results to logger.
    timestamp = time.time()
    csv_logger = CSVLogger(DATA_PATH+'logs/' + MODEL_NAME + '-' + 'training-' + str(timestamp) + '.log')

    if IMAGE_SHAPE is None:
        data = DataSetModel(seq_length=SEQ_LENGTH)
    else:
        data = DataSetModel(seq_length=SEQ_LENGTH, image_shape=IMAGE_SHAPE)        

    conv2dModel = Model(len(data.classes), MODEL_NAME, SEQ_LENGTH, SAVED_MODEL)

    # Get data.
    X, y = data.LoadSequencesToMemory('train', DATA_TYPE, concat)
    X_test, y_test = data.LoadSequencesToMemory('test', DATA_TYPE, concat)

    conv2dModel.model.fit(
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