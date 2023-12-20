from operator import itemgetter

class disk:
    """Диск"""
    def __init__(self, id, name, size, ShelfId):
        self.id = id
        self.name = name
        self.size = size                                       #В секундах
        self.ShelfId = ShelfId
 
class Shelf:
    """Полка"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class diskShelf:
    """
    'Диски Полки' для реализации
    связи многие-ко-многим
    """
    def __init__(self, ShelfId, diskId):
        self.ShelfId = ShelfId
        self.diskId = diskId

Shelfs = [Shelf(1, "Металл"),
        Shelf(2, "Рок-Н-Ролл"),
        Shelf(3, "Хардстайл")]

disks = [disk(1,"MetallicA",1134,1),
         disk(2,"Mашина времени",2517,2),
         disk(3,"Bladee Mixtape",1488,3),
         disk(4,"Elvis Presley",1860,2),
         disk(5,"SOAD Mezmerize",3252,1)
         ]

disksShelfs = [diskShelf(1,1),
             diskShelf(2,2),
             diskShelf(1,3),
             diskShelf(3,3)]

ShelfsId = [c.id for c in Shelfs]

OneToMany = [(f.name, f.size, Shelfs[ShelfsId.index(f.ShelfId)].name) for f in disks]

disksId = [f.id for f in disks]

ManyToMany = [(disks[disksId.index(fc.diskId)].name,
                   disks[disksId.index(fc.diskId)].size,
                   Shelfs[ShelfsId.index(fc.ShelfId)].name)
                  for fc in disksShelfs]

def task1(OneToMany):
    word1 = "а"
    ShelfsE1 = [c.name for c in Shelfs if word1 in c.name]
    disksE1 = [otm[0] for otm in OneToMany for c in ShelfsE1 if otm[2] == c]
    return ShelfsE1,disksE1

def task2(OneToMany):
    return sorted([[c.name, round(sum([otm[1] for otm in OneToMany if otm[2] == c.name])/(lambda x: 1 if x==0 else x)(len([otm[1] for otm in OneToMany if otm[2] == c.name])))] for c in Shelfs], key=itemgetter(1),reverse=True)

def task3(ManyToMany):
    char3 = "M"
    return [[f.name,[mtm[2] for mtm in ManyToMany if mtm[0]==f.name]] for f in disks if f.name[0] == char3]

if __name__ == '__main__':
    print(task1(OneToMany))
    print(task2(OneToMany))
    print(task3(ManyToMany))






















