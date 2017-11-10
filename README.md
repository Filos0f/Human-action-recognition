# Human-action-recognition

Example of using

1. Run the script ./Utils/downloadFromYouTube.py for getting video from YouTube
You need to specify cvs dataset file and folder where you want to save video. For instance:
python download.py {dataset_split}.csv <data_dir> 

2. Run script splitVideoByFrames.py from ./Utils after script finished, the frames will be appeared around the video files.
Moreover the file with information about how many frames were extructed for each videos will be saved in 
./Workspace/FilesData.csv

3. Specify in train.py parameter MODEL_NAME = "Conv3d" and DATA_TYPE = 'Images', and create folder ./Data/checkpoints than run train.py
After script will finished the saved model will be in ./Data/checkpoints

4. Create ./Data/sequances and run extractFeaturesByConv3d.py , after script will finished the files with features will be saved at folder ./Data/sequances 

5. Specify in train.py parameter MODEL_NAME = "LSTM" and DATA_TYPE = 'Features' than run train.py , saved model in .hdf5 format will be at ./Data/checkpoints 

6. You can test the work of the Conv3d + LSTM combinations by running the testModel.py


Utils

caclulateNumberOfVideosForEachAction.py

divideDataset.py