from pyftpdlib.authorizers import DummyAuthorizer  # 사용자 인증을 생성하는 모듈
from pyftpdlib.handlers import FTPHandler  # 사용자 인증, 파일 전송, 로깅 등 FTP서버를 조작하는 모듈
from pyftpdlib.servers import FTPServer  # FTP서버를 실행하는 모듈

import os

class FileServer:
    def __init__(self):
        self.ftpServerIP = "0.0.0.0"
        self.ftpServerPort = 21

        self.userId = "hyuna"
        self.userPassword = "980330"
        self.userDir = "C:\\FTEST"  #경로

    def start(self):
        # 계정별 디렉토리 생성
        if not (os.path.exists(self.userDir)):
            os.makedirs(self.userDir, exist_ok=True)
        # FTP Server 계정 추가
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.userId, self.userPassword, self.userDir, perm="elradfmwMT")  # 모든 권한(elradfmw)을 부여

        handler = FTPHandler
        handler.banner = "pyftpdlib based ftpd ready."  # 배너 설정

        handler.authorizer = authorizer
        handler.passive_ports = range(60000, 65535)  # 패시브통신 포트지정

        address = (self.ftpServerIP, self.ftpServerPort)  # FTP 서버주소 및 포트설정
        server = FTPServer(address, handler)

        server.max_cons = 50  # 최대 연결 개수
        server.max_cons_per_ip = 5  # IP당 최대 연결 개수
        print(f'[FileServer] Share Dir = {self.userDir}')
        server.serve_forever()

file_server = FileServer()
file_server.start()