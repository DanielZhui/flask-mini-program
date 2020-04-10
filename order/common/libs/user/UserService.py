import hashlib, base64

class UserService():

    # TODO: 修改 md(), 加密方式, 使用加盐的形式
    @staticmethod
    def genePwd(pwd, salt):
        md = hashlib.md5()
        str = '{}-{}'.format(base64.encodebytes(pwd.encode('utf-8')), salt)
        print(pwd, salt, str)
        md.update(str.encode('utf-8'))
        return md.hexdigest()