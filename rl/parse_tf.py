import os
import pandas as pd
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt


def parse_tfevent_log(root_dir):
    file_full_path = os.path.join(root_dir)
    all_train_returns = [] 
    for e in summary_iterator(file_full_path):
        # print(e.summary.value)
        for value in e.summary.value:
            if "returns/after_update" in value.tag:
                print("train returns: ", value.simple_value)
                all_train_returns.append(value.simple_value)
    # print("----------------",all_train_returns)
    try:
        print("train rewards max at ======== ", all_train_returns.index(max(all_train_returns)), " -- ", max(all_train_returns))
    except:
        print("No max training rew policy")

    final_rewards = []
    # extract final_evaluation_rew
    for e in summary_iterator(file_full_path):
        print(e.summary.value)
        for value in e.summary.value:
            if "final_evaluation_rew/avg_rew_" in value.tag:
                # print(e.summary.value)
                final_rewards.append(value.simple_value)

    return final_rewards


if __name__ == "__main__":
    # dir_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/cavia/"
    # exp_name = "2_lr=1.0tau=1.0_11_03_2025_17_38_49/events.out.tfevents.1741714729.e0822e68336f"    
    # parse_tfevent_log(f"{dir_path}/{exp_name}")

    # # # HalfCheetahDir-v1 CAVIA
    # log_path = "./logs/HalfCheetahDir-v1/cavia/50_lr=10tau=1.0_14_03_2025_19_50_07/events.out.tfevents.1741981807.4390cb3eb32b"
    # retry with lr 10 - garbage?
    # log_path = "./logs/HalfCheetahDir-v1/cavia/50_lr=10tau=1.0_28_03_2025_22_55_32/events.out.tfevents.1743202532.5d79741406fa"
    # # retry with lr 1
    # log_path = "./logs/HalfCheetahDir-v1/cavia/50_lr=1.0tau=1.0_29_03_2025_00_03_21/events.out.tfevents.1743206601.5d79741406fa"

    # HalfCheetahDir-v1 MAML
    # old yucky
    # log_path = "./logs/HalfCheetahDir-v1/maml/lr=10tau=1.0_16_03_2025_23_02_25/events.out.tfevents.1742166145.d2d58bd675f2"
    # actual working version - lr 0.1
    # log_path = "./logs/HalfCheetahDir-v1/maml/lr=0.1tau=1.0_27_03_2025_13_05_22/events.out.tfevents.1743080722.5d79741406fa"
    log_path = "./logs/HalfCheetahDir-v1/maml_test/lr=0.1tau=1.0_28_03_2025_22_27_20/events.out.tfevents.1743200840.5d79741406fa"   # load and test

    # 2dNavigation-v0 CAVIA
    # # 2 CP - old (no json)
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0_old/cavia/2_lr=1.0tau=1.0_13_03_2025_02_20_16/events.out.tfevents.1741832416.d91585773a5e"
    
    # 2 CP - new (with json) -- Perfect like paper
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/2_lr=0.2tau=1.0_20_03_2025_18_50_09/events.out.tfevents.1742496609.e8faa17b3fb1"
    # log_path = "./logs/2DNavigation-v0/cavia/2_lr=0.2tau=1.0_20_03_2025_18_50_09/events.out.tfevents.1742496609.e8faa17b3fb1"
    
    # # 2 CP - new but with policy 455 (max rew at train)
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia_test/2_lr=0.2tau=1.0_21_03_2025_22_11_59/events.out.tfevents.1742595119.e8faa17b3fb1"
    
    # # 5 CP
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/5_lr=0.2tau=1.0_19_03_2025_21_49_46/events.out.tfevents.1742420986.e8faa17b3fb1"
    # # 5 CP load and test
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia_test/5_lr=0.2tau=1.0_21_03_2025_13_21_30/events.out.tfevents.1742563290.e8faa17b3fb1"
    # # 5 CP load and test - policy 493
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia_test/5_lr=0.2tau=1.0_21_03_2025_16_24_48/events.out.tfevents.1742574288.e8faa17b3fb1"
    # 2dNavigation-v0 MAML
    # old yucky
    # log_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/HalfCheetahDir-v1/maml/lr=10tau=1.0_16_03_2025_23_02_25/events.out.tfevents.1742166145.d2d58bd675f2"
    # log_path = "./logs/HalfCheetahDir-v1/maml/lr=10tau=1.0_16_03_2025_23_02_25/events.out.tfevents.1742166145.d2d58bd675f2"

    # proper run
    # log_path = "./logs/2DNavigation-v0/maml/lr=0.2tau=1.0_26_03_2025_21_21_00/events.out.tfevents.1743024060.5d79741406fa" # only train
    # log_path = "./logs/2DNavigation-v0/maml/lr=1.0tau=1.0_18_03_2025_12_07_09/events.out.tfevents.1742299629.d2d58bd675f2" # only test

    
    
    eval_rew_CAVIA = parse_tfevent_log(log_path)
    # eval_rew_MAML = [-39.039867,-23.698885,-23.936651,-25.565693, -19.127525, -21.256426] # 2D - from last eval in only train log 
    
    # eval_rew_CAVIA = []
    eval_rew_MAML = [-27.296541,420.20038,499.67142,475.71887,467.92648,459.78778] # HC - from last eval in only train log 
    
    until = 4
    grad_updates = [0, 1, 2, 3, 4,5]
    # plt.plot(grad_updates, eval_rew, label='CAVIA')
    plt.plot(grad_updates[:until], eval_rew_CAVIA[:until], marker="o", label='CAVIA')
    plt.plot(grad_updates[:until], eval_rew_MAML[:until], marker="o", label='MAML')
    plt.xticks(grad_updates[:until], grad_updates[:until])
    plt.legend()
    plt.xlabel('Number of inner updates')
    plt.ylabel('Total reward')
    # plt.title('2D Navigation Env')
    plt.title('HalfCheetah Direction Env')
    plt.show()

