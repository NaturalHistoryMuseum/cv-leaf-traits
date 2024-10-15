import os
from leafmachine2.machine.machine import machine
from leafmachine2.machine.general_utils import load_config_file


dir_home = os.path.dirname(os.path.abspath("__file__"))
cfg_file_path = os.path.join(dir_home,'batch_test','LeafMachine2.yaml') 
numpy_path = os.path.join(dir_home,'batch_test','batch_output_numpy') 
cfg_testing = load_config_file(dir_home, cfg_file_path,system='LeafMachine2')
machine(cfg_file_path, dir_home, cfg_testing,numpy_path=numpy_path, save_numpy_only=True)