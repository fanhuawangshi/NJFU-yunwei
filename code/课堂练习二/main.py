import os
from urllib.request import urlopen

if __name__ == "__main__":
    # os.system("start http://www.baidu.com")
    from urllib.request import urlopen
    with urlopen('https://www.baidu.com/') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
            print(line)
