import copy
import random

class Hat:

	#initialize the object with any number of arguments with any keyword
    def __init__(self, **kwargs):
        self.contents = []
        #sotre the arguments as a list of strings representing the colors quantified by their values 
        # eg ['red', 'red', 'red', 'green', 'green]
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num):
    	#if the number ot draw is greater than the number of balls, draw all the balls
        if num > len(self.contents):
            drawn =[ball for ball in self.contents]
            self.contents=[]
            return drawn
		
		#create a randomized list based on the number entered and the contents list
        drawn = random.sample(self.contents, num)
        for ball in drawn:
        	#remove the balls from the original contents -- "without replacement"
            self.contents.remove(ball) 
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
	#this function calculates the probability of obtaining at least a certain set of balls based on an input that is adictionary 
    for _ in range(num_experiments):
    	#here we eun the eperiment (the draw)
        # Deepcopy so original hat is not changed
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)

        # Count balls
        #here we confirm if it  was a success or not by setting a new dictionary with the counts 
        drawn_counts = {}
        for ball in drawn_balls:
        	#add 1 to each key value iin ball eg red: 1 -> red: 2
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
		
		#comparing the two dictionaries resulting is success equals to True if all conditions are met 
        success = all(drawn_counts.get(ball, 0) >= count for ball, count in expected_balls.items())
        if success:
            success_count += 1
	#finally calculate the probability from all experiments
    probability = success_count / num_experiments
    return probability

# Example usage
hat = Hat(black=6, red=4, green=3)
print(hat.contents)
print(hat.draw(15))  # Draw 5 balls (this will mutate hat.contents)

# Run the experiment
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(probability)