# ReactionEnergyDiagram: Plotting reaction mechanisms and reaction energetics using Python

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
   
- An example for showing Oxygen Evolution Reaction (OER) over RuCrMnO$_2$ catalyst (from [here](https://arxiv.org/abs/2205.09007))
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

- You can find some other examples in the examples folder

### License:
```ReactionEnergyDiagram``` is released under the MIT License. 

### Citation:
- This package was developed to plot energy diagrams used for [our paper](https://arxiv.org/abs/2205.09007)
- Therefore, to cite the package, please use the following bibtex:
```
@article{choubisa2022accelerated,
  title={Accelerated chemical space search using a quantum-inspired cluster expansion approach},
  author={Choubisa, Hitarth and Abed, Jehad and Mendoza, Douglas and Yao, Zhenpeng and Wang, Ziyun and Sutherland, Brandon and Aspuru-Guzik, Al{\'a}n and Sargent, Edward H},
  journal={arXiv preprint arXiv:2205.09007},
  year={2022}
}
```
