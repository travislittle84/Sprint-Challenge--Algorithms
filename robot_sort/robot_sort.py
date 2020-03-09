class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # Robot - iterative select sort

        # L1: Robot goes through the list, one by one, starting at the beginning, looking for the smallest number.
        ## Robot picks up a number, moves to the next.
        ## Robot compares the number it's holding to the one it's standing on
        ### If the number the robot is standing on is smaller than what it's holding - swap it out
        ### Continue throughout the list, looking for and swapping out smaller numbers than in its hands
        # Once the robot hits the end of the list, go back to where the robot started (which will be None (empty)), place the item the robot is holding into the empty spot
        # Robot moves to next position, picks up the number it's standing on (hands should be empty so no comparision needed)
        # Robot continues searching and swapping smaller numbers
        # 
        # HOW TO KNOW IT"S FINISHED
        # - If at the last spot, call go back left function like usual
        # - inside go back left function, the function checks if the robot is standing in an empty spot
        #   - If robot is standing on an empty spot, it's holding the final number, so it just needs to
        #      put it back and turn off the light to end the while loop. 

        def initializeBot():
            self.swap_item()
            self.move_right()
        
        # this helper function moves to next spot and picks up the number there to prepare for
        # next iteration of the robot's main while loop (which is comparing it's hands to what it's standing on)
        def intialize_search_subroutine():
            # move right and pick up next item to start us off for next iteration
            self.move_right()
            self.swap_item()
        
        # this helper function "resets" the search back to where it started
        # it also detects if the bot is finished sorting
        def go_back_until_empty_spot():

            # ARE WE DONE?  check if the spot we're at is empty
            if self.compare_item() == None:
                # if it's empty we're done
                self.swap_item() # put the number back
                print(f'OFF - My job is complete.')
                self.set_light_off()    # turn off the light - ends the main while loop
            else:
                while self.can_move_left:
                    # search for the empty spot, which is where the search started for *THIS* iteration of while loop
                    self.move_left()
                    if self.compare_item() == None:
                        self.swap_item() # put the item into its proper place
                        
                        # get the bot ready for next iteration of while loop
                        intialize_search_subroutine()
                        break

        # helper method to make sure the list is at least 2 - call this at start
        def check_more_than_one():
            return self.can_move_right()

        # make sure the list is long enough to sort
        if check_more_than_one():
            self.set_light_on()
            print(f'ON: Beep bop boop - I am going to sort a list')
        else:
            print('List must be at least one long to sort')
        
        # print(f'Sorting {self._list}')

        initializeBot()
        
        while self.light_is_on(): # using the light as an on off switch
            # beep bop - searching for smallest number, i'm at the corect location with
            # a number in my hand thanks to either initializeBot or initialize_search_subroutine()
            # being called in go_back_until_empty_spot()
            
            if self.compare_item() == 1:
                self.swap_item()

            if self.can_move_right():
                self.move_right()            
            else:
                # at the end                
                if self.compare_item() == 1: # compare before go back
                    self.swap_item()
                go_back_until_empty_spot()
                

                    
# l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
# robot = SortingRobot(l)
# robot.sort()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)