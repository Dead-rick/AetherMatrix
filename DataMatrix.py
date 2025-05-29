from pydbErrors import *
from tabulate import tabulate as Fnx
import operator
from math import *
from copy import deepcopy

Integral_Adjust = lambda Val: Val-1 if Val != None and Val>0 else Val
Slicing_Adjust = lambda Val, wrt: slice(*slice(*(Integral_Adjust(Val.start),Val.stop,Val.step)).indices(wrt))
Islist = lambda Val: isinstance(Val, list)

def Secondary_Array_Validation(array):
   if not isinstance(array, list): return False
   else:
      Amplitude = len(array[0])
      for i in array: 
         if (not isinstance(i, list) or len(i) != Amplitude): return False
      return True

def Primary_Array_Validation(array):
   if not isinstance(array, list): return False
   for i in array:
      if isinstance(i, list):
         return False
   return True

def Null_Array_Validation(array):
   if isinstance(array, list):
      return False
   else:
      return True


def Dimension_Validation(array,dim1,dim2):
    if len(array) == dim1:
        for i in array:
            try:
                if len(i) == dim2:
                    pass
                else:
                    return False
            except TypeError:
                if dim1 != 1: return False
                else: return True
        return True
    else: return False

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge
}


def Comp_Operators(instance, other_instance, opr):
        Returned = []
        for i in range(instance.alt):
            Temp = []
            for j in range(instance.amp):
                if isinstance(other_instance, DataMatrix):
                    if other_instance.dim != instance.dim: raise ValueError(f'[Error #1] To opertions to carry, both the Object should have same dimension, but rather different here; {instance.dim} and {other_instance.dim}')
                    Temp.append(OPERATORS[opr](instance.array[i][j], other_instance.array[i][j]))
                else: Temp.append(OPERATORS[opr](instance.array[i][j],other_instance))
            Returned.append(Temp)    
        return Returned

class DataMatrix:
    def __init__(self, array):
         if Null_Array_Validation(array):
            self.array = [[array]]
         elif Primary_Array_Validation(array):
            self.array = [array]
         elif Secondary_Array_Validation(array):
            self.array = array
         else:
            raise ValueError('[Error #2] Illegally nested array.')
         self.amp = len(self.array[0])
         self.alt = len(self.array)
         self.dim = f'{self.alt}x{self.amp}'
         self.style = 'rounded_grid'
         self._headers = None
         self._index = False
         self._axis = 1

    @property
    def headers(self): return self._headers
   
    @headers.setter
    def headers(self, val):
      if val == None:
         self._headers = None
         return
      if not isinstance(val, list):
         raise TypeError(f'[Error #3] The headers argument must be a \'list\', but rather given as {type(val).__name__}.')
      if len(val) != self.amp:
         raise ValueError(f'[Error #4] Length of header should be same as the amplitude of the array!, the length of the headers are in {len(val)}.')
      self._headers = val

    @property
    def index(self): return self._index

    @index.setter
    def index(self, val):
      if not isinstance(val, bool):
         raise TypeError(f'[Error #5] The index argument must be a \'boolean\', but rather given as {type(val).__name__}.')
      self._index = val
   
    @property
    def axis(self): return self._axis

    @axis.setter
    def axis(self, val):
      if val not in [0, 1]:
         raise ValueError(f'[Error 6] The axis must be either 1 or 0; given as {val}.')
      self._axis = val

    def __len__(self):
        if self.axis == 1:
            return self.alt
        else:
            return self.amp
        
    def copy(self):
        return DataMatrix(deepcopy(self.array))
    
    @property
    def transpose(self):
        return DataMatrix([[x[i] for x in self.array] for i in range(len(self.array[0]))])
    
    def __repr__(self):
        return f"DataMatrix({self.dim})"

    def __str__(self):
        if not self.index and self.headers == None:
            Tbl = Fnx(self.array, tablefmt=self.style)
        elif not self.index and self.headers:
            Tbl = Fnx(self.array, tablefmt=self.style, headers=self.headers)
        elif self.index and self.headers == None:
            Tbl = Fnx([[j]+i for i,j in zip(self.array, range(1, self.alt+1))],headers=[i for i in range(self.amp+1)] ,tablefmt=self.style)
        elif self.index and self.headers:
            Tbl = Fnx([[i for i in range(self.amp+1)]]+[[j]+i for i,j in zip(self.array, range(1, self.alt+1))], tablefmt=self.style, headers=[None]+self.headers)
        return Tbl

    def __getitem__(self, index):
        Error_occured = False
        try:
            if isinstance(index, tuple):
                Row_Index, Col_Index = index
                if isinstance(Row_Index, int): Int_Row = Row_Index - 1 if Row_Index > 0 else Row_Index
                if isinstance(Col_Index, int): Int_Col = Col_Index - 1 if Col_Index > 0 else Col_Index
                if isinstance(Row_Index, slice): Slice_Row = Slicing_Adjust(Row_Index, self.alt)
                if isinstance(Col_Index, slice): Slice_Col = Slicing_Adjust(Col_Index, self.amp)
                if isinstance(Row_Index, int) and isinstance(Col_Index, int):
                    return DataMatrix(self.array[Int_Row][Int_Col])
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, int):
                    return DataMatrix([[i[Int_Col]] for i in self.array[Slice_Row]])
                elif isinstance(Row_Index, int) and isinstance(Col_Index, slice):
                    return DataMatrix(self.array[Int_Row][Slice_Col])
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, slice):
                    return DataMatrix([i[Slice_Col] for i in self.array[Slice_Row]])
            elif isinstance(index, int):
                return DataMatrix(self.array[Integral_Adjust(index)])
            elif isinstance(index, slice):
                return DataMatrix(self.array[Slicing_Adjust(index, wrt=self.alt)])
        except IndexError:Error_occured=True
        if Error_occured: raise IndexError(f'[Error #7] The provided is index is either out of range or illegal for the given array; provided index:{index}.')

    def __setitem__(self, index, data):
        if isinstance(data, DataMatrix):val = data.array
        else: val = data

        Error_occured = False
        try:
            if isinstance(index, tuple):
                Row_Index, Col_Index = index

                if isinstance(Row_Index, int): Int_Row = Row_Index - 1 if Row_Index > 0 else Row_Index
                if isinstance(Col_Index, int): Int_Col = Col_Index - 1 if Col_Index > 0 else Col_Index
                if isinstance(Row_Index, slice): Slice_Row = Slicing_Adjust(Row_Index, self.alt); Row_Range = range(*(Slice_Row).indices(self.alt))
                if isinstance(Col_Index, slice): Slice_Col = Slicing_Adjust(Col_Index, self.amp); Col_Range = range(*(Slice_Col).indices(self.amp))
                if isinstance(Row_Index, int) and isinstance(Col_Index, int):
                    self.array[Int_Row][Int_Col] = val
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, int):
                    if Islist(val):
                        if Dimension_Validation(val, len(Row_Range),1):
                            for i,j in zip(Row_Range,val):self.array[i][Int_Col] = j[0]
                        else:raise ValueError(f'[Error #8] The dimensions of the setter value is illegal for the index {index}, required:{len(Row_Range)}x1.')
                    else:
                        for i in Row_Range:self.array[i][Int_Col] = val              
                elif isinstance(Row_Index, int) and isinstance(Col_Index, slice):
                    if Islist(val):
                        if Dimension_Validation(val, 1, len(Col_Range)):
                            self.array[Int_Row][Slice_Col] = val[0]
                        else: raise ValueError(f'[Error #8] The dimensions of the setter value is illegal for the index {index}, required:1x{len(Col_Range)}.')
                    else: self.array[Int_Row][Slice_Col] = [val]*len(Col_Range)
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, slice):
                    if Islist(val):
                        if Dimension_Validation(val, len(Row_Range), len(Col_Range)):
                            for i,j in zip(Row_Range, val):
                                self.array[i][Slice_Col] = j
                        else: raise ValueError(f'[Error #8] The dimensions of the setter value is illegal for the index {index}, required:{len(Row_Range)}x{len(Col_Range)}.')
                    else:
                        for i in Row_Range: self.array[i][Slice_Col] = [val]*len(Col_Range)
            elif isinstance(index, int):
                if Islist(val):
                    if Dimension_Validation(val, 1, self.amp):
                        self.array[index-1] = val[0]
                    else: raise ValueError(f'[Error #8] The dimensions of the setter value is illegal for the index {index}, required:{self.amp}x1.')
                else: self.array[index-1] = [val]*self.amp
            elif isinstance(index, slice):
                Slice_index = Slicing_Adjust(index, self.alt)
                Row_Range = range(*(Slice_index).indices(self.alt))
                if Islist(val):
                    if Dimension_Validation(val, len(Row_Range), self.amp):
                        for i,j in zip(Row_Range, val):
                            self.array[i] = j
                    else: raise ValueError(f'[Erro #8] The dimensions of the setter value is illegal for the index {index}, required:{len(Row_Range)}x{self.amp}.')
                else:
                    for i in Row_Range: self.array[i] = [val]*self.amp
        except IndexError: Error_occured = True
        if Error_occured: raise IndexError(f'[Error #9] The provided is index is either out of range or illegal for the given array; provided index:{index}.')

    def __delitem__(self, key):
        Error_occured = False
        try:
            if isinstance(key, tuple):
                Row_Index,Col_Index = key
                if isinstance(Row_Index, int): Int_Row = Row_Index - 1 if Row_Index > 0 else Row_Index
                if isinstance(Col_Index, int): Int_Col = Col_Index - 1 if Col_Index > 0 else Col_Index
                if isinstance(Row_Index, slice): Slice_Row = Slicing_Adjust(Row_Index, self.alt); Row_Range = range(Slice_Row.start,Slice_Row.stop,Slice_Row.step)
                if isinstance(Col_Index, slice): Slice_Col = Slicing_Adjust(Col_Index, self.amp); Col_Range = range(Slice_Col.start,Slice_Col.stop,Slice_Col.step)
                if isinstance(Row_Index, int) and isinstance(Col_Index, int):
                    self.array[Int_Row][Int_Col] = None
                elif isinstance(Row_Index, int) and isinstance(Col_Index, slice):
                    if self.array[Int_Row] == self.array[Int_Row][Slice_Col]:del self.array[Int_Row]
                    else:self.array[Int_Row][Slice_Col] = [None]*len(Col_Range)
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, int):
                    if [i[Int_Col] for i in self.array[Slice_Row]] == [i[Int_Col] for i in self.array]:
                        for i in self.array[Slice_Row]: del i[Int_Col]
                    else: 
                        for i in Row_Range: self.array[i][Int_Col] = None
                elif isinstance(Row_Index, slice) and isinstance(Col_Index, slice):
                    if Slice_Row == slice(0, self.alt, 1):
                        for i in self.array: del i[Slice_Col]
                    elif Slice_Col == slice(0, self.amp, 1): del self.array[Slice_Row]
                    else:
                        for i in Row_Range:
                            for j in Col_Range:
                                self.array[i][j] = None
            elif isinstance(key, int):
                del self.array[key-1]
            elif isinstance(key, slice):
                Slice_Row = Slicing_Adjust(key, self.alt)
                del self.array[Slice_Row]
        except IndexError:Error_occured = True
        if Error_occured: raise IndexError(f'[Error #10] The provided is index is either out of range or illegal for the given array; provided index:{key}.')

        self.amp = len(self.array[0])
        self.alt = len(self.array)
    
    def __add__(self, Val):return DataMatrix(Comp_Operators(self, Val, '+'))
    def __mul__(self, Val):return DataMatrix(Comp_Operators(self, Val, '*'))
    def __truediv__(self, Val): return DataMatrix(Comp_Operators(self, Val, '/'))
    def __sub__(self, Val): return DataMatrix(Comp_Operators(self, Val, '-'))
    def __floordiv__(self, Val): return DataMatrix(Comp_Operators(self, Val, '//'))
    def __mod__(self, Val): return DataMatrix(Comp_Operators(self, Val, '%'))
    def __eq__(self, Val): return DataMatrix(Comp_Operators(self, Val, '=='))
    def __gt__(self, Val): return DataMatrix(Comp_Operators(self, Val, '>'))
    def __lt__(self, Val): return DataMatrix(Comp_Operators(self, Val, '<'))
    def __le__(self, Val): return DataMatrix(Comp_Operators(self, Val, '<='))
    def __ge__(self, Val): return DataMatrix(Comp_Operators(self, Val, '>='))
    def __ne__(self, Val): return DataMatrix(Comp_Operators(self, Val, '!='))
    
    def __iter__(self):
        if self.axis == 1:return iter(self.array)
        else:return iter(self.transpose.__raw__)

    def apply(self, func):
        return DataMatrix([[func(j) for j in i] for i in self.array])
    
    def __bool__(self):
        Bool_array = [[bool(j) for j in i] for i in self.array]
        Comp_Bool_array = [[True for j in range(self.amp)] for i in range(self.alt)]
        return Bool_array == Comp_Bool_array
    
    def append(self, val):
        if not isinstance(val, DataMatrix):raise TypeError('[Error #11] The value you going to append but be also a DataMatrix Object.')
        if self.axis == 1:
            if self.amp != val.amp:raise ValueError('[Error #12] The amplitude of the main array and the ampliude of appending array is not equal')
            self.array += val.array
        else:
            if self.alt != val.alt:raise ValueError('[Error #13] The altitude of the main array and the altitude of appending array is not equal')
            for i,j in zip(self.array, val.array):i += j
        self.amp = len(self.array[0])
        self.alt = len(self.array)
    
    def insert(self,index, val):
        Error_Occured = False
        try:
            if not isinstance(val, DataMatrix): raise TypeError('[Error #14] The value you going to append but be also a DataMatrix Object.')
            if self.axis == 1:
                if val.amp != self.amp:raise ValueError('[Error #15] The amplitude of the main array and the ampliude of appending array is not equal')
                for j in val.array[::-1]:self.array.insert(index-1, j)
            else:
                if val.alt != self.alt:raise ValueError('[Error #16] The altitude of the main array and the altitude of appending array is not equal')
                for i,j in zip(self.array, val.array):
                    for k in j[::-1]:i.insert(index-1, k)
            self.amp = len(self.array[0])
            self.alt = len(self.array)
        except IndexError: Error_Occured = True
        if Error_Occured:
            raise IndexError(f'[Error #17] The provided is index is either out of range or illegal for the given array; provided index:{index}.')


    @property
    def __raw__(self):
        return self.array
