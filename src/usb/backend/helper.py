"""
    Helper functionality

    Created on 2011-03-03

    @author: jldupont
"""
import os

_libs=None

def get_libraries():
    """
    Returns a list of library paths
    
    Uses 'ldconfig' to retrieve them all
    """
    all=os.popen("ldconfig -p").read().replace("\t","").split("\n")[1:]
    
    ## the tail end might be an empty list
    all=all[:-1] if len(all[-1])==0 else all
    
    ## just keep the path part
    return [entry.split(" => ")[1] for entry in all]


def find_library(name, libs=None):
    """
    
    Don't really care if this operation is expensive:
    it shouldn't be performed all that often anyways.
    """
    global _libs
    if libs is None:
        if _libs is None:
            _libs=get_libraries()
        libs=_libs
        
    for entry in libs:
        if entry.find(name)!=-1:
            return entry
    return None
    
def extract_library_name(path):
    """
    Extracts the name part of the library
    """
    bits=path.split(os.path.sep)
    return bits[-1]

    
if __name__=="__main__":
    print find_library("libusb-1.0")
    print find_library("libusb-0.1")

    libusb_path=find_library("libusb-1.0")
    print extract_library_name(libusb_path)
    
