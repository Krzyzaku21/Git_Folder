# _hiddenlist - prywatna metoda nie powinna być używana przez
# kod zewnętrzny,
# from module_name import * nie importuje wartości początkowych z _hiddenlist
# %%
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents) #instancja
  def push(self, value):
    self._hiddenlist.insert(0, value)
  def pop(self):
    return self._hiddenlist.pop(-1)
  def __repr__(self): #__repr__ służy do reprezentacji instancji w postaci łańcucha.
    return "QueueClass({})".format(self._hiddenlist)
queue = Queue([1, 2, 3])
print(queue) #Queue([1, 2, 3])
queue.push(0) #metoda umieszcza 0 na pozycji 0 w liście
print(queue) #Queue([0, 1, 2, 3])
queue.pop() #metoda skraca liste o -1 wartość z końca
print(queue) #Queue([0, 1, 2])
print(queue._hiddenlist) #[0, 1, 2]
# %%
