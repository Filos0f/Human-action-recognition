SET FFMPEG_PATH=/c/Git_Projects2/Human-action-recognition/requirements/ffmpeg.exe
SET INPUT_FILE=/c/Git_Projects2/Human-action-recognition/Train/answering questions/_5PV4fkZisA_000139_000149.mp4
SET OUTPUT=/c/Git_Projects2/Human-action-recognition/workspace/data/Test/questions-%04d.jpg

%FFMPEG_PATH% -i %INPUT_FILE% -vframes 10 %OUTPUT%
