## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model

The POTS system is a self watering plant system. It is made up to containers, which themselves contain different kinds of soil, vegetables that grow, and water. When either the water reserves or the nutrients in the container run out, the vegetables die.

The object diagram below shows a high-level abstraction of how the model works. As can be seen in the hand drawn diagram, the POTS system is composed of containers, vegetables, and water. The containers are composed of soil. There are different types of soil, a type of container (decorative), and types of vegetables represented in the object model as well.

*Object diagram:*
![POTS system](C:\Users\PaigePaulsen\Documents\GitHub\assignment-1-practice-designing-models-paigepaulsen\images\POTS_object1.jpg)


The class diagram below shows additional information about each class in the POTS model: attributes and functions (also known as methods and operations). Not all of the attributes were used (that I could find), and some of the methods are written to raise a NotImplementedError. These are duplicated in the subclasses below them, and the comments and some research online suggest that this is a check that the code is working properly in those subclasses. The POTS file is the main file, which contains three functions which call the other functions and classes located in the other files. 

*Class diagram:*
![POTS system](C:\Users\PaigePaulsen\Documents\GitHub\assignment-1-practice-designing-models-paigepaulsen\images\POTS_class.jpg)
