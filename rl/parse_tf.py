import os
import pandas as pd
from tensorflow.python.summary.summary_iterator import summary_iterator

def parse_tfevent_log(root_dir):
    file_full_path = os.path.join(root_dir)
    for e in summary_iterator(file_full_path):
        print(e.summary.value)
        # for value in e.summary.value:
        #     if "rew" in value.tag:
        #         print(e.summary.value)
        #         # print(value.simple_value)
            

if __name__ == "__main__":
    # dir_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/cavia/"
    # exp_name = "2_lr=1.0tau=1.0_11_03_2025_17_38_49/events.out.tfevents.1741714729.e0822e68336f"    
    # parse_tfevent_log(f"{dir_path}/{exp_name}")

    # # HalfCheetahDir-v1 CAVIA
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/cavia/50_lr=10tau=1.0_14_03_2025_19_50_07/events.out.tfevents.1741981807.4390cb3eb32b"
    # # HalfCheetahDir-v1 MAML
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/maml/lr=10tau=1.0_16_03_2025_23_02_25/events.out.tfevents.1742166145.d2d58bd675f2"
    
    # 2dNavigation-v0 CAVIA
    # # 2 CP - old (no json)
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0_old/cavia/2_lr=1.0tau=1.0_13_03_2025_02_20_16/events.out.tfevents.1741832416.d91585773a5e"
    # # 2 CP - new (with json)
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/2_lr=0.2tau=1.0_20_03_2025_18_50_09/events.out.tfevents.1742496609.e8faa17b3fb1"
    
    
    # 5 CP
    log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/5_lr=0.2tau=1.0_19_03_2025_21_49_46/events.out.tfevents.1742420986.e8faa17b3fb1"


    # # 2dNavigation-v0 MAML
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/maml/lr=10tau=1.0_16_03_2025_23_02_25/events.out.tfevents.1742166145.d2d58bd675f2"
    
    
    parse_tfevent_log(log_path)
