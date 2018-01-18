## Smart City (Solar Tracker) Model - Object Diagram

This model is a state machine diagram, showing how the program should make decisions. The goal of this diagram is to indicate how the classes will interact specifically within the timestep iteration, to demonstrate why they coded the way they are in the python files.


![My Behavior Diagram](../images/solartracker_behavior.jpg)

The first question is whether it is safe for the panels to be up, so the first question is if the wind is over 25 (miles per hour). If the wind is that fast, the panels will retract (inside the roof shingles, or a lair under the lawn, or just lay flat to reduce drag). If the wind is not dangerous, the panels ask the schedule what month it is and what the optimal angle for the panel should be. Then, the panels set an attribute called sunsense, which passes the power of the sun (i.e. if it is cloudy or not). Then, the panels need to ask the schedule how many hours of daylight, which is stored along with the optimal angle in each instance. Then, the panels pass this information to the battery as it charges = the charge is the hours of daylight multiplied by the power of the sun. This is added to the level already stored in the battery. If this level is greater than 100, the battery is finished charging, and will print a statement to that effect, and end the simulation. If it is not finished charging, the simulation continues to the next time step.
