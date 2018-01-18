# Assignment1 - Practice Designing Models

> * Participant name: Paige Paulsen
> * Jan.18.2018
> * Project Title: Solar Tracking For Optimizing Solar Panel Efficiency

## General Introduction: Solar Tracking

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![By Rama - Own work, CC BY-SA 2.0 fr, https://commons.wikimedia.org/w/index.php?curid=874992](images/solarpanel-07.jpg)
By Rama (Own work) [CeCILL (http://www.cecill.info/licences/Licence_CeCILL_V2-en.html) or CC BY-SA 2.0 fr (https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en)], via Wikimedia Commons


## Requirements (Experimental Design)

Solar panels are most efficient when using a solar tracker of some kind, which orients the panels towards the sun. This problem can be modeled using a simple simulation in Python.

By maximizing the efficiency of solar panels, solar energy can make up a greater portion of the energy requirements of the city of Orlando, reducing greenhouse gas emissions and improving air quality. This program will simulate a single axis solar tracker, allowing optimization of angle based on time of year. By including functionality to retract the panels during periods of high wind, we can also reduce the likelihood of damage. In addition, by signalling the user when a battery is full, we can improve the implementation of home solar for lay users.

These types of active solar trackers are used in smaller installations, where the same increase in output is not possible through adding additional solar panels. However, they are not suitable for rooftop installations due to the increased mechanical requirements and additional wind speeds. This simulation will be useful for deciding if a solar tracker is an appropriate choice for a given location by simulating the rate of battery charge. (Source: https://en.wikipedia.org/wiki/Solar_tracker)

To use an active dual axis solar tracker we will need several types of inputs. We will need to estimate the rate at which the battery fills while exposed to sunlight. We will need to collect wind speed data from a local sensor so that the panels retract when the wind speed reaches dangerous levels. We will need to account for the North/South angle of the sun at different times of year.

## Smart City Solar Panel Tracking Model

This model shows how a solar panel works as a system - the inputs from weather conditions and sunlight, behavior modified by the schedule, and output as battery charging. 

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of how the solar tracker interacts with weather conditions and schedule to charge the battery
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City (My Problem) Simulation

The goal of this simulation is to demonstrate how a solar panel can charge a battery, given the changing position of the sun throughout the year, the possibility of cloud cover, and the potential for dangerous high winds. The [**summary**](model/README.md) document describes the goals of the simulation.


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.


