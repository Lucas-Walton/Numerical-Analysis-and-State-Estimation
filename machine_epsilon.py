## Find Machine Epsilon
def machine_epsilon():
    epsilon = 1.0
    while (1 < 1 + epsilon):
        epsilon = epsilon/2.0

    epsilon*= 2.0
    return

if __name__ == "__main__":
    print("Machine epsilon:", machine_epsilon())