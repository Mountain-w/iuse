import os


class FileGenerator:
    @classmethod
    def make_file(cls, n, contexts, flag):
        if not os.path.exists('./data'):
            os.mkdir('./data')
        if flag == 'in':
            path = str(n) + '.in'
        elif flag == 'out':
            path = str(n) + '.out'
        with open('data/' + path, 'a+') as f:
            for context in contexts:
                # f.write(str(context) + '\n')
                print(context, file=f)
        return True
