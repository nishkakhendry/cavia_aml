import json
import matplotlib.pyplot as plt

def get_context_params(json_path):
    with open(json_path, 'r') as f:
        data_dict = json.load(f)

    goal_x = []
    goal_y = []
    cp1 = []	
    cp2 = []
    cp3 = []
    cp4 = []
    cp5 = []
    for batch in data_dict.keys():
        if batch == "batch_500":
            all_tasks = data_dict[batch]["grad_update_2"]
            for task in all_tasks.keys():
                print(all_tasks[task])
                goal_x.append(all_tasks[task]["task"][0])
                goal_y.append(all_tasks[task]["task"][1])
                cp1.append(all_tasks[task]["context_params"][0])
                cp2.append(all_tasks[task]["context_params"][1])
                # cp3.append(all_tasks[task]["context_params"][2])
                # cp4.append(all_tasks[task]["context_params"][3])
                # cp5.append(all_tasks[task]["context_params"][4])

            
    return goal_x, goal_y, cp1, cp2 #, cp3, cp4, cp5

if __name__ == "__main__":
    # json_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/5_lr=0.2tau=1.0_19_03_2025_21_49_46/CAVIA_2D_5cp_task_cp.json"
    # Perfect like paper - 2D CAVIA 200 test 2 cp
    # json_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/2_lr=0.2tau=1.0_20_03_2025_18_50_09/task_cp_2D_CAVIA_2cp_200test.json"
    
    json_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/task_cp.json"
    
    goal_x, goal_y, cp1, cp2 = get_context_params(json_path)
    # goal_x, goal_y, cp1, cp2, cp3, cp4, cp5 = get_context_params(json_path)

    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.scatter(goal_x, goal_y, c=cp1, cmap="viridis")
    # ax2.scatter(goal_x, goal_y, c=cp2, cmap='viridis')
    # plt.show()
    
    fig, axs = plt.subplots(1, 2) #5)
    count = 0
    cps = [cp1, cp2 ]#, cp3, cp4, cp5]
    
    for ax in axs.flat:
        if count == 0:
            ax.set_ylabel('goal_y')
        ax.set_xlabel('goal_x')
        ax.title.set_text(f'Context para {count + 1}')
        sc = ax.scatter(goal_x, goal_y, c=cps[count], cmap="viridis")
        # ax2.scatter(goal_x, goal_y, c=cp2, cmap='viridis')
        # ax3.scatter(goal_x, goal_y, c=cp3, cmap='viridis')
        # ax4.scatter(goal_x, goal_y, c=cp4, cmap='viridis')
        # ax5.scatter(goal_x, goal_y, c=cp5, cmap='viridis')
        count += 1
    
    fig.colorbar(sc, ax=axs)
    # plt.tight_layout()
    plt.show()