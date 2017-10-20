import json

path = 'C:\Git_Projects2\Human-action-recognition\\'

with open(path + "kinetics_train.json") as data_file:    
    data = json.load(data_file)

eating_spahetti = 0
riding_mechanical_bull = 0
presenting_weather_forecast = 0
sled_dog_racing = 0
playing_squash = 0
snowkiting = 0
diving_cliff = 0
shearing_sheep = 0
pull_ups = 0
filling_eyebrows = 0
bench_pressing = 0
riding_or_walking_with_horse = 0
passing_American_football = 0
picking_fruit = 0
weaving_basket = 0
playing_tennis = 0
crawling_baby = 0
cutting_watermelon = 0
tying_tie = 0
trapezing = 0
bowling = 0

recording_music = 0
tossing_coin = 0
fixing_hair = 0
yawning = 0
shooting_basketball = 0
answering_question = 0
rock_scissors_paper = 0
drinking_beer = 0
shaking_hands = 0
making_a_cake = 0
throwing_ball = 0
drinking_shots = 0
eating_chips = 0
drinking = 0
headbutting = 0
sneezing = 0
sniffing = 0
eating_doughnuts = 0
faceplanting = 0
slapping = 0

for key, value in data.items():
	if data[key]['annotations']['label'] == "eating spaghetti":
		eating_spahetti = eating_spahetti + 1
	if data[key]['annotations']['label'] == "riding mechanical bull" :
		riding_mechanical_bull = riding_mechanical_bull + 1
	if data[key]['annotations']['label'] == "presenting weather forecast" :
		presenting_weather_forecast = presenting_weather_forecast + 1
	if data[key]['annotations']['label'] == "sled dog racing" :
		sled_dog_racing = sled_dog_racing + 1
	if data[key]['annotations']['label'] == "playing squash" :
		playing_squash = playing_squash + 1
	if data[key]['annotations']['label'] == "snowkiting" :
		snowkiting = snowkiting + 1
	if data[key]['annotations']['label'] == "diving cliff" :
		diving_cliff = diving_cliff + 1
	if data[key]['annotations']['label'] == "shearing sheep" :
		shearing_sheep = shearing_sheep + 1
	if data[key]['annotations']['label'] == "pull ups" :
		pull_ups = pull_ups + 1
	if data[key]['annotations']['label'] == "filling eyebrows" :
		filling_eyebrows = filling_eyebrows + 1
	if data[key]['annotations']['label'] == "bench pressing" :
		bench_pressing = bench_pressing + 1
	if data[key]['annotations']['label'] == "riding or walking with horse" :
		riding_or_walking_with_horse = riding_or_walking_with_horse + 1
	if data[key]['annotations']['label'] == "passing American football" :
		passing_American_football = passing_American_football + 1
	if data[key]['annotations']['label'] == "picking fruit" :
		picking_fruit = picking_fruit + 1
	if data[key]['annotations']['label'] == "weaving basket" :
		weaving_basket = weaving_basket + 1
	if data[key]['annotations']['label'] == "playing tennis" :
		playing_tennis = playing_tennis + 1
	if data[key]['annotations']['label'] == "crawling baby" :
		crawling_baby = crawling_baby + 1
	if data[key]['annotations']['label'] == "cutting watermelon" :
		cutting_watermelon = cutting_watermelon + 1
	if data[key]['annotations']['label'] == "tying tie" :
		tying_tie = tying_tie + 1
	if data[key]['annotations']['label'] == "trapezing" :
		trapezing = trapezing + 1
	if data[key]['annotations']['label'] == "bowling" :
		bowling = bowling + 1
#####################################################################################

	if data[key]['annotations']['label'] == "recording music" :
		recording_music = recording_music + 1
	if data[key]['annotations']['label'] == "tossing coin" :
		tossing_coin = tossing_coin + 1
	if data[key]['annotations']['label'] == "fixing hair" :
		fixing_hair = fixing_hair + 1
	if data[key]['annotations']['label'] == "yawning" :
		yawning = yawning + 1
	if data[key]['annotations']['label'] == "shooting basketball" :
		shooting_basketball = shooting_basketball + 1
	if data[key]['annotations']['label'] == "answering question" :
		answering_question = answering_question + 1
	if data[key]['annotations']['label'] == "rock scissors paper" :
		rock_scissors_paper = rock_scissors_paper + 1
	if data[key]['annotations']['label'] == "drinking beer" :
		drinking_beer = drinking_beer + 1
	if data[key]['annotations']['label'] == "shaking hands" :
		shaking_hands = shaking_hands + 1
	if data[key]['annotations']['label'] == "making a cake" :
		making_a_cake = making_a_cake + 1
	if data[key]['annotations']['label'] == "throwing ball" :
		throwing_ball = throwing_ball + 1
	if data[key]['annotations']['label'] == "drinking shots" :
		drinking_shots = drinking_shots + 1
	if data[key]['annotations']['label'] == "eating chips" :
		eating_chips = eating_chips + 1
	if data[key]['annotations']['label'] == "drinking" :
		drinking = drinking + 1
	if data[key]['annotations']['label'] == "headbutting" :
		headbutting = headbutting + 1
	if data[key]['annotations']['label'] == "sneezing" :
		sneezing = sneezing + 1
	if data[key]['annotations']['label'] == "sniffing" :
		sniffing = sniffing + 1
	if data[key]['annotations']['label'] == "eating doughnuts" :
		eating_doughnuts = eating_doughnuts + 1
	if data[key]['annotations']['label'] == "faceplanting" :
		faceplanting = faceplanting + 1
	if data[key]['annotations']['label'] == "slapping" :
		slapping = slapping + 1


outFile = open(path + "out.txt", "w")

outFile.write("eating_spahetti \t\t" + str(eating_spahetti) + "\n");
outFile.write("riding_mechanical_bull \t\t" + str(riding_mechanical_bull) + "\n")
outFile.write("presenting_weather_forecast \t\t" + str(presenting_weather_forecast) + "\n")
outFile.write("sled_dog_racing \t\t" + str(sled_dog_racing) + "\n")
outFile.write("playing_squash \t\t" + str(playing_squash) + "\n")
outFile.write("snowkiting \t\t" + str(snowkiting) + "\n")
outFile.write("diving_cliff \t\t" + str(diving_cliff) + "\n")
outFile.write("shearing_sheep \t\t" + str(shearing_sheep) + "\n")
outFile.write("pull_ups \t\t" + str(pull_ups) + "\n")
outFile.write("filling_eyebrows \t\t" + str(filling_eyebrows) + "\n")
outFile.write("bench_pressing \t\t" + str(bench_pressing) + "\n")
outFile.write("riding_or_walking_with_horse \t\t" + str(riding_or_walking_with_horse) + "\n")
outFile.write("passing_American_football \t\t" + str(passing_American_football) + "\n")
outFile.write("picking_fruit \t\t" + str(picking_fruit) + "\n")
outFile.write("weaving_basket \t\t" + str(weaving_basket) + "\n")
outFile.write("playing_tennis \t\t" + str(playing_tennis) + "\n")
outFile.write("crawling_baby \t\t" + str(crawling_baby) + "\n")
outFile.write("cutting_watermelon \t\t" + str(cutting_watermelon) + "\n")
outFile.write("tying_tie \t\t" + str(tying_tie) + "\n")
outFile.write("trapezing \t\t" + str(trapezing) + "\n")
outFile.write("bowling \t\t" + str(bowling) + "\n")

outFile.write("recording_music \t\t" + str(recording_music) + "\n")
outFile.write("tossing_coin \t\t" + str(tossing_coin) + "\n")
outFile.write("fixing_hair \t\t" + str(fixing_hair) + "\n")
outFile.write("yawning \t\t" + str(yawning) + "\n")
outFile.write("shooting_basketball \t\t" + str(shooting_basketball) + "\n")
outFile.write("answering_question \t\t" + str(answering_question) + "\n")
outFile.write("rock_scissors_paper \t\t" + str(rock_scissors_paper) + "\n")
outFile.write("drinking_beer \t\t" + str(drinking_beer) + "\n")
outFile.write("shaking_hands \t\t" + str(shaking_hands) + "\n")
outFile.write("making_a_cake \t\t" + str(making_a_cake) + "\n")
outFile.write("throwing_ball \t\t" + str(throwing_ball) + "\n")
outFile.write("drinking_shots \t\t" + str(drinking_shots) + "\n")
outFile.write("eating_chips \t\t" + str(eating_chips) + "\n")
outFile.write("drinking \t\t" + str(drinking) + "\n")
outFile.write("headbutting \t\t" + str(headbutting) + "\n")
outFile.write("sneezing \t\t" + str(sneezing) + "\n")
outFile.write("sniffing \t\t" + str(sniffing) + "\n")
outFile.write("eating_doughnuts \t\t" + str(eating_doughnuts) + "\n")
outFile.write("faceplanting \t\t" + str(faceplanting) + "\n")
outFile.write("slapping \t\t" + str(slapping) + "\n")

outFile.close()