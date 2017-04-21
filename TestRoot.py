import abc

class AbstractTest:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self,callable_test_obj): 
        print("This abstract function should not have been called")
        raise NotImplementedError()
