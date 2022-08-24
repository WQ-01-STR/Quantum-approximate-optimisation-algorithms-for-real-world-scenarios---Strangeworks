# Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks
Womanium Quantum Hackathon 2022

## Name of the team: WQ-01-STR
- Discord ServerID: 1006453003512991794
- Discord Invite link: https://discord.gg/GKUh6smA
## Member of the team
### Oxana
- DiscordID: 692436681076375703
- GitHub: https://github.com/AmanieOxana
- email: oxana dot shaya at rwth minus aachen dot de
### Konstantin
- DiscordID: 745906052658364516
- GitHub: https://github.com/gksmail
- email: kgolovkin@mail.ru
## Name of the Pitch Presenter on Demo Day.
Oxana
## Name of the Challenge
   Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks
###  Command target in challenge
Make the QUBO algorithm available for research and use, available for business
<div>
  Quadratic unconstrained binary optimization (QUBO), also known as unconstrained binary quadratic programming (UBQP), is a combinatorial optimization problem with a wide range of applications from finance and economics to machine learning. QUBO is an NP hard problem, and for many classical problems from theoretical computer science, like maximum cut, graph coloring and the partition problem, embeddings into QUBO have been formulated.
</div>
<div>
Quantum computers make it possible to find a fairly good solution to this problem. But there are limitations on the use of quantum computers to solve it.
</div>
<h3> Problem </h3>
<div>
1. A small number of qubits, which limits the size of the problem that can be solved.
</div>
<div>
2. Difficulty in understanding and accessing a quantum computer. High requirements for the education of the task manager. As a result, an increase in the cost of staff training. And increase the salary expectations of staff.
</div>
<div>
In a highly competitive environment, companies that can find new optimal solutions will be able to gain a competitive advantage in relation to other companies. Therefore, there is a competition between the complexity of access to quantum computing and the cost of such access. Both hardware and at the level of knowledge.
</div>

### Project idea
<div>
Organize access for a wide range of users to solve the QUBO problem, at the level of setting the QUBO problem. The service will estimate the cost of finding the optimal solution, if the cost satisfies it, it pays for the calculation. And get the best solution.
This will solve the second problem of using quantum computing.
</div>
<div>
To solve the first problem, the service will provide various problem decomposition mechanisms. Breaking them down into smaller problems. It will also allow, on the basis of classical algorithms, to merge a broken task into a single whole.
</div>
<div>
This service may be of interest to researchers of the problem. They will be able to offer their own methods of splitting the task into parts and merging them. And provide your solution on a commercial basis.
</div>
<div>
The service will allow you to create algorithms for bringing applied problems to the QUBO problem, so that users can operate an applied problem formulated in terms of the user
</div>
<div>
The opportunity to make money on quantum computing will attract more enthusiasts who will work and promote quantum computing
</div>
<div>
Also develop a service api, in popular programming languages
</div>
<div>
And make access packages to them
</div>

- npm - package for javascript and typescript
- dart packages - for flutter
- nuget - dot net packages
- maven package - packages for java project
- pip - python
<div>
Develop extensions for MS Excel, MS 
</div>
<div>
This will make it possible to widely apply the formulation and solution of the QUBO problem using quantum computers in a wide range of applications.
</div>

### Areas of work
As part of the hackathon, research was carried out on the possibility of creating such a service.

- Investigation of the relationship between quantum and classical algorithms. 
- Generalization of the QAOA problem to create a service available to users

#### Investigation of the relationship between quantum and classical algorithms. 
#####  made by Oxana

Search for business relevant cases, that be of interest for QC investors. Investigation of the influence of the depth (parameter p) of the circuit of QAOA on the accuracy of the found optimal solution in notebooks  <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/calccost_for_different_depths.ipynb'> and  <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/QUBO_cost_solve_with_different_depths(2).ipynb'>

#### Generalization of the QAOA problem to create a service available to users
#####  made by Konstantin
<div>
In notebook <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/calccost.ipynb'>calccost.ipynb</a>, the calculation of the cost of a quantum circuit is implemented, for various platforms. Platforms differ in the set of basis gates and the cost of their use. This work allows you to evaluate and select the appropriate backend, depending on the number of cubes available and the total cost of executing the algorithm on the backend
</div>
<div>
  Moved code to <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/costdc.py'>costdc.py<a> for reuse
</div>


<div>
In notebook <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/Optimization_pipeline.ipynb'>Optimization_pipeline.ipynb</a>
</div>
<div>
The QUBO problem is formulated as a classical weight matrix problem. Auxiliary algorithms for working with the weight matrix have been implemented. Such as shuffling the weight matrix, dividing the weight matrix into parts. This will reduce the size of the QUBO problem.
</div>

- Implemented a mechanism for constructing graphs based on the matrix of weights.
- The algorithm for constructing a circuit of arbitrary depth is implemented, depending on the parameter p.
- Running the algorithm on an arbitrary backend.
- Processing the results of the algorithm

<div>
  Moved code to <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/qubo.py'>qubo.py</a> for reuse
</div>
<div>
In the <a href='https://github.com/WQ-01-STR/Quantum-approximate-optimisation-algorithms-for-real-world-scenarios---Strangeworks/blob/main/QUBO_cost_solve.ipynb'>QUBO_cost_solve.ipynb</a> notebook
an example of using objects to calculate the cost and solve the QUBO problem
</div>



