import os
import subprocess

shutdown = input("Do you want to shutdown? (yes/no): ")

if shutdown == 'yes':
    try:
        subprocess.run(['sudo', 'shutdown', '-h', 'now'])
    except Exception as e:
        print(f"Error: {e}")
else:
    print('Shutdown is not required')
