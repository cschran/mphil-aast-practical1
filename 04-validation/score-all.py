#!/usr/bin/env python

import aml
import aml.score as mlps
import numpy as np


# settings - original AIMD trajectory
dt_ref = 4
dir_AIMD = '../._RESULTS_/01-AIMD-ice/'
fn_trj_ref = dir_AIMD + 'ICE-Ih-pos-1.xyz'
fn_frc_ref = dir_AIMD + 'ICE-Ih-frc-1.xyz'
fn_vel_ref = dir_AIMD + 'ICE-Ih-vel-1.xyz'
fn_topo_ref = dir_AIMD + 'ice-Ih.pdb'

# settings - C-NNP model
dir_model = '../._RESULTS_/02-MLP-train/model/'

# settings - C-NNP trajectory
dt_test = 4
dir_C_NNP = '../03-MLP-ice/'
fn_trj_test = dir_C_NNP + 'ICE-Ih-pos-1.xyz'
fn_vel_test = dir_C_NNP + 'ICE-Ih-vel-1.xyz'
fn_topo_test = dir_AIMD + 'ice-Ih.pdb'

# load position trajectory
trj_ref = mlps.load_with_cell(fn_trj_ref, top=fn_topo_ref)
trj_test = mlps.load_with_cell(fn_trj_test, top=fn_topo_test)

# perform RDF scoring
mlps.run_rdf_test(trj_ref, trj_test)

# load velocity trajectory
vel_ref = mlps.load_with_cell(fn_vel_ref, top=fn_topo_ref)
vel_test = mlps.load_with_cell(fn_vel_test, top=fn_topo_test)

# perform VDOS scoring
mlps.run_vdos_test(vel_ref, dt_ref, vel_test, dt_test)

# read AIMD trajectory positions and forces
cell = np.array([[13.489, 0, 0], [0, 15.576,0], [0, 0, 14.641]])*aml.constants.angstrom
frames = aml.read_frames_cp2k(fn_positions=fn_trj_ref, fn_forces=fn_frc_ref, cell=cell)
structures_ref = aml.Structures.from_frames(frames, stride=1, probability=1.0)

# perform force RMSE scoring
mlps.run_rmse_test(dir_model, fn_topo_ref, structures_ref)
