from ReactionEnergyDiagram import ReactionEnergyDiagram
rde = ReactionEnergyDiagram(spacing=0.3, epsilon=0.3, figsize=(10,7))

# Add a step
rde.add_step('*',0)
rde.add_step('*O', -0.320865,connect=True, linestyle='dotted', legend=r'RuCrMnO$_2$')
rde.add_step('*OH', 1.424233,connect=True, linestyle='dotted')
rde.add_step('*OOH', 1.508143,connect=True, linestyle='dotted')
rde.add_step(r'O$_2$', 2.308490,connect=True, linestyle='dotted')

# Save the figure as 'ReactionMechanism.png'
rde.plot(save=False, filename='ReactionMechanism.png')
