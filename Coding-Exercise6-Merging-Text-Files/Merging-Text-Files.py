import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
"""
主要用 glob 抓出所有檔名。

再用file.read把檔內的內容，全部讀出來，

再寫入file中， 而且還記得 多加了換行 。
"""
