from day9_1 import *


class File:
    __slots__ = ['idn', 'size', 'index']
    def __init__(self, idn, size, index) -> None:
        self.idn = idn
        self.size = size
        self.index = index

    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception('Can\'t compare those')
        if self.index == other.index:
            return self.size < other.size
        return self.index < other.index
    
    def is_free_space(self):
        return self.idn == '.'
    
    def get_checksum(self):
        checksum = 0
        for i in range(self.size):
            checksum += (self.index + i) * self.idn
        return checksum
    
    def __repr__(self) -> str:
        return f'{self.idn}, index: {self.index}, size: {self.size}'


def line_to_files_spaces(line):
    files = []
    space = []
    index = 0
    for i in range(len(line)):
        size = int(line[i])
        if size == 0:
            continue
        if i % 2 == 0:
            # files
            files.append(File(i//2, size, index))
        else:
            # free space
            space.append(File('.', int(line[i]), index))
        index += size
    return files, space


def first_fit(file: File, spaces: list[File]):
    '''
    returns the index of the leftmost free space block that could fit the file
    '''
    for space in spaces:
        if space.size < file.size:
            continue
        # if space.index > file.index:
        #     break
        index = space.index
        space.size -= file.size
        space.index += file.size
        # print(f'{file.idn} moves from index {file.index} to index {index}')
        return index
    # print(f'{file.idn} does not move')
    return file.index


def main():
    files, spaces = line_to_files_spaces(DATA)

    files.sort(key=lambda x : x.idn, reverse=True)
    spaces.sort()

    result = 0

    for file in files:
        file.index = first_fit(file, spaces)
        spaces.sort()
        result += file.get_checksum()

    print(result)


if __name__ == '__main__':
    main()
