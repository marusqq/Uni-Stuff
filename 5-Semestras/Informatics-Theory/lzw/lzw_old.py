#!/usr/bin/env python
__author__ = "Marius Pozniakovas, Tomas Kučejevas, Lukas Miežys, Rafal Michalkiewicz"
#lzw functions used in main.py

import struct
import itertools
import six
import string
import random
from sys import argv

#MP
import inspect
log = open('debug.log', 'w+')
import time

TIMER = True
DEBUG = True

if TIMER:
    startTime = time.time()

if len(argv) == 5:
    M_NUMBER = int(argv[4])

COUNT = 0
CLEAR_CODE = 256
END_OF_INFO_CODE = 257

DEFAULT_MIN_BITS = 9
DEFAULT_MAX_BITS = 13



def debug(text = None, program = None, line = None):

    #function used for debug certain places of code

    global COUNT
    COUNT = COUNT+1
    if DEBUG:

        log.write ('---------------------------------------------------------------------------------------------------------------' + '\n')
        log.write ('Seq: ' + str(COUNT) + '\n')
        log.write ('Program: ' + str(program) + '\t\t Line: ' + str(line) + '\t\t Text: ' + str(text) + '\n')
        
        if text == 'TERMINATE':
            log.close()

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

#number M saving
def save_m_number():
    
    file = open('m.txt', 'w')

    m_secret = str(M_NUMBER)
    m_secret_length = len(m_secret)

    #write the length
    file.write(chr(m_secret_length - 1))

    debug(program = 'lzw.save_m_number', text = 'end, length_of_m = ' + str(m_secret_length) , line = lineno())

    #write each seperate chars (encode them as + 25 - (i+1))
    for i in range(0, m_secret_length):

        #if the number is negative get a random ascii alphabet letter
        if m_secret[i] == '-':

            alphabet = string.ascii_letters
            random_letter = random.choice(alphabet)
            key = random_letter
        
        #if we have a normal number just add 25 and remove index * 2
        else:
            key = chr(int(m_secret[i]) + 25 - (i * 2))

        #output the key
        file.write (key)

        #this is just for debugger
        debug(program = 'lzw.save_m_number', text = 'end, key = ' + str(key) , line = lineno())
    
    file.close()
    return

#compressing main logic
def compress(bytes):

    save_m_number()
    if TIMER:
        loadingTime = time.time()
        total = loadingTime - startTime
        print ('M number encoded. M: ' + str(M_NUMBER) + '. \t\tTime: ' + str(total))

    debug(program = 'lzw.compress', text = 'start, bytes = ' + str(bytes) , line = lineno())
    encoder = ByteEncoder()
    debug(program = 'lzw.compress', text = 'after encoder creation', line = lineno())
    return encoder.encodetobytes(bytes)

#decompressing main logic
def decompress(bytes, m):
    debug(program = 'lzw.decompress', text = 'start', line = lineno())
    decoder = ByteDecoder()
    debug(program = 'lzw.decompress', text = 'after decoder creation', line = lineno())
    return decoder.decodefrombytes(bytes, m)

#encoder class
class ByteEncoder(object):
    
    #constructor
    def __init__(self, max_width = DEFAULT_MAX_BITS):
        debug(program = 'ByteDecoder.init', text = 'before creating objects, self= ' + str(self), line = lineno())
        self._encoder = Encoder(max_code_size=2**max_width)
        debug(program = 'ByteDecoder.init', text = 'before creating encoder object, self= ' + str(self), line = lineno())
        self._packer = BitPacker(initial_code_size = self._encoder.code_size())
        debug(program = 'ByteDecoder.init', text = 'before creating bitpacker object, self= ' + str(self), line = lineno())

    def encodetobytes(self, bytes):
        debug(program = 'ByteEncoder.encodetobytes', text = 'start', line = lineno())
        codepoints = self._encoder.encode(bytes)

        if TIMER:
            loadingTime = time.time()
            total = loadingTime - startTime
            print ('Bytes Encoded. \t\tTime: ' + str(total))

        debug(program = 'ByteEncoder.encodetobytes', text = 'after _encoder.encode, bytes =' + str(bytes), line = lineno())
        codebytes = self._packer.pack(codepoints)

        if TIMER:
            loadingTime = time.time()
            total = loadingTime - startTime
            print ('Bits Packed. \t\tTime: ' + str(total))

        debug(program = 'ByteEncoder.encodetobytes', text = 'after _packer.pack', line = lineno())

        return codebytes

#used in decompressing
class ByteDecoder(object):

    def __init__(self):

        debug(program = 'ByteDecoder.init', text = 'before creating objects, self= ' + str(self), line = lineno())
        self._decoder = Decoder()
        debug(program = 'ByteDecoder.init', text = 'after decoder object creation, self._decoder= ' + str(self._decoder), line = lineno())
        self._unpacker = BitUnpacker(initial_code_size=self._decoder.code_size())
        debug(program = 'ByteDecoder.init', text = 'after bitunpacker, self._unpacker= ' + str(self._unpacker), line = lineno())
        self.remaining = []

    def decodefrombytes(self, bytes, m):

        debug(program = 'ByteDecoder.decodefrombytes', text = 'start, self= ' + str(self) + ' bytes=' + str(bytes), line = lineno())
        codepoints = self._unpacker.unpack(bytes)

        if TIMER:
            loadingTime = time.time()
            total = loadingTime - startTime
            print ('Bits unpacked. \t\tTime: ' + str(total))

        debug(program = 'ByteDecoder.decodefrombytes', text = 'after bit unpacking, self= ' + str(self), line = lineno())
        clearbytes = self._decoder.decode(codepoints, m)

        if TIMER:
            loadingTime = time.time()
            total = loadingTime - startTime
            print ('Bytes decoded. \t\tTime: ' + str(total))

        debug(program = 'ByteDecoder.init', text = 'before bit decoding, self= ' + str(self), line = lineno())

        return clearbytes

#used in compressing
class BitPacker(object):

    def __init__(self, initial_code_size):
       """
       Takes an initial code book size (that is, the count of known
       codes at the beginning of encoding, or after a clear)
       """
       debug(program = 'BitPacker.init', text = 'start', line = lineno())
       self._initial_code_size = initial_code_size

    def pack(self, codepoints):
        debug(program = 'Bitpacker.pack', text = 'start', line = lineno())
        """
        Given an iterator of integer codepoints, returns an iterator
        over bytes containing the codepoints packed into varying
        lengths, with bit width growing to accomodate an input code
        that it assumes will grow by one entry per codepoint seen.

        Widths will be reset to the given initial_code_size when the
        LZW CLEAR_CODE or END_OF_INFO_CODE code appears in the input,
        and bytes following END_OF_INFO_CODE will be aligned to the
        next byte boundary.

        >>> import lzw, six
        >>> pkr = lzw.BitPacker(258)
        >>> [ b for b in pkr.pack([ 1, 257]) ] == [ six.int2byte(0), six.int2byte(0xC0), six.int2byte(0x40) ]
        True
        """
        tailbits = []
        codesize = self._initial_code_size

        minwidth = 8
        while (1 << minwidth) < codesize:
            minwidth = minwidth + 1

        nextwidth = minwidth

        for pt in codepoints:
            #print ('pt ', end = ': ')
            #print (pt)
            newbits = inttobits(pt, nextwidth)
            tailbits = tailbits + newbits

            # PAY ATTENTION. This calculation should be driven by the
            # size of the upstream codebook, right now we're just trusting
            # that everybody intends to follow the TIFF spec.
            codesize = codesize + 1

            if pt == END_OF_INFO_CODE:
               while len(tailbits) % 8:
                  tailbits.append(0)
                  
            if pt in [ CLEAR_CODE, END_OF_INFO_CODE ]:
                nextwidth = minwidth
                codesize = self._initial_code_size
            elif codesize >= (2 ** nextwidth):
                nextwidth = nextwidth + 1

            #print ('\n')
            while len(tailbits) > 8:
                
                #print ('all bits', end = ': ')
                #print(tailbits)
                
                nextbits = tailbits[:8]
                #print ('nextbits', end = ': ')
                #print(nextbits)

                nextbytes = bitstobytes(nextbits)

                for bt in nextbytes:
                    #print ('first bt', end = ': ')
                    #print (bt, end = '= char = ')
                    #print (chr(bt))
                    yield struct.pack("B", bt)

                tailbits = tailbits[8:]
                #print ('tailbits', end = ': ')
                #print (tailbits)
                #print ('\n')


        if tailbits:
            tail = bitstobytes(tailbits)
            for bt in tail:
                yield struct.pack("B", bt)

#used in decompressing
class BitUnpacker(object):
    """
    An adaptive-width bit unpacker, intended to decode streams written
    by L{BitPacker} into integer codepoints. Like L{BitPacker}, knows
    about code size changes and control codes.
    """

    def __init__(self, initial_code_size):
       """
       initial_code_size is the starting size of the codebook
       associated with the to-be-unpacked stream.
       """
       debug(program = 'Bitunpacker._init_', text = 'start', line = lineno())

       self._initial_code_size = initial_code_size

    def unpack(self, bytesource):
        """
        Given an iterator of bytes, returns an iterator of integer
        code points. Auto-magically adjusts point width when it sees
        an almost-overflow in the input stream, or an LZW CLEAR_CODE
        or END_OF_INFO_CODE

        Trailing bits at the end of the given iterator, after the last
        codepoint, will be dropped on the floor.

        At the end of the iteration, or when an END_OF_INFO_CODE seen
        the unpacker will ignore the bits after the code until it
        reaches the next aligned byte. END_OF_INFO_CODE will *not*
        stop the generator, just reset the alignment and the width


        >>> import lzw, six
        >>> unpk = lzw.BitUnpacker(initial_code_size=258)
        >>> [ i for i in unpk.unpack([ six.int2byte(0), six.int2byte(0xC0), six.int2byte(0x40) ]) ]
        [1, 257]
        """
        debug(program = 'BitPacker.unpack', text = 'start', line = lineno())
        bits = []
        offset = 0
        ignore = 0
        
        codesize = self._initial_code_size
        minwidth = 8
        while (1 << minwidth) < codesize:
            minwidth = minwidth + 1

        pointwidth = minwidth
        debug(program = 'BitPacker.unpack', text = 'pointwidth = ' + str(pointwidth), line = lineno())

        for nextbit in bytestobits(bytesource):
            #debug(program = 'BitPacker.unpack', text = 'nextbit = ' + str(nextbit), line = lineno())

            offset = (offset + 1) % 8
            if ignore > 0:
                ignore = ignore - 1
                continue

            bits.append(nextbit)
             
            if len(bits) == pointwidth:
                codepoint = intfrombits(bits)
                bits = []

                debug(program = 'BitPacker.unpack', text = 'codepoint = ' + str(codepoint), line = lineno())
                yield codepoint

                codesize = codesize + 1

                if codepoint in [ CLEAR_CODE, END_OF_INFO_CODE ]:
                    codesize = self._initial_code_size
                    pointwidth = minwidth
                else:
                    # is this too late?
                    while codesize >= (2 ** pointwidth):
                        pointwidth = pointwidth + 1

                if codepoint == END_OF_INFO_CODE:
                    ignore = (8 - offset) % 8

#used in decompressing
class Decoder(object):
    """
    Uncompresses a stream of lzw code points, as created by
    L{Encoder}. Given a list of integer code points, with all
    unpacking foolishness complete, turns that list of codepoints into
    a list of uncompressed bytes. See L{BitUnpacker} for what this
    doesn't do.
    """
    def __init__(self):
       """
       Creates a new Decoder. Decoders should not be reused for
       different streams.
       """
       debug(program = 'Decoder.__init__', text = 'start', line = lineno())
       self._clear_codes()
       self.remainder = []

    def code_size(self):
       """
       Returns the current size of the Decoder's code book, that is,
       it's mapping of codepoints to byte strings. The return value of
       this method will change as the decode encounters more encoded
       input, or control codes.
       """

       debug(program = 'Decoder.code_size', text = 'start', line = lineno())
       return len(self._codepoints)

    def decode(self, codepoints, m):
        """
        Given an iterable of integer codepoints, yields the
        corresponding bytes, one at a time, as byte strings of length
        E{1}. Retains the state of the codebook from call to call, so
        if you have another stream, you'll likely need another
        decoder!

        Decoders will NOT handle END_OF_INFO_CODE (rather, they will
        handle the code by throwing an exception); END_OF_INFO should
        be handled by the upstream codepoint generator (see
        L{BitUnpacker}, for example)

        >>> import lzw
        >>> dec = lzw.Decoder()
        >>> result = b''.join(dec.decode([103, 97, 98, 98, 97, 32, 258, 260, 262, 121, 111, 263, 259, 261, 256]))
        >>> result == b'gabba gabba yo gabba'
        True

        """
        debug(program = 'Decoder.decode', text = 'start, codepoints = ' + str(codepoints), line = lineno())

        codepoints = [ cp for cp in codepoints ]

        for cp in codepoints:
            decoded = self._decode_codepoint(cp)
            debug(program = 'Decoder.decode', text = 'decoded = ' + str(decoded), line = lineno())
            for character in six.iterbytes(decoded):
                # TODO optimize, casting back to bytes when bytes above
                debug(program = 'Decoder.decode', text = 'six.int2byte(character) = ' + str(character), line = lineno())
                yield six.int2byte(character)

    def _decode_codepoint(self, codepoint):
        """
        Will raise a ValueError if given an END_OF_INFORMATION
        code. EOI codes should be handled by callers if they're
        present in our source stream.
        """
        

        debug(program = 'Decoder._decode_codepoint', text = 'start', line = lineno())
        

        ret = b""

        if codepoint == CLEAR_CODE:
            self._clear_codes()
        elif codepoint == END_OF_INFO_CODE:
            raise ValueError("End of information code not supported directly by this Decoder")
        else:
            debug(program = 'Decoder._decode_codepoint', text = self._codepoints, line = lineno())
            if codepoint in self._codepoints:
                ret = self._codepoints[ codepoint ]
                if None != self._prefix:
                    self._codepoints[ len(self._codepoints) ] = self._prefix + six.int2byte(six.indexbytes(ret, 0))
                    debug(program = 'Decoder._decode_codepoint', text = 'add new prefix: ' + str(self._prefix + six.int2byte(six.indexbytes(ret, 0))), line = lineno())
                    print (self.code_size())
            else:
                ret = self._prefix + six.int2byte(six.indexbytes(self._prefix, 0))
                self._codepoints[ len(self._codepoints) ] = ret

            self._prefix = ret
            debug(program = 'Decoder._decode_codepoint', text = 'prefix = ' + str(ret), line = lineno())

        return ret

    def _clear_codes(self):
        debug(program = 'Decoder._clear_codes', text = 'start', line = lineno())
        self._codepoints = dict( (pt, struct.pack("B", pt)) for pt in range(256) )
        self._codepoints[CLEAR_CODE] = CLEAR_CODE
        self._codepoints[END_OF_INFO_CODE] = END_OF_INFO_CODE
        self._prefix = None
        debug(program = 'Decoder._clear_codes', text = 'dict = ' + str(self._codepoints), line = lineno())

#used in compressing
class Encoder(object):
    """
    Given an iterator of bytes, returns an iterator of integer
    codepoints, suitable for use by L{Decoder}. The core of the
    "compression" side of lzw compression/decompression.
    """
    def __init__(self, max_code_size=(2**DEFAULT_MAX_BITS)):
        """
        When the encoding codebook grows larger than max_code_size,
        the Encoder will clear its codebook and emit a CLEAR_CODE
        """
        debug(program = 'Encoder.init', text = 'start of init', line = lineno())
        self.closed = False

        self._max_code_size = max_code_size
        self._buffer = b''
        self._clear_codes()            

        if max_code_size < self.code_size():
            raise ValueError("Max code size too small, (must be at least {0})".format(self.code_size()))

    def code_size(self):
        """
        Returns a count of the known codes, including codes that are
        implicit in the data but have not yet been produced by the
        iterator.
        """
        debug(program = 'Encoder.code_size', text = 'code_size = ' + str(len(self._prefixes)), line = lineno())
        return len(self._prefixes)

    def flush(self):
        """
        Yields any buffered codepoints, followed by a CLEAR_CODE, and
        clears the codebook as a side effect.
        """
        debug(program = 'Encoder.flush', text = 'start', line = lineno())

        if self._buffer:
            yield self._prefixes[ self._buffer ]
            self._buffer = b''

        yield CLEAR_CODE
        self._clear_codes()

    def encode(self, bytesource):
        """
        Given an iterator over bytes, yields the
        corresponding stream of codepoints.
        Will clear the codes at the end of the stream.

        >>> import lzw
        >>> enc = lzw.Encoder()
        >>> [ cp for cp in enc.encode(b"gabba gabba yo gabba") ]
        [103, 97, 98, 98, 97, 32, 258, 260, 262, 121, 111, 263, 259, 261, 256]

        """
        debug(program = 'Encoder.encode', text = 'start', line = lineno())

        for b in bytesource:
            for point in self._encode_byte(b):
                debug(program = 'Encoder.encode', text = 'ascii number: ' + str(point), line = lineno())
                yield point
                

            if self.code_size() >= self._max_code_size:
                for pt in self.flush():
                    yield pt
        
        for point in self.flush():
            yield point

    def _encode_byte(self, point):
        # Yields one or zero bytes, AND changes the internal state of
        # the codebook and prefix buffer.
        #
        # Unless you're in self.encode(), you almost certainly don't
        # want to call this.

        # In python3 iterating over the bytestring will return in codepoints,
        # we use the byte([]) constructor to conver this back into bytestring
        # so we can add to new_prefix and key the _prefixes by the bytestring.
        debug(program = 'Encoder._encode_byte', line = lineno(), text = 'start, point = ' + str(point))
        byte = point if isinstance(point, six.binary_type) else six.int2byte(point)

        new_prefix = self._buffer

        if new_prefix + byte in self._prefixes:
            new_prefix = new_prefix + byte
        elif new_prefix:
            encoded = self._prefixes[ new_prefix ]
            self._add_code(new_prefix + byte)
            new_prefix = byte
            debug(program = 'Encoder._encode_byte', line = lineno(), text = 'end, flag set to = ' + str(point))
            yield encoded
        
        self._buffer = new_prefix

    def _clear_codes(self):

        # Teensy hack, CLEAR_CODE and END_OF_INFO_CODE aren't
        # equal to any possible string.
        debug(program = 'encoder._clear_codes', text = 'start', line = lineno())
        
        self._prefixes = dict( (struct.pack("B", codept), codept) for codept in range(256) )
        self._prefixes[ CLEAR_CODE ] = CLEAR_CODE
        self._prefixes[ END_OF_INFO_CODE ] = END_OF_INFO_CODE

        debug(program = 'after => Encoder._clear_codes', text = self._prefixes, line = lineno())

    def _add_code(self, newstring):
        
        #freeze here
        if M_NUMBER > 0 and len(self._prefixes) - END_OF_INFO_CODE > abs(M_NUMBER):
            debug(program = 'encoder._add_code', text = 'NEW DICTIONARY ENTRIES HAVE BEEN FROZEN, because M = ' + str(M_NUMBER) + ' and this is ' + str(len(self._prefixes) - END_OF_INFO_CODE) + 'th new dictionary. ' + 'Prefix = ' + str(newstring)  , line = lineno())

        else:
            self._prefixes[ newstring ] = len(self._prefixes)
            debug(program = 'encoder._add_code', line = lineno(), text = 'new_code added => ' + str(newstring) + '\t' + 'in [' + str(len(self._prefixes)-1) + ']' + 
            '\n' + str(self._prefixes))
            #delete here
            if M_NUMBER < 0 and len(self._prefixes) - END_OF_INFO_CODE > abs(M_NUMBER):
                debug(program = 'encoder._add_code', text = 'OLD CUSTOM DICTIONARY ENTRIES HAVE BEEN DELETED, because M = ' + str(M_NUMBER) + ' and this is ' + str(len(self._prefixes) - END_OF_INFO_CODE) + 'th new dictionary. ' + 'Prefix = ' + str(newstring)  , line = lineno())
                self._clear_codes()
                
#used in decompressing
def unpackbyte(b):
   """
   Given a one-byte long byte string, returns an integer. Equivalent
   to struct.unpack("B", b)
   """
   debug(program = 'lzw.unpackbyte', text = 'start', line = lineno())
   if isinstance(b, bytes):
       debug(program = 'lzw.unpackbyte', text = 'end, six.byte2int(b) = ' + str(six.byte2int(b)), line = lineno())
       return six.byte2int(b)
   return b

#used when using a file, so both compressing and decompressing
def filebytes(fileobj, buffersize=1024):
    """
    Convenience for iterating over the bytes in a file. Given a
    file-like object (with a read(int) method), returns an iterator
    over the bytes of that file.
    """
    debug(program = 'lzw.filebytes', text = 'start, iterating: ' + str(fileobj), line = lineno())
    buff = fileobj.read(buffersize)
    while buff:
        for byte in buff: yield byte
        buff = fileobj.read(buffersize)

#used in reading bytes from filename
def readbytes(filename, buffersize=1024):
    """
    Opens a file named by filename and iterates over the L{filebytes}
    found therein.  Will close the file when the bytes run out.
    """
    debug(program = 'lzw.readbytes', text = 'start, reading from: ' + filename, line = lineno())

    with open(filename, "rb") as infile:
        for byte in six.iterbytes(filebytes(infile, buffersize)):
            debug(program = 'lzw.readbytes', text = 'reading byte = ' + str(byte), line = lineno())
            yield six.int2byte(byte)  # TODO optimize, we are re-casting to bytes

#used in writing bytes to filename
def writebytes(filename, bytesource):
    """
    Convenience for emitting the bytes we generate to a file. Given a
    filename, opens and truncates the file, dumps the bytes
    from bytesource into it, and closes it
    """
    debug(program = 'lzw.writebytes', text = 'start, writing to: ' + filename, line = lineno())
    with open(filename, "ab") as outfile:
        for bt in bytesource:
            debug(program = 'lzw.writebytes', text = 'TO FILE: ' + str(bt), line = lineno())
            outfile.write(bt)

#used compressing
def inttobits(anint, width=None):
    
    #lzw.inttobits(304, width=16)
    #[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]

    debug(program = 'lzw.INTtoBITS', text = 'start, anint = ' + str(anint), line = lineno())
    remains = anint
    retreverse = []
    while remains:
        retreverse.append(remains & 1)
        remains = remains >> 1

    retreverse.reverse()

    ret = retreverse
    if None != width:
        ret_head = [ 0 ] * (width - len(ret))
        ret = ret_head + ret

    debug(program = 'lzw.INTtoBITS', text = 'returning: ' + str(ret), line = lineno())
    return ret

#used decompressing
def intfrombits(bits):
    
    #lzw.intfrombits([ 1, 0, 0, 1, 1, 0, 0, 0, 0 ]) => 304
    debug(program = 'lzw.INTfromBITS', text = 'start, bits = ' + str(bits), line = lineno())

    ret = 0
    lsb_first = [ b for b in bits ]
    lsb_first.reverse()
    
    for bit_index in range(len(lsb_first)):
        if lsb_first[ bit_index ]:
            ret = ret | (1 << bit_index)
    
    debug(program = 'lzw.INTfromBITS', text = 'return = ' + str(ret), line = lineno())
    return ret

#used decompressing
def bytestobits(bytesource):
    
    # [ x for x in lzw.bytestobits(b"\\x01\\x30") ] => 
    # [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    
    debug(program = 'lzw.BYTEStoBITS', text = 'start, bytes = ' + str(bytesource), line = lineno())

    for b in bytesource:

        value = unpackbyte(b)

        for bitplusone in range(8, 0, -1):
            bitindex = bitplusone - 1
            nextbit = 1 & (value >> bitindex)
            debug(program = 'lzw.BYTEStoBITS', text = 'start, nextbit = ' + str(nextbit), line = lineno())
            yield nextbit

#used compressing
def bitstobytes(bits):

    # width should be 8
    # bitstobytes([0, 0, 0, 0, 0, 0, 0, 0, "Yes, I'm True"]) == [ 0x00, 0x80 ]
    # bitstobytes([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]) == [ 0x01, 0x30 ]

    debug(program = 'lzw.BITStoBYTES', text = 'start, bits = ' + str(bits), line = lineno())

    ret = []
    nextbyte = 0
    nextbit = 7
    for bit in bits:
        if bit:
            nextbyte = nextbyte | (1 << nextbit)

        if nextbit:
            nextbit = nextbit - 1
        else:
            ret.append(nextbyte)
            nextbit = 7
            nextbyte = 0

    if nextbit < 7: ret.append(nextbyte)

    debug(program = 'lzw.BITStoBYTES', text = 'WRITING THIS ASCII NUMBER TO FILE = ' + str(ret) , line = lineno())
    
    return ret
        
