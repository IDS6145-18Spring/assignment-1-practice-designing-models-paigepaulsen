# Assignment1 - Practice Designing Models

> * Participant name: Paige Paulsen
> * Jan.18.2018
> * Project Title: (Title of the problem you are looking and modeling)

## General Introduction: Solar Tracking

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![By Rama - Own work, CC BY-SA 2.0 fr, https://commons.wikimedia.org/w/index.php?curid=874992](images/solarpanel-07.jpg)

One problem which could be solved in a smart city is optimizing solar panel orientation. Solar panels are most efficient when using a solar tracker, which orients the panels towards the sun. This problem can be modeled using a simple simulation in Python. 

By maximizing the efficiency of solar panels, solar energy can make up a greater portion of the energy requirements of the city of Orlando, reducing greenhouse gas emissions and improving air quality. This program will simulate a tip-tilt dual axis solar tracker, allowing maximization based on time of day and time of year. By including functionality to retract the panels during periods of high wind, we can also reduce the likelihood of damage. In addition, by signalling the user when a battery is full, we can improve the implementation of home solar for lay users.

These types of active dual axis solar trackers are used in smaller installations, where the same increase in output is not possible through adding additional solar panels. However, they are not suitable for rooftop installations due to the increased mechanical requirements and additional wind speeds. This simulation will be useful for deciding if a dual axis solar tracker is an appropriate choice for a given location. (Source: https://en.wikipedia.org/wiki/Solar_tracker)

## Requirements (Experimental Design)

To use an active dual axis solar tracker we will need several types of inputs. We will need to estimate the rate at which the battery fills while exposed to sunlight. We will need to collect wind speed data from a local sensor so that the panels retract when the wind speed reaches dangerous levels. We will need to account for the North/South angle of the sun at different times of year. We will need to account for the East/West movement of the sun throughout the day, modified by the time of year.

## Smart City (My Problem) Model

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City (My Problem) Simulation

(remove: for part 3 add two to three sentences here and link the [**(your own name)**](model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
