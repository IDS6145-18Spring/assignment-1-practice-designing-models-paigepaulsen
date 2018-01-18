## Smart City (Solar Tracker) Model - Class Diagram

This model is a class diagram, showing the classes with attributes and functions of the solar tracker system and how they interact.

![My Class Diagram](../images/solartracker_class.jpg)

The schedule determines the position of the solar panel. The wind determines if the panel needs to take shelter. The sun and the length of daylight together determine how the battery charges. The information about wind and sun are passed through to the panels (which contain a sensor, for the sake of argument)in order for all these pieces to happen.
