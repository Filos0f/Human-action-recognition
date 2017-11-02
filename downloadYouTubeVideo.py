from pytube import YouTube
from subprocess import call
import csv
import os
import re

PATH_TO_SAVE = 'C:/Git_Projects2/Human-action-recognition/Videos/Kinetics'
PATH_TO_DATASET = 'E:/Innopolis/Diploma/DeepMind/kinetics_train/kinetics_train/'
DATASET_NAME = 'kinetics_train.csv'
EXTENSION = '.mp4'

def download_one_video(save_path, url='https://www.youtube.com/watch?v=-l35Ml9PLUE') :
	yt = YouTube(url).streams.filter(subtype='mp4', progressive=False).first().download(save_path)
	return YouTube(url).title

def download_all_video() :

	with open(PATH_TO_DATASET+DATASET_NAME, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		idx = 0
		prev_lable = ' '
		for row in spamreader:
			if row[0] == 'label' :
				continue

			if prev_lable != row[0] :
				idx = 0
			# 1. check lable and create dir if its need
			current_directory = PATH_TO_SAVE + '/' + row[0]
			if not os.path.exists(current_directory):
				os.makedirs(current_directory)

			# 2. download video
			file_name = download_one_video(current_directory, 'https://www.youtube.com/watch?v=' + row[1])

			# 3. prepare new name for video
			file_name = re.sub('[!@#$/:,]', '', file_name)
			re.sub(' +',' ',file_name)
			file_name = file_name + EXTENSION
			old_file_name = current_directory + '/' + file_name
			new_file_name = current_directory + '/' + row[0] + '_' + str(idx) + EXTENSION

			# 4. cut downloaded file
			t_start = float(row[2])
			t_end = float(row[3])

			path_to_ffmpeg = "C:/Git_Projects2/Human-action-recognition/Method/Requariments/ffmpeg.exe"
			cmd = [path_to_ffmpeg,
			"-y", 
			"-i", old_file_name,
			"-ss", "%0.2f"%t_start,
			"-t", "%0.2f"%(t_end-t_start),
			"-vcodec", "copy", "-acodec", "copy", new_file_name]
			call(cmd)

			# 5. delete old video
			os.remove(old_file_name)

			prev_lable = row[0]
			idx = idx + 1


download_all_video()
