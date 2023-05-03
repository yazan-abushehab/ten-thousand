import random
from collections import Counter
class GameLogic:

    def roll_dice(num_dice):
       """
       Roll the specified number of dice, and return a list of the results.
       Each result is a random integer between 1 and 6 (inclusive).
       from chatGpt
       """

       return tuple(random.randint(1, 6) for _ in range(num_dice)) 
    
    def calculate_score(tuple):

        """This function takes in a tuple of dice rolls and calculates 
        the score based on the rules of a dice game.
        It uses a counter to count the occurrences of each number in the tuple and then calculates the score based on the different combinations of numbers that can appear.
        For example, if there are one or two 5's in the tuple, 
        the score is increased by 50 points for each 5. If there are three 5's,
        the score is increased by 500 points, and so on for other combinations of numbers.
        The function also checks for other combinations such as three pairs, 
        a straight (1-6), and double trips (two sets of three of a kind). The score is doubled for double trips.
        Finally, the function returns the total score as an integer"""
        unbanked=0
        counter = Counter(tuple)
        """5's """
        if counter[5] == 1 or counter[5] == 2 : unbanked+=50 *counter[5]
        if counter[5] == 3 :unbanked += 500
        if counter[5] == 4 :unbanked += 1000
        if counter[5] == 5 :unbanked += 2000
        if counter[5] == 6 :unbanked += 4000
        """1's"""
        if counter[1] == 1 or counter[1] == 2 : unbanked+=100 *counter[1]
        if counter[1] == 3 :unbanked += 1000
        if counter[1] == 4 :unbanked += 2000
        if counter[1] == 5 :unbanked += 4000
        if counter[1] == 6 :unbanked += 8000

        """2's"""
        if counter[2] == 3 :unbanked += 200
        if counter[2] == 4 :unbanked += 400
        if counter[2] == 5 :unbanked += 800
        if counter[2] == 6 :unbanked += 1600
        """3's	"""
        if counter[3] == 3 :unbanked += 300
        if counter[3] == 4 :unbanked += 600
        if counter[3] == 5 :unbanked += 1200
        if counter[3] == 6 :unbanked += 2400
        """4's"""
        if counter[4] == 3 :unbanked += 400
        if counter[4] == 4 :unbanked += 800
        if counter[4] == 5 :unbanked += 1600
        if counter[4] == 6 :unbanked += 3200
        """6's"""
        if counter[6] == 3 :unbanked += 600
        if counter[6] == 4 :unbanked += 1200
        if counter[6] == 5 :unbanked += 2400
        if counter[6] == 6 :unbanked += 4800
        
        """three pairs"""
        if len(counter)== 3 and len(set(counter.values()))==1 and list(set(counter.values()))[0]==2:
            unbanked = 1500
        """Straight 1- 6"""
        if counter[1] == 1 and counter[2] == 1 and counter[3] == 1 and counter[4] == 1 and counter[5] == 1 and counter[6] == 1:
            unbanked = 2000
        """Double Trips when 2 sets of a 3 of a kind are hit. Scores are added together and doubled"""
        if len(counter)== 2 and len(set(counter.values()))==1 and list(set(counter.values()))[0]==3:
            unbanked= unbanked * 2
        return unbanked
    def validate_keepers(roll,keepers):
        roll_to_test_cheater = list(roll)
        for i in keepers:
            if i not in roll_to_test_cheater:
                  
                return False
            index = roll_to_test_cheater.index(i)
            roll_to_test_cheater.pop(index)
        return True
            
    def get_scorers(test_input):
        main_score = GameLogic.calculate_score(test_input)
        # print(main_score)
        scorers = []
        input_list = list(test_input)
        # print(range(len(input_list)))
        for i,val in enumerate(input_list):
            input_list.pop(i)
            element_score = GameLogic.calculate_score(tuple(input_list))
            if element_score != main_score:
                # print("x")
                scorers.append(val)
                input_list.insert(i,val)
            else:
                input_list.insert(i,val)   
        scorers_tuple = tuple(scorers) 
        # print(scorers_tuple)       
        return scorers_tuple