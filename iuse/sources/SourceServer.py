import os
from iuse.settings import FILE_BASE_DIR, TEST_BASE_DIR
from utils.modelshelpers.enums import FileType, DeleteStatus
from sources.models import Source


class SourceServer:
    @classmethod
    def make_full_path(cls, path):
        """
        用相对路径组装成文件系统路径。
        """
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
        """
        根据路径创建文件夹
        """
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)

    @staticmethod
    def create_file(path, file):
        """
        根据路径创建文件
        """
        try:
            with open(path, 'wb+') as f:
                f.write(file)
        except Exception as e:
            return False
        return True

    @classmethod
    def delete(cls, source):
        """
        真正的删除操作，接收一个资源，凭借出完整路径后删除文件系统中真正的文件。
        """
        path = os.path.join(FILE_BASE_DIR, cls.generate_path(source))
        if int(source.type) == FileType.FILE:
            source.delete()
            try:
                os.remove(path)
            except Exception:
                pass

    @classmethod
    def set_on_delete(cls, source):
        """
        假删除
        """
        # 如果是文件，直接将 on_delete 属性置为 has_delete
        source.on_delete = DeleteStatus.has_deleted
        source.save()
        # 如果是文件夹，需要递归将所有子文件 on_delete 属性置为 has_delete
        if int(source.type) == FileType.DIR:
            children = source.children
            for child in children:
                cls.set_on_delete(child)

    @classmethod
    def recover(cls, source):
        """
        从回收站中恢复
        """
        # 如果是文件，直接将 on_delete 属性置为 exists
        source.on_delete = DeleteStatus.exists
        source.save()
        # 如果是文件夹，则需要递归将所有子文件 on_delete 属性置为 exists
        if int(source.type) == FileType.DIR:
            children = Source.objects.filter(parent_dir=source).all()
            for child in children:
                cls.recover(child)