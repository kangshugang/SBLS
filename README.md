# Simulation-Based Learning and Searching for Decision Making

This project intends to provide a simulation-based learning and searching tool set to solve decision making problems.

Here a **decision making problem** is defined as a problem that must have different **alternative solutions**, we need to **make a decision** to find the **best solution** based on some **performance measures**.

Based on the above definition, a decision making problem must meet the following requirements:

  - **multiple alternative solutions**
  - **the solutions are measurable and comparable**

First, if the problem has only a single unique solution, there is no other choice. There will not be any need to make decisions. This problem is not a decision making problem.

Second, if the soltuions are not measurable and comparable, we have no way to tell which solution is better or worse than another solution. Then, the computer cannot help much on such problems. Therefore such problems are out of the scope of this project. 

If a decision making problem meets the above two requirements, we can try to use computer to help make the best decisions. 

In order to solve the problem, we need to do the following:

  - **model the problem**
  - **test & training the model**
  - **use the trained model to make decisions**
  
Model the problem means creating a **simulation model** to mimick the problem itself. With the simualtion model, we can simulate the problem solving process and generate the solutions based on the given input. As defined before, with a given input, there will be multiple possible solutions, the simulation model will be able to simulation different senarios and generate (ideally all) the alterative solutions. 

After a model is created, we need to **verify** whether the model is **correct**. And we need to **train** the model to make it **smart**.

With a **correct** and **smart** model in place, we can then utilize it for making decisions. Basically, given a input, the system can produce **high quality** (if not the best) solutions **quickly** (i.e., in a timely manner).

Here we have a few **questions**:
  1. Why simulation?
  2. Where is search?
  3. Why we need search? 
  4. Why train the model?
  5. What do you mean quickly?
  6. Is the best solution always achivable?
  






