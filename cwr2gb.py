from functools import reduce
from random import random, shuffle

class cwr2gb_Negotiator:
    # Constructor - Note that you can add other fields here; the only 
    # required fields are self.preferences and self.offer
    def __init__(self):
        self.preferences = []
        self.offer = []
        self.iter_limit = 0
        self.count = 0
        self.nego = ""
        self.result = (True, 0, 0, 0)
        self.util = 0

    # initialize(self : BaseNegotiator, preferences : list(String), iter_limit : Int)
        # Performs per-round initialization - takes in a list of items, ordered by the item's
        # preferability for this negotiator
        # You can do other work here, but still need to store the preferences 
    def initialize(self, preferences, iter_limit):
        self.preferences = preferences
        self.iter_limit = iter_limit

    # make_offer(self : BaseNegotiator, offer : list(String)) --> list(String)
        # Given the opposing negotiator's last offer (represented as an ordered list), 
        # return a new offer. If you wish to accept an offer & end negotiations, return the same offer
        # Note: Store a copy of whatever offer you make in self.offer at the end of this method.
    def make_offer(self, offer):
       #Counter for rounds and determining which negotiator you are

       if self.count > 0:
            self.count = self.count + 1
       if offer == None and self.count == 0:
            self.nego = "A"
            self.count = self.count + 1
            self.offer = self.preferences[:]
            return self.offer
       elif self.count == 0:
            self.nego = "B"
            self.count = self.count + 1
            self.offer = self.preferences[:]
            return self.offer
       #Scenario when my utility is greater than theirs
       #Or Scenario when their utility is negative and mine is positive
       self.offer = offer
       if self.util < 0 and self.utility() > 0:
           self.offer = offer[:]
           return offer
       if self.util < self.utility():
           self.offer = offer[:]
           return offer
       #Scenario for Round 10 and Negotiator B
       if self.count == 10 and self.nego == "B":
            self.offer = self.preferences[:]
            return self.offer
       #Scenario for Negotiator A Last Round
       if self.count == 11:
            self.offer = self.preferences[:]
            return self.offer
       #Scenario for everything else, random generator to throw off other robots
       if self.count != 11 and self.count != 10:
            self.util2 = self.utility()
            self.offer = self.preferences[:]
            self.max = self.utility()
            while self.util2 < self.util and self.util < self.max:
                ordering = self.preferences[:]
                shuffle(ordering)
                self.offer = ordering[:]
                self.util2 = self.utility()
            return self.offer

    # utility(self : BaseNegotiator) --> Float
        # Return the utility given by the last offer - Do not modify this method.
    def utility(self):
        total = len(self.preferences)
        return reduce(lambda points, item: points + ((total / (self.offer.index(item) + 1)) - abs(self.offer.index(item) - self.preferences.index(item))), self.offer, 0)

    # receive_utility(self : BaseNegotiator, utility : Float)
        # Store the utility the other negotiator received from their last offer
    def receive_utility(self, utility):
        self.util = utility
        return self.util

    # receive_results(self : BaseNegotiator, results : (Boolean, Float, Float, Int))
        # Store the results of the last series of negotiation (points won, success, etc.)
    def receive_results(self, results):
        self.result = results
        return self.result


