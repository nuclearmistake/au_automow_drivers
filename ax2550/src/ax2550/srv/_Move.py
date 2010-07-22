# autogenerated by genmsg_py from MoveRequest.msg. Do not edit.
import roslib.message
import struct


class MoveRequest(roslib.message.Message):
  _md5sum = "93d42aa924f3e31d0e39ee842f5a0642"
  _type = "ax2550/MoveRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 speed
float32 direction

"""
  __slots__ = ['speed','direction']
  _slot_types = ['float32','float32']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   speed,direction
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(MoveRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.speed is None:
        self.speed = 0.
      if self.direction is None:
        self.direction = 0.
    else:
      self.speed = 0.
      self.direction = 0.

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<2f', self.speed, self.direction))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      end = 0
      start = end
      end += 8
      (self.speed, self.direction,) = struct.unpack('<2f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<2f', self.speed, self.direction))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      end = 0
      start = end
      end += 8
      (self.speed, self.direction,) = struct.unpack('<2f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

# autogenerated by genmsg_py from MoveResponse.msg. Do not edit.
import roslib.message
import struct


class MoveResponse(roslib.message.Message):
  _md5sum = "034a8e20d6a306665e3a5b340fab3f09"
  _type = "ax2550/MoveResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 result


"""
  __slots__ = ['result']
  _slot_types = ['int32']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   result
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(MoveResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = 0
    else:
      self.result = 0

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<i', self.result))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      end = 0
      start = end
      end += 4
      (self.result,) = struct.unpack('<i',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<i', self.result))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      end = 0
      start = end
      end += 4
      (self.result,) = struct.unpack('<i',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

class Move(roslib.message.ServiceDefinition):
  _type          = 'ax2550/Move'
  _md5sum = '25e98ccadfa44705f7e9f9aa4e16eae6'
  _request_class  = MoveRequest
  _response_class = MoveResponse
