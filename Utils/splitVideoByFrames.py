import csv
import glob
import os
import os.path
from subprocess import call

#PATH_TO_FFMPEG = "ffmpeg"
PATH_TO_FFMPEG = "./requirements/ffmpeg.exe"
#PATH_TO_FFMPEG = "../requirements/ffmpeg/bin/ffmpeg.exe"

EXTENSION_OF_OUTPUT_FRAME = '.jpg'
EXTENSION_OF_INPUT_VIDEO = '.mp4'
TRAIN_VIDEO_FOLDER = './Train/'
TESTING_VIDEO_FOLDER = './Validation/'

WORKER_DIR = './workspace'

os.chdir("../")

def ExtractFrames():
    if not os.path.exists(WORKER_DIR):
        os.makedirs(WORKER_DIR)

    dataFiles = []
        
    ProcessThePath(TRAIN_VIDEO_FOLDER, dataFiles)
    ProcessThePath(TESTING_VIDEO_FOLDER, dataFiles)

    with open(WORKER_DIR + '/FilesData.csv', 'w') as fout:
        writer = csv.writer(fout)
        writer.writerows(dataFiles)

    print("Frames were extracted from %d video files." % (len(dataFiles)))

def ProcessThePath(folder, dataFiles) :
    # Getting the folders names which should be named like a name of class action
    foldersClasses = glob.glob(folder + '*')

    for actionClassFolder in foldersClasses:
        # Getting the list of videos from one folder

        filesForOneActionClass = glob.glob(actionClassFolder + '/*' + EXTENSION_OF_INPUT_VIDEO)
        for pathOfVideo in filesForOneActionClass:
            # Getting the frames from video
            videoInfo = SplitVideoPath(pathOfVideo)

            lableOfDataType, className, fileName, fileNameWithExtension = videoInfo
            if not CheckTheFrameAlreadyExtracted(videoInfo):
                src = os.getcwd() + '/' + lableOfDataType + '/' + className + '/' + \
                    fileNameWithExtension
                dest = os.getcwd() + '/' + lableOfDataType + '/' + className + '/' + \
                    fileName + '-%04d'+EXTENSION_OF_OUTPUT_FRAME
                print(src)
                print(dest)
                print(PATH_TO_FFMPEG)
                command = [PATH_TO_FFMPEG,
                        '-i', src,
                        '-vframes', '100',
                        #'-vf', 'fps=1/0.5',
                        dest]
                call(command)
                

            # Now get how many frames it is.
            framesCount = NumberOfFrames(videoInfo)
            dataFiles.append([lableOfDataType, className, fileName, framesCount])

            print("Generated %d frames for %s" % (framesCount, fileName))

def NumberOfFrames(videoInfo):
    lableOfDataType, className, fileName, _ = videoInfo
    generated_files = glob.glob('./' + lableOfDataType + '/' + className + '/' +
                                fileName + '*.jpg')
    return len(generated_files)

def SplitVideoPath(path):
    parts = path.split('\\')
    if len(parts) == 1 :
        parts = path.split('/')
        fileNameWithExtension = parts[3]
        className = parts[2]
        lableOfDataType = parts[1]
    else :
        fileNameWithExtension = parts[2]
        className = parts[1]
        lableOfDataType = parts[0][2 : len(parts[0])]
    fileName = fileNameWithExtension.split('.')[0]
    return lableOfDataType, className, fileName, fileNameWithExtension

def CheckTheFrameAlreadyExtracted(videoInfo):
    lableOfDataType, className, fileName, _ = videoInfo
    return bool(os.path.exists('./' + lableOfDataType + '/' + className +
                               '/' + fileName + '-0001.jpg'))

def main():
    ExtractFrames()

if __name__ == '__main__':
    main()
