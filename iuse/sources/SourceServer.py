

class SourceServer:

    @classmethod
    def generate_path(cls, source):
        cur = source
        path = []
        while cur.parent_dir:
            path.append(cur.name)
            cur = cur.parent_dir
        path.append(cur.name)
        return '/'.join(path[::-1])