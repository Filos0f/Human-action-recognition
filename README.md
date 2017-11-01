# Human-action-recognition

Example of using

1. Run the script downloadYouTubeVideo.py for getting video from YouTube
The all videos will be placed at folder ./Videos around the script
The video will be divided by two folders ./Train/ActionName and ./Test/ActionName

Note! If you want to add video by hand you should create folders ./Train/ActionName and ./Test/ActionName in ./Video folder and move here video clips.

2. Run script splitVideoByFrames.py from ./Method/Data after script finished, the frames will be appeared around the file.

3. Specify in train.py parameter MODEL_NAME = "Conv3d" and DATA_TYPE = 'Images', and create folder ./Data/checkpoints than run train.py
After script will finished the saved model will be in ./Data/checkpoints

4. Create ./Data/sequances and run extractFeaturesByConv3d.py , after script will finished the files with features will be saved at folder ./Data/sequances 

5. Specify in train.py parameter MODEL_NAME = "LSTM" and DATA_TYPE = 'Features' than run train.py , saved model in .hdf5 format will be at ./Data/checkpoints 

6. You can test the work of the Conv3d + LSTM combinations by running the testModel.py