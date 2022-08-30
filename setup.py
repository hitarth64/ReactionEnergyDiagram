import setuptools

setuptools.setup(name='ReactionEnergyDiagaram',
      version='0.0',
      description='Python package to plot reaction energy diagrams',
      author='Hitarth Choubisa',
      author_email='hitarthc64@gmail.com',
      url='https://github.com/hitarth64/ReactionEnergyDiagram',
      packages=setuptools.find_packages(),
      install_requires=open("requirements.txt", "r").readlines(),
      classifiers = [
            "Programming Language :: Python :: 3",
            "License :: MIT License"
       ],
     )
