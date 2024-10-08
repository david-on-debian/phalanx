#!/usr/bin/python3

""" This python3 module (technically it`s a file...) provides a class (IOport,) for
simulating I/O ports such as RJ-45 ports, USB, PS/2, etc.

The way to use this module is as follows:
import phalanx
eth0 = IOport()
eth1 = IOport()
eth0.load("hello there")
eth0.write(eth1)
eth1.read()
value = eth1.read_return()
print(value)

In the very soon future, I will explain all of
that line by line. but not just yet.

--author: David Geoke
"""

# thank goodness this (the whole module) works.

__author__ = 'David J Goeke <secret321king3@gmail.com>'
__credits__ = ('None yet')
__all__ = ['IOport']

import sys # the most important and confusing module out there

class IOport:
    """ a class for emulating I/O ports such as(but not limited to,): USB ports, HDMI ports, Serial ports, PS/2 ports, RJ45 Ethernet ports, etc.
    I have honestly no idea what practical purpose ON EARTH this could serve, but still, it`s fun, so, who cares?       (me.)
    P.S. this module is extremely complicated, so bear with be when trying to use this.
    see the ``phalanx-doc`` file for more information.
    """
    __data_in = None
    __data_out = None
    __current_data = None
    
    @property
    def data_in(self):
        return self.__data_in
        
    @data_in.setter
    def data_in(self, data):
        """ the setter for ``data_in``.
        """
        self.__data_in = data
        
    @property
    def data_out(self):
        return self.__data_out
        
    @data_out.setter
    def data_out(self, data):
        """the setter for ``data_out``.
        """
        self.__data_out = data
        
    @property
    def current_data(self):
        return self.__current_data
        
    @current_data.setter
    def current_data(self, data):
        """the setter for ``current_data``.
        """
        self.__current_data = data
    
    @staticmethod
    def load(self, data):
        """sets self.data_out to ``data`` so you can use ``[IOport-name].write([IOport-name], [second-IOport-name]).
        see the documentation for ``write`` for more information.
        """
        self.data_out = data
    
    @staticmethod
    def write(self, target, data=None):
        """writes ``data`` to target.data_in;
        unless ``data`` is None, then `write` takes the data from self.data_out.
        """
        if data is None:
            data = self.data_out
        else:
            pass
        target.data_in = data 
        
    @staticmethod
    def read(self):
        """honestly pretty self-explanatory. reads the (if any) value from self.data_in, then places it in self.current_data.
        """
        self.current_data = self.data_in

    @staticmethod
    def read_return(self):
        """ Again, pretty self-explanatory;
        returns self.current_data ( set by self.read() )
        """
        return self.current_data
    
    @staticmethod
    def execute(self, error_file):
        """ executes the data in self.current_data. 
        """
        try:
            cdata = compile(self.current_data, error_file, 'exec')  
            exec(cdata)
        except:
            raise TypeError(f"IOport.execute() expected str, bytes or os.PathLike object, not {type(error_file)}.\n\
maybe you put in, for example, sys.stdout, but what you need to say is: 'sys.stdout'.")


