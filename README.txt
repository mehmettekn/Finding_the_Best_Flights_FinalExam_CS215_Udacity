This is my solution to final question #4 for CS215 at Udacity.com

###


Source code is in finding_the_best_flights.py

Unittesting is provided in unit_test.py

Data used for testing is in all_flights.py

###

This program uses an implementation of Dijkstra algorithm. It 
is a simple example of lexographic sorting. This program creates a 
graph, where nodes are locations and edges are flights. It then 
searches the graph and returns a list of flights between the origin
and the destination provided. It returns the cheapest path possible.
Should there be more than one cheapest case, it returns the path with
the shortest flight duration. It returns None, when destination is not 
reachable from origin.

The unit_test module only provides known test cases and asserts the
answers. The answers are provided in the question description at Udacity.
The tests are calculated on a list of flights flown by an
Australian airline, Skipper. The program assumes that all flights are 
on the same day and no overnight layovers are allowed.

###

Mehmet Tekin, 2012.