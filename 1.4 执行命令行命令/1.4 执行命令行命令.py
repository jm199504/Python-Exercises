import subprocess

for i in range(1, 11):
    command = f"touch {i}.txt"
    subprocess.run(command, shell=True)
