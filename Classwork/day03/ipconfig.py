import subprocess

def extractPhyIP():
    phy = []
    content = subprocess.check_output('ipconfig -all')
    content = str(content)
    content = content.split("\\r\\n")
     for line in content:
        if("Physical Address" in line):
            phy.append(line)

    return phy
