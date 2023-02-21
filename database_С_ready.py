import pickle

MAX_COUNT = 3

CMD_SHOW = 1
CMD_ADD = 2
CMD_DELETE = 3
CMD_SORT_NAME = 4
CMD_SORT_TYPE = 5
CMD_EXIT = 6

dbName = 'zoo.dat'

class TAnimal:
  name = ''
  typ = ''
  age = 0

Animals = []

#-----------------------------------
#  READ DATABASE - чтение данных из файла
#-----------------------------------
def readDatabase():
  global Animals
  print('\nЧитаем базу данных...')
  F = open( dbName, "rb" )
  Animals = pickle.load( F )
  F.close()

#-----------------------------------
#  SAVE DATABASE - запись данных в файл
#-----------------------------------
def saveDatabase():
  print('\nСохраняем базу данных...')
  F = open( dbName, "wb" )
  print( len(Animals) )
  pickle.dump( Animals, F )
  F.close()

#-----------------------------------
#  МЕНЮ
#-----------------------------------
def menu():
  while True:
    print()
    print('Выберите действие:');
    print(' 1 - просмотр данных');
    print(' 2 - добавление записи');
    print(' 3 - удаление записи');
    print(' 4 - сортировка по имени');
    print(' 5 - сортировка по породе');
    print(' 6 - выход');
    cmd = int(input("Номер операции:"))
    if cmd in [CMD_SHOW, CMD_ADD, CMD_DELETE, CMD_EXIT, CMD_SORT_NAME, CMD_SORT_TYPE]:
      break;
  return cmd

#-----------------------------------
#  SHOW DATA - показать все записи
#-----------------------------------
def showData():
  print('\nБаза данных "Зоопарк"')
  print('-----------------------')
  for i, a in enumerate(Animals):
    print( str(i+1)+".", a.name, a.typ, a.age )

#-----------------------------------
#  ADD RECORD - добавить запись
#-----------------------------------
def addRecord():
  if len(Animals) >= MAX_COUNT:
    print( "\nНет места для новой записи в базе данных" )
    return
  print('Введите данные нового животного:')
  newAnimal = TAnimal()
  newAnimal.name = input('Кличка: ')
  newAnimal.typ = input('Порода: ')
  newAnimal.age = int(input('Возраст: '))
  Animals.append( newAnimal )
  saveDatabase()
  print('Запись добавлена.')

#-----------------------------------
#  DELETE RECORD - удалить запись
#-----------------------------------
def deleteRecord():
  print('\nУдаление записи...')
  no = int(input('Номер записи для удаления: '))
  if not( 1 <= no <= len(Animals) ):
    print( "\nНет записи с номером", no, "в базе данных" )
    return
  del Animals[no-1]
  saveDatabase()
  print('Запись ', no, ' удалена.')

#-----------------------------------
#  SORT BY NAME - сортировать по имени
#-----------------------------------
def sortByName():
  print('\nСортировка по имени...')
  Animals.sort( key = lambda a: a.name )
  showData()

#-----------------------------------
#  SORT BY TYPE - сортировать по породе
#-----------------------------------
def sortByType():
  print('\nСортировка по породе...')
  Animals.sort( key = lambda a: a.typ )
  showData()

#-----------------------------------
#  Основная программа
#-----------------------------------
readDatabase()
cmd = 0
while cmd != CMD_EXIT:
  cmd = menu()
  if cmd == CMD_SHOW: showData()
  if cmd == CMD_ADD:  addRecord()
  if cmd == CMD_DELETE: deleteRecord()
  if cmd == CMD_SORT_NAME: sortByName()
  if cmd == CMD_SORT_TYPE: sortByType()
print('Работа закончена.')
