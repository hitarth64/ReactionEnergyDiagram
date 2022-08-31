# ReactionEnergyDiagram [RED]: Plotting reaction mechanisms and reaction energetics using Python

## Table of Contents

- [Installation](#how-to-install)
- [Structure of the repository](#structure-of-the-repository)
- [Usage](#usage)
- [License](#license)
- [How to cite](#citation)

### How to install: 
- You can install the library as: ```pip install git+https://github.com/hitarth64/ReactionEnergyDiagram```

### Structure of the repository:
- Most of the functionality is contained inside the ```ReactionEnergyDiagaram/ReactionEnergyDiagaram.py```

### Usage:
- To use the ```ReactionEnergyDiagram``` package, simply import it as:

   ```from ReactionEnergyDiagram import ReactionEnergyDiagram```
   
- An example for showing Oxygen Evolution Reaction (OER) over RuCrMnO<sub>2</sub> catalyst 
   ```
   from ReactionEnergyDiagram import ReactionEnergyDiagram
   rde = ReactionEnergyDiagram(spacing=0.3, epsilon=0.3, figsize=(10,7))
   
   rde.add_step('*',0)
   rde.add_step('*O', -0.320865,connect=True, linestyle='dotted', legend=r'RuCrMnO$_2$')
   rde.add_step('*OH', 1.424233,connect=True, linestyle='dotted')
   rde.add_step('*OOH', 1.508143,connect=True, linestyle='dotted')
   rde.add_step(r'O$_2$', 2.308490,connect=True, linestyle='dotted')
   
   # Save the figure as 'ReactionMechanism.png'
   rde.plot(save=False, filename='ReactionMechanism.png')
   ```
   
   The result is:
   ![SingleReaction](https://github.com/hitarth64/ReactionEnergyDiagram/blob/main/examples/ReactionMechanism.png)

- You can also plot multiple reactions in the same diagram to compare different reaction energetics and pathways. Key is to use ```superimpose``` function before inserting a new reaction.
   ```
   from ReactionEnergyDiagram import ReactionEnergyDiagram
   red = ReactionEnergyDiagram(spacing=0.3, epsilon=0.3, figsize=(10,7))
   
   red.add_step('*',0)
   red.add_step('*O', -0.320865,connect=True, linestyle='dotted', legend=r'RuCrMnO$_2$')
   red.add_step('*OH', 1.424233,connect=True, linestyle='dotted')
   red.add_step('*OOH', 1.508143,connect=True, linestyle='dotted')
   red.add_step(r'O$_2$', 2.308490,connect=True, linestyle='dotted')
   
   red.superimpose() # resets the internal counters and pointers
   red.add_step('*',0)
   red.add_step(None, -1.140617,connect=True, linestyle='dotted', color='red', legend=r'RuCrMnSbO$_2$')
   red.add_step(None, 2.097738,connect=True, linestyle='dotted', color='red')
   red.add_step(None, 1.792776,connect=True, linestyle='dotted', color='red')
   red.add_step(None, 2.170103,connect=True, linestyle='dotted', color='red')
   
   # Save the figure as 'ReactionMechanism.png'
   rde.plot(save=False, filename='TwoReactionMechanisms.png')
   ```
   The result is:
   
   ![SingleReaction](https://github.com/hitarth64/ReactionEnergyDiagram/blob/main/examples/TwoReactionMechanisms.png)

### License:
```ReactionEnergyDiagram``` is released under the MIT License. 
