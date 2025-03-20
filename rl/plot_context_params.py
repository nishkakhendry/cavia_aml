import json
import matplotlib.pyplot as plt

def get_context_params(json_path):
    with open(json_path, 'r') as f:
        data_dict = json.load(f)

    goal_x = []
    goal_y = []
    cp1 = []	
    cp2 = []
    for batch in data_dict.keys():
        if batch == "batch_500":
            print(data_dict[batch]["grad_update_2"])
            all_tasks = data_dict[batch]["grad_update_2"]
            for task in all_tasks.keys():
                goal_x.append(all_tasks[task]["task"][0])
                goal_y.append(all_tasks[task]["task"][0])
                cp1.append(all_tasks[task]["context_params"][0])
                cp2.append(all_tasks[task]["context_params"][1])
        # print(data_dict[key])
        # print()
            
if __name__ == "__main__":
    json_path = "C:/Users/nishk/OneDrive/Desktop/LT/cavia_aml/rl/logs/2DNavigation-v0/cavia/5_lr=0.2tau=1.0_19_03_2025_21_49_46/CAVIA_2D_5cp_task_cp.json"
    
    goal_x, goal_y, cp1, cp2 = get_context_params(json_path)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.scatter(goal_x, goal_y, c=cp1, cmap="viridis")
    ax2.scatter(goal_x, goal_y, c=cp2, cmap='viridis')
    plt.show()
    