def write_log(message):
    with open("logs.csv", "a") as file:
        file.write(message + "\n")