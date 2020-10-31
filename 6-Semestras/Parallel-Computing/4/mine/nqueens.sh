#!/bin/sh
#SBATCH -p short
#SBATCH -n4
#SBATCH -C alpha
mpicc -o nqueens nqueens.c
mpiexec -c 4 ./nqueens