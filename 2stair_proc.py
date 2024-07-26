def staircase( repeats, threshold, step, correct):
	#first: constants
	kStepMin = 1
	kThreshMin = 20
	kStepMax = 30
	kThreshMax = 80

	#correctInt is 1 if stimuli detected, else -1
	if correct:
		correctInt = 1
	else:
		correctInt = -1

	#decrease step size if reversal
	if ((repeats > 0 and correctInt < 0) or (repeats < 0 and correctInt > 0)) :		
		step = step / 2
		if abs(repeats) > 3:
			print("reversal after DOUBLING!")
			repeats = 0
		else:
			print("reversal without prior doubling")
			repeats = correctInt
	else:
		if repeats == 0: #very first trial - no previous doubling	
			repeats = repeats + correctInt 
	repeats = repeats + correctInt

	#increase step size for repeated responses
	if abs(repeats) > 3:
		print("Three or more in same direction DOUBLING!")
		step = step * 2	
	if step < kStepMin:
		step = kStepMin
	if step > kStepMax:
		step = kStepMax

	#now adjust threshold
	prevThreshold = threshold
	threshold = threshold - (step * correctInt)
	if threshold < kThreshMin:
		threshold = kThreshMin
	if threshold > kThreshMax:
		threshold = kThreshMax
	step = abs(prevThreshold - threshold)
	print("  threshold %.2f, stepsize %.2f, repeats %d" % (threshold, step, repeats))
	return repeats, threshold, step

#####Main Loop

#Initialize staircase
repeats = 0
threshold = 80
step = 15

#Python 2/3 dual compatibility -- 3 uses input, 2 uses raw_input, this should
#allow both to be happy.
try:
    input = raw_input
except NameError:
    pass

#Titrate across trials
for trial in range(0, 150): #allowing up to 150 trials before program breaks
	response = input("Trial %d: Does participant detect a stimulus with a contrast of  %.2f? (y/n)\n" % (trial, threshold))
	if response.lower() in ("y", "yes"):
     		Correct = True
	else:
		Correct = False
	repeats, threshold, step = staircase( repeats, threshold, step, Correct)

##Oh look, an ancient note from grad school past -- I'll leave it here, with
##this new note.
#What do we need to pass back and forth with EB?
#Increase or Decrease of contrast (if threshold < 50, decrease.  if threshold > 50, increase)
#Correct or Incorrect response
#Repeats_up
#Repeats_down
#Threshold_up
#Threshold_down
#Step_up
#Step_down
#Double_up/Double_down (Not needed, doubling status handled by repeats variable and offsetting from first trial)
