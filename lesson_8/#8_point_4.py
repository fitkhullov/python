#point_4
class EquipmentBase:
    base_content = {'Принтер': [0, []], 'Сканер': [0, []], 'Ксерокс': [0, []]}
    subdivisions = {'A', 'B', 'C', 'D'}
    transfered_items = {'Принтер' : [], 'Сканер': [], 'Ксерокс': []}
    def __init__(self, spec_info, stand_info):
        stand_info.update(spec_info)
        EquipmentBase.base_content[stand_info['name']][0] += 1
        EquipmentBase.base_content[stand_info['name']][1].append(stand_info)
        
    def transfer_to_copmany(name, amount, subdivision):
        if name in set(EquipmentBase.base_content) and subdivision in EquipmentBase.subdivisions and EquipmentBase.base_content[name][0] >= amount:
            EquipmentBase.transfered_items[name].append([{'sub': subdivision, 'amount': amount}])
        else:
            contain_name =  name in set(EquipmentBase.base_content)
            containt_sub = subdivision in EquipmentBase.subdivisions
            contain_amount = EquipmentBase.base_content[name][0] >= amount
            print('the False state mean that your request in that position is wrong')
            print(f'{name}:{contain_name}, {subdivision}: {contain_sub}, {amount}: {contain_amount}')
 
        
class Equipment(EquipmentBase):
    def __init__(self, **stand_info):
        self._is_transfered = False
        self.stand_info = stand_info
        
    @property
    def stand_info(self):
        return self._stand_info
    
    @stand_info.setter
    def stand_info(self, stand_info):
        if {'name', 'model', 'brand', 'price'} != set(stand_info):
            print('Wrong data!')
            try:
                self._stand_info
            except AttributeError:
                self._stand_info = {'name': None, 'model': None, 'brand': None, 'price': None} 
        elif list(map(type, [stand_info['name'], stand_info['model'], stand_info['brand']])) == [str]*3 and \
            (type(stand_info['price']) == float or type(stand_info['price']) == int):
            self._stand_info = stand_info    
        return
    
    def transfer_to_base(self):
        if set(self._stand_info.values()) == None:
            print('I cant transfer this obj. Pls add informattion about this obj.')
        else:
            print('transfer is start')
            super().__init__(self._spec, self._stand_info)
            self._is_transfered = True
        
        
class Printer(Equipment):
    def __init__(self, spec, **info):
        info.update({'name': 'Принтер'})
        super().__init__(**info)
        self.spec = spec
    
    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, spec):
        if type(spec) == bool:
            self._spec = {'colored': spec}
        else:
            try:
                self._spec
            except AttributeError:
                print('this param must be boolean')
                self._spec = {'colored': None}                
        return
    
        
class Scaner(Equipment):
    def __init__(self, spec, **info):
        info.update({'name': 'Сканер'})
        super().__init__(**info)
        self.spec = spec
    
    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, spec):
        if type(spec) == int and 1 <= spec <= 3:
            self._spec = {'dimensions': spec}
        else:
            try:
                self._spec
            except AttributeError:
                self._spec = {'dimensions': None}
                print('this param must be integer and included in the interval [1; 3]')
        return
    
    
class Xerox(Equipment):
    def __init__(self, spec, **info):
        info.update({'name': 'Ксерокс'})
        super().__init__(**info)
        self.spec = spec
        
    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, spec):
        if type(spec) == str and spec in {'diode', 'halogen', 'luminescent'}:
            self._spec = {'light_type': spec}
        else:
            try:
                self._spec
            except AttributeError:
                self._spec = {'light_type': None}
                print('this param must be str and be one of those: "diode", "halogen", "luminescent"')
        return
          
        
        
printer = Printer(True, model = 'xm-104', brand = 'psychotronic',  price = 199)
scaner = Scaner(3, model = 'xm-105', brand = 'BobaYoba', price = 0)
xerox = Xerox('diode', model = 'xm-106', brand = 'YobaBoba',  price = 1)
