import json
from pprint import pprint

initPath = "E:\\Innopolis\\Diploma\\DeepMind\\Scripts\\kinetics_train.json"

outPathForWellData = "E:\\Innopolis\\Diploma\\DeepMind\\Scripts\\highAccuracyDataset.json"
outPathForBadData = "E:\\Innopolis\\Diploma\\DeepMind\\Scripts\\lowAccuracyDataset.json"

with open(initPath) as data_file:    
    data = json.load(data_file)

wellData = {}
badData = {}

for key, value in data.items():
	if data[key]['annotations']['label'] == "eating spaghetti" \
        or data[key]['annotations']['label'] == "riding mechanical bull" \
        or data[key]['annotations']['label'] == "presenting weather forecast" \
        or data[key]['annotations']['label'] == "sled dog racing" \
        or data[key]['annotations']['label'] == "playing squash" \
        or data[key]['annotations']['label'] == "snowkiting" \
        or data[key]['annotations']['label'] ==  "diving cliff" \
        or data[key]['annotations']['label'] == "shearing sheep" \
        or data[key]['annotations']['label'] == "pull ups" \
        or data[key]['annotations']['label'] == "filling eyebrows" \
        or data[key]['annotations']['label'] == "bench pressing" \
        or data[key]['annotations']['label'] == "riding or walking with horse" \
        or data[key]['annotations']['label'] == "passing American football" \
        or data[key]['annotations']['label'] == "picking fruit" \
        or data[key]['annotations']['label'] == "weaving basket" \
        or data[key]['annotations']['label'] == "playing tennis" \
        or data[key]['annotations']['label'] == "crawling baby" \
        or data[key]['annotations']['label'] == "cutting watermelon" \
        or data[key]['annotations']['label'] == "tying tie" \
        or data[key]['annotations']['label'] == "trapezing" \
        or data[key]['annotations']['label'] == "bowling" :

		wellData[key] = value

	elif data[key]['annotations']['label'] == "recording music" \
        or data[key]['annotations']['label'] == "tossing coin" \
        or data[key]['annotations']['label'] == "fixing hair" \
        or data[key]['annotations']['label'] == "yawning" \
        or data[key]['annotations']['label'] == "shooting basketball" \
        or data[key]['annotations']['label'] == "answering question" \
        or data[key]['annotations']['label'] ==  "rock scissors paper" \
        or data[key]['annotations']['label'] == "drinking beer" \
        or data[key]['annotations']['label'] == "shaking hands" \
        or data[key]['annotations']['label'] == "making a cake" \
        or data[key]['annotations']['label'] == "throwing ball" \
        or data[key]['annotations']['label'] == "drinking shots" \
        or data[key]['annotations']['label'] == "eating chips" \
        or data[key]['annotations']['label'] == "drinking" \
        or data[key]['annotations']['label'] == "headbutting" \
        or data[key]['annotations']['label'] == "sneezing" \
        or data[key]['annotations']['label'] == "sniffing" \
        or data[key]['annotations']['label'] == "eating doughnuts" \
        or data[key]['annotations']['label'] == "faceplanting" \
        or data[key]['annotations']['label'] == "slapping" :

		badData[key] = value

with open(outPathForWellData, 'w') as outfile:
    json.dump(wellData, outfile)

with open(outPathForBadData, 'w') as outfile:
    json.dump(badData, outfile)
