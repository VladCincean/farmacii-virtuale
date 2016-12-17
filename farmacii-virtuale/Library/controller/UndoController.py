'''
Created on 25 nov. 2015

@author: Vlad
'''

class UndoController:
    """
    Controls the undo/redo operations over all application
    """
    def __init__(self):
        self._operations = []
        self._index = -1
        
    def recordUpdatedControllers(self, controllers):
        """
        Every time an application controller records an operation with support for undo/redo it must call this method
        Input: controllers - A list of controllers that can undo/redo the operation. 
        In case an operation involves multiple distinct controllers, this is where they all have to be provided 
        """
        self._operations.append(controllers)
        
        '''
        We clear the list of steps that were previously undone
        '''
        self._operations = self._operations[0:self._index + 2]
        self._index = len(self._operations) - 1
    
    def undo(self):
        """
        Undo the last performed operation by any application controller
        """
        if self._index < 0:
            return False
        for controller in self._operations[self._index]:
            controller.undo()
        self._index -= 1
        return True
    
    def redo(self):
        """
        Redo the last performed operation by any application controller
        """
        if self._index >= len(self._operations) - 1:
            return False
        self._index += 1
        for controller in self._operations[self._index]:
            controller.redo()
        return True
