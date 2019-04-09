import os, sys
import json
from collections import OrderedDict

'''
folder = './setting/'
if not os.path.exists(folder):
    os.makedirs(folder)
f = open(folder+'새파일.txt', 'w')
for message in range(1,20):
    data = "%d째 줄입니다.\n" %message
    f.write(data)
print('done')
f.close()
'''

class FileManagement:

    dir_data = OrderedDict()

    def __init__(self):
        print('초기화')
        os.chdir(os.pardir)
        if __name__ == '__main__':
            self.menu_list()


    def _createDir(self, folder):

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(folder+"폴더가 생성되었습니다.")
            self._savelistDir(folder)
            return True
        else:
            print(folder +"는 이미 생성되어있습니다.")
            return False

    def _delDir(self, folder):
        if os.path.exists(folder):
            os.rmdir(folder)

    def _listDir(self):
        print("저장된 폴더리스트를 불러옵니다")

    def _savelistDir(self, folder):
        setfolderlist = "list"
        if not os.path.exists(setfolderlist):
            os.makedirs(setfolderlist)
            self.dir_data["Name"] = folder
            print(self.dir_data["Name"])
            with open(setfolderlist+'/listDir.json', 'w', encoding="utf-8") as make_file:
                json.dump(self.dir_data, make_file, ensure_ascii=False, indent="\t")

        else:
            os.makedirs(setfolderlist)
            self.dir_data["Name"] = folder
            print(self.dir_data["Name"])
            with open(setfolderlist + '/listDir.json', 'a', encoding="utf-8") as make_file:
                json.dump(self.dir_data, make_file, ensure_ascii=False, indent="\t")


    def _loadlistDir(self):
        print("xxxxxx")

    def _createFile(self, folder, filename):
        folder_exist_flag = self._createDir(folder)
        if(folder_exist_flag == True):
            f = open(folder+filename+".txt", 'w')
            print(folder+"에 " + filename+ " 파일이 생성되었습니다.")
            f.close()


    def _readFile(self, folder, filename):
        folder_exist_flag = FileManagement._createDir(folder)
        if (folder_exist_flag == True):
            f = open(folder+filename+".txt", 'r')
            print("파일을 불러왔습니다.")
            for file_read in f:
                print(file_read)
                f.close()
            else:
                print("읽어올 내용이 없습니다.")
                f.close()
    def _writeFile(self, folder, filename, message):
        folder_exist_flag = FileManagement._createDir(folder)
        if (folder_exist_flag == True):
            f = open(folder + filename + ".txt", 'a')
            print("파일을 불러왔습니다.")
            for file_write in message:
                data = file_write
                f.write(data)

    def _delFile(self, floder, filename):
        print("hello")


    def _delFile(self, folder, filename):
        folder_exist_flag = FileManagement._createDir(folder)
        if (folder_exist_flag == True):
            if os.path.isfile(folder+filename):
                os.remove(folder+filename)
        try:
            print("이상 없음")
        except Exception as e:
            print(e)

    def menu_list(self):
        flag = True
        '''print("1 : 폴더생성 2: 폴더삭제 3: 생성된 폴더리스트 4: 파일생성 5: 파일 쓰기 6: 파일 읽기 7: 파일 지우기 0 : 종료")'''
        while(flag):
            try:
                print("1 : 폴더생성 2: 폴더삭제 3: 생성된 폴더리스트 4: 파일생성 5: 파일 쓰기 6: 파일 읽기 7: 파일 지우기 0 : 종료")
                select_menu =  int(input('원하시는 작업을 선택해주세요.'))
            except ValueError as ve:
                print("지정된 숫자를 입력바랍니다.")
                continue
            '''print(type(select_menu))'''
            if(select_menu == 1):
                folder_name = input("생성할 폴더명을 입력 : ")
                self._createDir(folder_name)
                '''self.create_folder_list.append(folder_name)'''
            elif(select_menu == 3):
                self._listDir()
            elif(select_menu == 0):
                print("프로그램을 종료합니다.")
                flag = False



if __name__ =='__main__':
    print("start")
    FileManagement()