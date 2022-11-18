import os

def install():
    install_dependencies_linux = "pip3 install -r requirements.txt"
    os.system(install_dependencies_linux)
    print ("It is strongly advised that you run start.py thereafter!")

if __name__ == "__main__":

    install()

