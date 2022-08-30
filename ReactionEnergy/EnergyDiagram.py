import matplotlib.pyplot as plt

class ReactionEnergyDiagram():

    def __init__(self, epsilon=0.2, spacing=0.01, precision=3, figsize=(7,7)):
        """
        epsilon: represents the horizontal distance between consecutive energy levels
        spacing: represents the distance between labels and energy levels
        precision: precision for representing floats
        figsize: size for the figure
        """
        self.epsilon = epsilon
        self.spacing = spacing
        fig,ax = plt.subplots(figsize=figsize)
        self.ax = ax
        self.fig = fig
        self.lastenergy = 0.0
        self.steps = 0
        self.precision = precision
        self.min = 0.0
        self.legend = False # takes a note if a legend is assigned to any
    
    def add_step(self, label, increment, color='blue', connect=False, linestyle='--', legend=None):
        """
        label: Label for the step
        increment: Energy change (final-initial) in eV
        color: color for the energy levels
        connect: connect energy levels
        linestyle: linestyle for the connecting lines
        legend: legend for the corresponding energy level
        """
        if legend is None:
            self.ax.plot([self.steps+self.epsilon, self.steps+1], [self.lastenergy+increment]*2, c=color)
        else:
            self.legend = True
            self.ax.plot([self.steps+self.epsilon, self.steps+1], [self.lastenergy+increment]*2, c=color, label=legend)
            
        if type(label) == float:
            self.ax.annotate(str(round(label,self.precision)), (self.steps+0.5+self.epsilon/2.0, increment+self.lastenergy-self.spacing))
        elif type(label) == str:
            self.ax.annotate(label, (self.steps+0.5+self.epsilon/2.0, increment+self.lastenergy-self.spacing))
            
        if connect:
            self.ax.plot([self.steps, self.steps+self.epsilon],[self.lastenergy, self.lastenergy+increment],linestyle=linestyle,c=color)
        
        self.steps += 1
        self.lastenergy = self.lastenergy + increment
        self.min = min(self.min, self.lastenergy)
    
    def plot(self, xlabel='Reaction coordinate', ylabel='Reaction energy (eV)', LabelFontsize=14, TicksFontsize=12, save=True, filename='ReactionMechanism.png'):
        """
        plots the diagram
        """
        plt.ylim(self.min-3*self.spacing)
        plt.xticks([])
        plt.xlabel(xlabel,fontsize=LabelFontsize)
        plt.ylabel('Reaction energy (eV)',fontsize=LabelFontsize)
        plt.yticks(fontsize=TicksFontsize)
        if self.legend:
            plt.legend(loc='upper left',fontsize=LabelFontsize)
            
        if save:
            self.fig.savefig(filename,transparent=True,dpi=300)
            
        return self.fig.show()
    
    def superimpose(self):
        """
        Call this function to enable superimposition of another reaction energy diagram on the existing one
        """
        self.lastenergy = 0.0
        self.steps = 0
        self.min = 0.0        
