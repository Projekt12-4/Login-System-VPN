import os 

def start():

    start_command_env = os.environ.get("START_SERVER_SHELL") 
    db_secret_key_env = os.environ.get("DB_SECRET_KEY")

        
    if start_command_env and db_secret_key_env is None:
        print(f"---------------------------------\n[WARN-NO_ENV_VAR]\n$START_SERVER_SHELL: {start_command_env}\n$DB_SECRET_KEY {db_secret_key_env}\nNo environment variables detected!\n---------------------------------")            
        exit(0)

    else:
        print(f"---------------------------------\n[INFO-ENV_VAR]\n$START_SERVER_SHELL: {start_command_env}\n$DB_SECRET_KEY: {db_secret_key_env}\n---------------------------------")
        os.system(start_command_env)



if __name__ == "__main__":

    start()