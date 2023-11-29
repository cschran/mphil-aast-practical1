#!/usr/bin/env python

from pathlib import Path
import numpy as np

import aml


# Set random number seed for reproducability
np.random.seed(0)

# load structures
print('Load training set... ', end='', flush=True)

dir_trj = Path('../._RESULTS_/01-AIMD-ice')

# stride through trajectory
stride_trj = 1

print('Reading structures')
print('------------------')
print()
print(f'Directory: {dir_trj}')
print(f'Stride: {stride_trj}')
print()

fn_positions = dir_trj / 'ICE-Ih-pos-1.xyz'
fn_forces = dir_trj / 'ICE-Ih-frc-1.xyz'
cell = np.array([[13.489, 0, 0], [0, 15.576,0], [0, 0, 14.641]])*aml.constants.angstrom

frames = aml.read_frames_cp2k(fn_positions=fn_positions, fn_forces=fn_forces, cell=cell)
structures = aml.Structures.from_frames(frames, stride=stride_trj, probability=1.0)
print()
print(f'Number of structures loaded: {len(structures)}')
print()

# Select 200 random structures for training set
n_train = XXXXXX
train = structures.get(structures.sample(n_train))
print()
print(f'Number of structures for training: {len(train)}')
print()

# construct blank C-NNP object
print('Create blank C-NNP model... ', end='', flush=True)
# settings - n2p2 constructor
kwargs_model = dict(
    elements = ('O', 'H'),
    n = 4,
    fn_template = 'input.nn',
    n_tasks = 4,
    n_core_task = 2
)
n2p2 = aml.N2P2(dir_run=Path('./final-training'), **kwargs_model)
print('done.')
print()

# perform training
print('Train all member models... ', end='', flush=True)
n2p2.train(train, n_epoch=20)
print('done.')
print()

# save final C-NNP model in a format suitable for prediction
print('Save all member models... ', end='', flush=True)
n2p2.save_model()
print('done.')
print()
