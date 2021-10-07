import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from covid_abs.abs import *
from covid_abs.graphics import *
from covid_abs.experiments import batch_experiment

from matplotlib import animation, rc
from IPython.display import HTML

#warnings.simplefilter('ignore')
runname = "_immune"

for i in range(20):
    if not os.path.isdir(f"data{runname}{i}"):
        os.mkdir(f"data{runname}{i}")
        os.mkdir(f"params{runname}{i}")
        print(f"using dir data{runname}{i}")
        dir = i
        break

for i in range(1000000):
    name = f"data{runname}{dir}/dat{i}.csv"
    f = lambda x: lockdown(x, response)
    state_dict = {"initial_infected_perc": 0.02,
                  "initial_immune_perc": np.random.rand()*0.5,
                  "length": 100,
                  "height": 100,
                  "population_size": 118,
                  "contagion_distance": 2,
                  "critical_limit": 0.01,
                  "amplitudes": {
                                  Status.Susceptible: 10,
                                  Status.Recovered_Immune: 10,
                                  Status.Infected: 10,
                                  }
                }
    batch_experiment(1, 100, name, **state_dict)
    amps = state_dict.pop("amplitudes")
    params = pd.DataFrame(state_dict, index=[0])
    params.to_csv(f"params{runname}{dir}/params{i}.csv", index = False)