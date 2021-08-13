import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from covid_abs.abs import *
from covid_abs.graphics import *
from covid_abs.experiments import batch_experiment

from matplotlib import animation, rc
from IPython.display import HTML

warnings.simplefilter('ignore')

for i in range(1000000):
    name = f"data2/dat{i}.csv"
    state_dict = {"initial_infected_perc": np.random.rand()*0.1,
                  "length": 100,
                  "height": 100,
                  "population_size": int(np.random.rand()*100)+1,
                  "contagion_distance": np.random.rand()*10,
                  "critical_limit": np.random.rand()*0.1,
                  "amplitudes": {
                                  Status.Susceptible: np.random.rand()*10,
                                  Status.Recovered_Immune: np.random.rand()*10,
                                  Status.Infected: np.random.rand()*10,
                                  }
                 }
    batch_experiment(10, 50+int(np.random.rand()*100), name, **state_dict)
    amps = state_dict.pop("amplitudes")
    state_dict["amp_susc"] = amps[Status.Susceptible]
    state_dict["amp_rec"] = amps[Status.Recovered_Immune]
    state_dict["amp_inf"] = amps[Status.Infected]
     
    params = pd.DataFrame(state_dict, index=[0])
    params.to_csv(f"params/params{i}.csv", index = False)