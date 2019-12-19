
import os
import time
import re
def getCodeFromSms(timeout=20):
    file = "D:\logcat.txt"
    if os.path.exists(file):
        os.remove(file)
    n = 0
    smscode = ""
    pattern = re.compile(r"验证码：([0-9]+)")
    while n < timeout:
        os.system("adb logcat -c")
        time.sleep(2)
        n += 2
        print(n)
        cmd = r'adb logcat -d >D:\logcat.txt'
        os.system(cmd)
        with open("D:\logcat.txt",mode='r',encoding='utf-8') as log:
            for line in log:
                if "验证码" in line:
                    search = re.search(pattern, line)
                    if search:
                        print(line)
                        smscode = search.group(1)
                        print(smscode)
                        break
        if smscode:
            break

    return smscode
# print(getCodeFromSms())