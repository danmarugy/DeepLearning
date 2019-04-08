import os, sys

folder = './setting/'
if not os.path.exists(folder):
    os.makedirs(folder)
f = open(folder+'새파일.txt', 'w')
for message in range(1,20):
    data = "%d째 줄입니다.\n" %message
    f.write(data)

print('done')
f.close()
class exam_file_nw_test:

    def __init__(self):
        print('초기화')

    def _createDir(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(folder+"폴더가 생성되었습니다.")
            return True
        else:
            return False

    def _delDir(folder):
        if os.path.exists(folder):
            os.rmdir(folder)

    def _createFile(folder, filename):
        folder_exist_flag = exam_file_nw_test._createDir(folder)
        if(folder_exist_flag == True):
            f = open(folder+filename+".txt", 'w')
            print(folder+"에 " + filename+ " 파일이 생성되었습니다.")
            f.close()

    def _readFile(folder, filename):
        folder_exist_flag = exam_file_nw_test._createDir(folder)
        if (folder_exist_flag == True):
            f = open(folder+filename+".txt", 'r')
            print("파일을 불러왔습니다.")
            for file_read in f:
                print(file_read)
                f.close()
            else:
                print("읽어올 내용이 없습니다.")
                f.close()

    def _writeFile(folder, filename, message):
        folder_exist_flag = exam_file_nw_test._createDir(folder)
        if (folder_exist_flag == True):
            f = open(folder + filename + ".txt", 'a')
            print("파일을 불러왔습니다.")
            for file_write in message:
                data = file_write
                f.write(data)

    def _delFile(floder, filename):
        folder_exist_flag = exam_file_nw_test._createDir(folder)
        if (folder_exist_flag == True):
            if os.path.isfile(folder+filename):
                os.remove(folder+filename)

        try:
            print("이상 없음")
        except Exception as e:
            print(e)


if __name__ =='__main__':
    print("start")
    exam_file_nw_test()