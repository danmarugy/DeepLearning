import os

folder = './setting/'
if not os.path.exists(folder):
    os.makedirs(folder)
f = open(folder+'새파일.txt', 'w')
for message in range(1,20):
    data = "%d째 줄입니다.\n" %message
    f.write(data)

print('done')
f.close()


def __init__(self):

def _createDir():
    if not os.path.exists(folder):
        os.makedirs(folder)
def _delDir():
def _createFile():
def _readFile():
def _writeFile():
def _addFile():
def _delFile():

if __name__ =='__main__':
    print("start")