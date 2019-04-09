import os, sys

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

class exam_file_nw_test:

    create_folder_list = []
    '''efnt = exam_file_nw_test()'''

    def __init__(self):
        print('초기화')
        exam_file_nw_test._menu_list(self)
        '''efnt._menu_list(self)'''

    def _createDir(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(folder+"폴더가 생성되었습니다.")
            return True
        else:
            print(folder +"는 이미 생성되어있습니다.")
            return False

    def _delDir(folder):
        if os.path.exists(folder):
            os.rmdir(folder)

    def _listDir():
        print("저장된 폴더리스트를 불러옵니다")

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

    def _delFile(folder, filename):
        folder_exist_flag = exam_file_nw_test._createDir(folder)
        if (folder_exist_flag == True):
            if os.path.isfile(folder+filename):
                os.remove(folder+filename)

        try:
            print("이상 없음")
        except Exception as e:
            print(e)

    def _menu_list(self):
        flag = True
        print("1 : 폴더생성 2: 폴더삭제 3: 생성된 폴더리스트 4: 파일생성 5: 파일 쓰기 6: 파일 읽기 7: 파일 지우기 0 : 종료")
        while(flag):
            try:
                select_menu =  int(input('원하시는 작업을 선택해주세요.'))
            except ValueError as ve:
                print("지정된 숫자를 입력바랍니다.")
            print(type(select_menu))
            if(select_menu == 1):
                folder_name = input("생성할 폴더명을 입력 : ")
                exam_file_nw_test._createDir(folder_name)
                exam_file_nw_test.create_folder_list.append(folder_name)
            elif(select_menu == 3):
                exam_file_nw_test._listDir()
            elif(select_menu == 0):
                print("프로그램을 종료합니다.")
                flag = False



if __name__ =='__main__':
    print("start")
    exam_file_nw_test()