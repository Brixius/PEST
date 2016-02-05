class stair:
    def __init__(self):
        self.thresh = 50
        self.step = 10
	self.repeats = 0
	self.stepMin = 1
	self.threshMin = 1
	self.stepMax = 30
	self.threshMax = 99
	self.doubled = 0
    def adjust(self, wasCorrect):
#If participant got trial correct, do the following.
	if wasCorrect:
		if self.repeats == 0:
			self.repeats = 2
			#If this is the first trial (only time repeats will be 0), a correct response sets repeats
			#to 2.  As seen below, an incorrect response sets repeats to -2.  This is because we want
			#to double the step size after three contiguous right or
			#wrong responses, and the script doubles the step size whenever repeats is >=4 or <= -4.
			#Thus, 2, 3, 4, double.  -2, -3, -4, double.  We do not use 1 or -1 here because, per rule
			#4 of PEST, if a reversal (going from a string of right responses to a wrong response, or
			#or vice versa) occurs immediately after a step size doubling, one extra contiguous
			#response must be made to get another doubling (4, instead of 3).  When this reversal-
			#after-doubling occurs, the repeats are set to 1 or -1.  When a reversal occurs NOT after
			#a doubling, the repeats are again set to 2 or -2.  This way, it normally takes 3
			#contiguous correct / incorrect responses to double step size, but on the rare reversal-
			#after-doubling event, it takes 4, per PEST.
		else:
			self.repeats = self.repeats+1
		if self.repeats <= 0 and self.doubled == 0:
			self.repeats = 2 #REVERSAL! NOT AFTER A DOUBLING
			self.step = self.step / 2
		elif self.repeats <= 0 and self.doubled == 1:
			self.repeats = 1 #REVERSAL! AFTER A DOUBLING!
			self.step = self.step / 2
		if self.repeats >= 4:
			self.step = self.step*2
			self.doubled = 1
		elif self.repeats < 4:
			self.doubled = 0
		if self.step < self.stepMin:
			self.step = self.stepMin
		if self.step > self.stepMax:
			self.step = self.stepMax
		self.thresh = self.thresh - self.step
#If the participant got the trial incorrect, do the following
	else:
		if self.repeats == 0: 
			self.repeats = -2
		else:
			self.repeats = self.repeats-1
		if self.repeats >= 0 and self.doubled == 0:
			self.repeats = -2 #REVERSAL! NOT AFTER A DOUBLING
			self.step = self.step / 2
		elif self.repeats >= 0 and self.doubled == 1:
			self.repeats = -1 #REVERSAL! AFTER A DOUBLING!
			self.step = self.step / 2
		if self.repeats <= -4:
			self.step = self.step*2
			self.doubled = 1
		elif self.repeats > 4:
			self.doubled = 0
		if self.step < self.stepMin:
			self.step = self.stepMin
		if self.step > self.stepMax:
			self.step = self.stepMax
		self.thresh = self.thresh + self.step
	if self.thresh < self.threshMin:
		self.thresh = self.threshMin
	if self.thresh > self.threshMax:
		self.thresh = self.threshMax
	print "  threshold %.2f, stepsize %.2f, repeats %d" % (self.thresh, self.step, self.repeats) #TEXT FEEDBACK: COMMENT OUT FOR FINAL CODE
	return self.thresh

#####Main Loop
#Initialize staircase
s = stair()
threshold = s.thresh
#Titrate across trials
for trial in range(0, 150): #allowing up to 150 trials before program breaks
	response = raw_input("Trial %d: Does participant detect a stimulus with a contrast of  %.2f? (y/n)\n" % (trial, threshold))
	if response.lower() in ("y", "yes"):
     		Correct = True
	else:
		Correct = False
	threshold = s.adjust(Correct)
