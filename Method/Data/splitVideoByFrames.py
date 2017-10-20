import csv
import glob
import os
import os.path
from subprocess import call

PATH_TO_FFMPEG = "D:/ffmpeg-20170921-183fd30-win64-static/bin/ffmpeg"

EXTENSION_OF_OUTPUT_FRAME = '.jpg'
EXTENSION_OF_INPUT_VIDEO = '.avi'
TRAIN_VIDEO_FOLDER = '../../Videos/Train/' #'./train/'
TESTING_VIDEO_FOLDER = '../../Videos/Test/'
TRAIN_FRAMES_FOLDER = './train/'
TEST_FRAMES_FOLDER = './test/'

def ExtractFrames():
    # Checking whether the folder exists, create othervise
    if not os.path.exists(TRAIN_FRAMES_FOLDER):
        os.makedirs(TRAIN_FRAMES_FOLDER)
    if not os.path.exists(TEST_FRAMES_FOLDER):
        os.makedirs(TEST_FRAMES_FOLDER)

    dataFiles = []
        
    ProcessThePath(TRAIN_VIDEO_FOLDER, dataFiles)
    ProcessThePath(TESTING_VIDEO_FOLDER, dataFiles)

    with open('./FilesData.csv', 'w') as fout:
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
                src = lableOfDataType + '/' + className + '/' + \
                    fileNameWithExtension
                dest = lableOfDataType + '/' + className + '/' + \
                    fileName + '-%04d'+EXTENSION_OF_OUTPUT_FRAME
                print(src)
                print(dest)
                call([PATH_TO_FFMPEG, "-i", src, dest])

            # Now get how many frames it is.
            framesCount = NumberOfFrames(videoInfo)

            dataFiles.append([lableOfDataType, className, fileName, framesCount])

            print("Generated %d frames for %s" % (framesCount, fileName))

def NumberOfFrames(videoInfo):
    lableOfDataType, className, fileName, _ = videoInfo
    generated_files = glob.glob(lableOfDataType + '/' + className + '/' +
                                fileName + '*.jpg')
    return len(generated_files)

def SplitVideoPath(path):
    parts = path.split('\\')
    fileNameWithExtension = parts[2]
    fileName = fileNameWithExtension.split('.')[0]
    className = parts[1]
    # Lable Train or Test
    lableOfDataType = parts[0]
    print(lableOfDataType)
    return lableOfDataType, className, fileName, fileNameWithExtension

def CheckTheFrameAlreadyExtracted(videoInfo):
    lableOfDataType, className, fileName, _ = videoInfo
    return bool(os.path.exists(lableOfDataType + '/' + className +
                               '/' + fileName + '-0001.jpg'))

def main():
    ExtractFrames()

if __name__ == '__main__':
    main()
