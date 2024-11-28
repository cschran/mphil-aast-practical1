source /lsc/opt/intel/setvars.sh
source /data/cerberus1/cs2121/cp2k/tools/toolchain/install/setup
ulimit -s unlimited
#source /data/cerberus1/cs2121/n2p2/env.sh
export PATH="/data/cerberus1/cs2121/n2p2/bin:$PATH"
export LD_LIBRARY_PATH="/data/cerberus1/cs2121/n2p2/lib:$LD_LIBRARY_PATH"
#source /data/cerberus1/cs2121/aml/env.sh
export PYTHONPATH="/data/cerberus1/cs2121/aml/:$PYTHONPATH"
