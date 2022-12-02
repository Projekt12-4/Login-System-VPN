import os
from dataclasses import dataclass, field
import time

@dataclass(kw_only=True)
class DevEnvSetup():

    containerName: str
    user_email: str
    user_name: str
    dir_prefix: str = field(init=False)
    ssh_key_priv: str
    ssh_key_pub: str = field(init=False)  

    def __post_init__(self: object) -> None:
        # Assuming the keys have the same name and are in the same directory
        self.dir_prefix = "$HOME/.ssh/"
        self.ssh_key_priv = f"{self.dir_prefix}{self.ssh_key_priv}"
        self.ssh_key_pub = f"{self.ssh_key_priv}.pub"

    def gitConfig(self: object) -> None:
        # Creating os commands to then be executed by the script
        git_email: str = f'git config user.email "{self.user_email}"'
        git_user: str = f'git config user.name "{self.user_name}"'
        # Execute
        print(f"Executing:\n{git_email}")
        os.system(git_email)
        time.sleep(2)  # Adding time to prevent any potential errors
        print(f"Executing:\n{git_user}")
        os.system(git_user)
    
    def keyConfig(self: object) -> None:
        # Inserting the keys into the devcontainer (WARNING: containername has a cryptic, weird value)
        # user for the container is appuser as defined in the dockerfile
        priv: str = f'docker cp {self.ssh_key_priv} {self.containerName}:/home/appuser/.ssh/'
        pub: str = f'docker cp {self.ssh_key_pub} {self.containerName}:/home/appuser/.ssh/'
        # Execute
        print(f"Executing:\n{priv}")
        os.system(priv)
        time.sleep(2)
        print(f"Executing:\n{pub}")
        os.system(pub)

def main():
    env = DevEnvSetup(containerName="ec6775bf5935", user_email="oleg.ionov@tutanota.de", user_name="xqly-stack", ssh_key_priv="id_ed25519") 
    #containerName=, user_email=, user_name=, ssh_key_priv=
    env.gitConfig()
    env.keyConfig()
    
if __name__ == "__main__":

    main()
