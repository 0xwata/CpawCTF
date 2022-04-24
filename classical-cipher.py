

from pydoc import plain
from xmlrpc.client import Boolean

class ClassicalCipher:

  def __init__(self, plain):
      self._plain = plain

  def caesar(self):
    key = 1
    result = ""
    while(key < 26):
      for char in self._plain:
        value = self.__shift(char, key)
        result += value
      print(key, self._plain, result)
      result = ""
      key += 1

  def __shift(self, c, k):
    if self.__is_upper(c):
        ord_shift_c = ord('A')+ (ord(c) - ord('A')+ k) % 26
        return chr(ord_shift_c)
    if self.__is_lower(c):
      ord_shift_c = ord('a')+ (ord(c) - ord('a')+ k) % 26
      return chr(ord_shift_c)
    else:
      return c

  def __is_upper(self, c):
    return ord('A') <= ord(c) <= ord('Z')

  def __is_lower(self, c):
    return ord('a') <= ord(c) <= ord('z')



def main():
  plain = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"
  classicalCipher = ClassicalCipher(plain=plain)
  classicalCipher.caesar()


if __name__ == '__main__':
  main()