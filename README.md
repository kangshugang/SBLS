# Simulation-Based Learning and Searching for Decision Making

This project provides a generic **Python framework** for simulation-based learning and searching, aiming at solving decision making problems.

Here a **decision making problem** is defined as a problem that must have different **alternative solutions**, we need to **make a decisions** to find the **best solutions** based on some **performance measures**.

Based on the above definition, a decision making problem must meet the following requirements:

  - **multiple alternative solutions**
  - **the solutions are measurable and comparable**

First, if the problem has only a single unique solution, there is no other choice. There will be no need to make decisions. This problem is not a decision making problem.

Second, if the soltuions are not measurable and comparable, we have no way to tell whether a solution is better or worse than another solution. Then, the computer cannot help much on such problems. Therefore such problems are out of the scope of this project. 

If a decision making problem meets the above two requirements, we can try to use computer to help make the best decisions. 

In order to solve the problem, we need to do the following:

  - **model the problem**
  - **test & training the model**
  - **use the trained model to make decisions**
  
Model the problem means creating a **simulation model** to mimick the problem itself. With the simualtion model, we can simulate the problem solving process and generate the solutions based on the given input. As defined before, with a given input, there will be multiple possible solutions, the simulation model will be able to simulate different senarios and generate (ideally all) the alterative solutions. 

After a model is created, we need to **verify** whether the model is **correct**. And we need to **train** the model to make it **"smart"**.

With a **correct** and **smart** model, we can then utilize it for making better decisions. Basically, given a input, the system can produce **high quality** (if not the best) solutions **quickly** (i.e., in a timely manner).

Here we have a few **questions**:
  1. Why simulation?
  2. Why search? 
  3. What do you mean *quickly*?
  4. Why train the model?
  5. Is the best solution always achivable?
  
First, simulation is a natural way to model a problem. Basically, tell the computer how to create solutions with the given input. We call this a simulation model.

Secondly, as described before, there will be mutliple alternative solutions. The process of finding the best solution from the many alternatives is called **search**. 

Thirdly, the number of alternative solutions is often very large, such as in millions or billions, or even more. This is known as **combinatorial explosion**, and sometimes called NP-hard (don't worry about NP-hard, we are not going to go deep in that). For this kind of problems, the difficulty is not knowing how to find the best solution, the difficulty is how to find it **quickly**. Of course, if we have enough time, we can enumerate all the alternative solutions and compare them, and then we find the best solution. It seems to be trival. But this is often not practical, as it may take the computer very long time (such as hundreds of years) to find the best solution in this way.  

Forthly, The purpose of training the model is to **learn** some patterns based on the problem itself (**training** with simulation practice through some sample inputs). With the patterns learned, when we need to make a decision for a given input, the patterns can be used to guide the search to **quickly** reach **high quality** solutions.

Finally, the answer to the question: *"Is the best solution always achivable?"* is both yes and no. If there is no time limitation, the answer is yes. If there is a time limitation, the answer is no. In practical applications, there is always a time limitation, such as minutes or even seconds, therefore, generally speaking, the answer is no. This is why we try to find **high quality** solutions, instead of trying to find the best (or optimal) solutions.

The project is programmed in **Python**. It provides a **generic framework** for *modeling complex decision making problems*, *traing the model with simulation practices*, and *utilize the trained models for decision makings*. It combine the strength of *learning* and *search* together in tackling the challenges.

**Scheduling** is a decision making problems that is challenging in both research and industrial practices. It is be used as an example application to demonstrate the feasiblity and effectiveness of this framework.

## Notes
 - This project is now at the conceptual phase, code will be developed and commited to this repository overtime.
 - This is a spare time project, do not expect any timely progress.
   
