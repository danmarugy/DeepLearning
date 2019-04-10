import os, sys

class ManageFolder:

    def __init__(self):
        print('ManageFolder의 __init__입니다.')
        self.setWorkFolder()

    def setWorkFolder(self):
        print('작업 폴더  설정 함수')
        print('현재 설정된 작업 폴더는 '+os.getcwd()+'입니다.')
        os.chdir(os.pardir)
        print('현재 설정된 작업 폴더는 ' + os.getcwd() + '입니다.')
        os.chdir(os.pardir)
        print('현재 설정된 작업 폴더는 ' + os.getcwd() + '입니다.')
        os.chdir(os.pardir)
        print('현재 설정된 작업 폴더는 ' + os.getcwd() + '입니다.')
        s = os.listdir(os.getcwd())

    def getWorkFolder(self):
        print('작업 폴더 호출 함수')

    def createFolder(self):
        print('폴더 생성 함수')

    def addFolder(self):
        print('폴더 추가 함수')

    def delFolder(self):
        print('폴더 삭제 함수')

    def saveFolderList(self):
        print('저장할 폴더명 and 경로 리스트 함수')

    def callFolderList(self):
        print('폴더 리스트 읽어 오는 함수')

    def searchFolder(self):
        print('폴더 검색 함수')

if __name__ == "__main__":
    print('FolderManager Main 함수')
    ManageFolder()