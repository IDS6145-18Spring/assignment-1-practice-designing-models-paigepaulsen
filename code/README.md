## Smart City Solar Tracker Model

Starting coding framework for optimizing solar panel efficiency using a single axis.

The [**Code**](code/solar_system) here should follow the pattern described in the state machine diagram, although all the functionality may not be present or fully functional. I learned how to Build on Thursday evening, so there are certainly a few errors in the code I had been writing before that.

The [schedule](code/solar_system/schedule.py) class has attributes for the optimal angle of the panel, the time exposed to sunlight, the name of the month, and the timestep that will call a specific month. Each object within this class has a dedicated optimal angle, amount of daylight, name (i.e. January), and the appropriate remainder if the timestep were divided by 12 to produce that month. The whatmonth() function is intended to instantiate the appropriate month object based on the timestep.

The [wind](code/solar_system/wind.py) class is simple - the wind has a speed attribute and a function that raises that speed. I would want this function to be called randomly in the timesteps, but that is a problem for another time.

The [sun](code/solar_system/sun.py) class is also simple. The sun has a default power value, indicating it is sunny, and a function to simulate clouds rolling in that simply changes the power level. I would also want this to be called randomly in the timesteps, but left it for another time (I would love to know how to get random numbers or T/F outcomes to work).

The [battery](code/solar_system/battery.py) class records the amount of energy added to the battery each timestep. It has two functions, charge() and finish(). Charge uses inputs from different classes - the power level of the sun (ideally, passed through the panel, to indicate how it would actually work with the machine)and the amount of daylight, based on the attributes of that month object. 

The [panels](code/solar_system/panels.py) class contains attributes for the current angle of the panel, a wind sensor attribute, and a sun sensor attribute. The angle of the panel should be set by using the ChangeAltitude() function, which should just pass the optimal angle from the schedule object to the panel attribute. The wind sensor attribute should be set via the Shelter() function, which should read the wind speed from the wind class. The Shelter() function should only be called if that wind speed is 25 or greater. The sun sensor attribute should hold the current power of the sun, so that it can be passed to the battery.

In the [main](code/solar_system/main.py) I have tried to put these together as best I can, using the timestep function from POTS. Ideally, at the beginning of the simulation, a panel and a battery are created. Then, the timestep begins, and timestep a new month is instantiated (in the schedule file). The attributes of wind, sun, and schedule then determine the output of the panel, read by the battery as the charging is simulated. The simulation should end when the battery reaches 100.
