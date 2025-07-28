import struct
from typing import Tuple


class Reader:
    '''
        A class to read binary data from a bytes.  
        It provides methods to read formatted data, strings, and chunk IDs,  
        as well as to skip a specified number of bytes.
        '''
    
    def __init__( self, data: bytes ):
        self.__data: bytes  = data
        self.offset         = 0

    def getf( self, value_format: str ) -> Tuple:
        size = struct.calcsize( value_format )
        self.offset += size
        return struct.unpack_from( value_format, self.__data, self.offset - size )

    def gets( self, size: int ) -> Tuple:
        self.offset += size
        return struct.unpack_from( '<{}s'.format(size), self.__data, self.offset - size )[0].split(b'\x00')[0].decode( encoding='mbcs' )

    def getid( self, required_chunks_id, debug=False ):
        self.offset += 4
        chunk_id = struct.unpack_from( '<4s', self.__data, self.offset - 4 )[0].decode( encoding='mbcs' )

        if type( required_chunks_id ) == str:
            required_chunks_id = [required_chunks_id, ]

        if chunk_id not in required_chunks_id:
            if not debug:
                raise Exception( 'chunk id "{0}" not in "{1}"'.format( chunk_id, required_chunks_id ) )
        else:
            return chunk_id

    def skip( self, count: int ):
        self.offset += count
