import hashlib, base64

class UserService():

    @staticmethod
    def genePwd(pwd, salt):
        md = hashlib.md5()
        str = '{}-{}'.format(base64.encodebytes(pwd.encode('utf-8')), salt)
        md.update(str.encode('utf-8')
        return md.hexdigest()