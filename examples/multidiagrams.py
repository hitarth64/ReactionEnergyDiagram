from ReactionEnergyDiagram import ReactionEnergyDiagram
red = ReactionEnergyDiagram(spacing=0.3, epsilon=0.3, figsize=(10,7))

red.add_step('*',0)
red.add_step('*O', -0.320865,connect=True, linestyle='dotted', legend=r'RuCrMnO$_2$')
red.add_step('*OH', 1.424233,connect=True, linestyle='dotted')
red.add_step('*OOH', 1.508143,connect=True, linestyle='dotted')
red.add_step(r'O$_2$', 2.308490,connect=True, linestyle='dotted')

# Use superimpose to add another reaction to the same figure
red.superimpose() 
red.add_step('*',0)
red.add_step(None, -1.140617,connect=True, linestyle='dotted', color='red', legend=r'RuCrMnSbO$_2$')
red.add_step(None, 2.097738,connect=True, linestyle='dotted', color='red')
red.add_step(None, 1.792776,connect=True, linestyle='dotted', color='red')
red.add_step(None, 2.170103,connect=True, linestyle='dotted', color='red')

# Save the figure as 'TwoReactionMechanisms.png'
red.plot(save=False, filename='TwoReactionMechanisms.png', transparent=False)
