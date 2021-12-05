import os, sys

from cmdstanpy import CmdStanModel, cmdstan_path

# /root/.cmdstan/cmdstan-2.28.2/examples/bernoulli/bernoulli.stan
stan_file = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.stan')
if sys.argv[1] == '1':
    model = CmdStanModel(stan_file=stan_file, cpp_options={'STAN_THREADS': True, 'STAN_OPENCL': True})
    if sys.argv[2] == 'c':
        model.compile(force=True, cpp_options={'STAN_THREADS': True, 'STAN_OPENCL': True})
else:
    model = CmdStanModel(stan_file=stan_file)
    if sys.argv[2] == 'c':
        model.compile(force=True)
data_file = os.path.join(os.path.dirname(__file__), 'example.json')
fit = model.sample(data=data_file)

