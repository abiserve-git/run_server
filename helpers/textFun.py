from colorama import Fore
from colorama import Style


def Tred(text):
    print(f"_______________❌ {Fore.RED}{text}{Style.RESET_ALL} ❌_______________")
    
    
def Tgreen(text):
    print(f"_______________  ✅ {Fore.GREEN}{text}{Style.RESET_ALL} ✅_______________")

def Tyellow(text):
    print(f"_______________⚠️ {Fore.YELLOW}{text}{Style.RESET_ALL} ⚠️_______________")