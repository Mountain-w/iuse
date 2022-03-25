import os
from iuse.settings import FILE_BASE_DIR, TEST_BASE_DIR
from utils.modelshelpers.enums import FileType
from sources.models import Source


class SourceServer:
    @classmethod
    def make_full_path(cls, path):
        full_path = os.path.join(FILE_BASE_DIR, path)
        return full_path

    @classmethod
    def generate_path(cls, source):
        """
        接受一个资源对象，创建出它的路径
        缓存中如果存在就直接返回path
        """
        cur = source
        path = []
        while cur.parent_dir:
            path.append(cur.name)
            cur = cur.parent_dir
        path.append(cur.name)
        return '/'.join(path[::-1])

    @classmethod
    def create_sources(cls, source, file=None):
        """
        接受一个资源对象，一个二进制文件流（为空时创建文件夹）
        """
        path = os.path.join(FILE_BASE_DIR, cls.generate_path(source))
        if source.type == FileType.DIR:
            SourceServer.create_dir(path)
        else:
            if not SourceServer.create_file(path, file):
                return False
        return True

    @classmethod
    def create_sources_for_test(cls, source, file=None):
        """
        接受一个资源对象，一个二进制文件流（为空时创建文件夹）
        """
        path = os.path.join(TEST_BASE_DIR, cls.generate_path(source))
        if source.type == FileType.DIR:
            SourceServer.create_dir(path)
        else:
            if not SourceServer.create_file(path, file):
                return False
        return True

    @staticmethod
    def create_dir(path):
        print(path)
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)

    @staticmethod
    def create_file(path, file):
        try:
            with open(path, 'wb+') as f:
                f.write(file)
        except Exception as e:
            return False
        return True