# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from quadrotor_msgs/PositionCommand.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class PositionCommand(genpy.Message):
  _md5sum = "4712f0609ca29a79af79a35ca3e3967a"
  _type = "quadrotor_msgs/PositionCommand"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
geometry_msgs/Point position
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration
float64 yaw
float64 yaw_dot
float64[3] kx
float64[3] kv 

uint32 trajectory_id

uint8 TRAJECTORY_STATUS_EMPTY = 0
uint8 TRAJECTORY_STATUS_READY = 1
uint8 TRAJECTORY_STATUS_COMPLETED = 3
uint8 TRAJECTROY_STATUS_ABORT = 4
uint8 TRAJECTORY_STATUS_ILLEGAL_START = 5
uint8 TRAJECTORY_STATUS_ILLEGAL_FINAL = 6
uint8 TRAJECTORY_STATUS_IMPOSSIBLE = 7

# Its ID number will start from 1, allowing you comparing it with 0.
uint8 trajectory_flag

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  # Pseudo-constants
  TRAJECTORY_STATUS_EMPTY = 0
  TRAJECTORY_STATUS_READY = 1
  TRAJECTORY_STATUS_COMPLETED = 3
  TRAJECTROY_STATUS_ABORT = 4
  TRAJECTORY_STATUS_ILLEGAL_START = 5
  TRAJECTORY_STATUS_ILLEGAL_FINAL = 6
  TRAJECTORY_STATUS_IMPOSSIBLE = 7

  __slots__ = ['header','position','velocity','acceleration','yaw','yaw_dot','kx','kv','trajectory_id','trajectory_flag']
  _slot_types = ['std_msgs/Header','geometry_msgs/Point','geometry_msgs/Vector3','geometry_msgs/Vector3','float64','float64','float64[3]','float64[3]','uint32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,position,velocity,acceleration,yaw,yaw_dot,kx,kv,trajectory_id,trajectory_flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PositionCommand, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Vector3()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Vector3()
      if self.yaw is None:
        self.yaw = 0.
      if self.yaw_dot is None:
        self.yaw_dot = 0.
      if self.kx is None:
        self.kx = [0.] * 3
      if self.kv is None:
        self.kv = [0.] * 3
      if self.trajectory_id is None:
        self.trajectory_id = 0
      if self.trajectory_flag is None:
        self.trajectory_flag = 0
    else:
      self.header = std_msgs.msg.Header()
      self.position = geometry_msgs.msg.Point()
      self.velocity = geometry_msgs.msg.Vector3()
      self.acceleration = geometry_msgs.msg.Vector3()
      self.yaw = 0.
      self.yaw_dot = 0.
      self.kx = [0.] * 3
      self.kv = [0.] * 3
      self.trajectory_id = 0
      self.trajectory_flag = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_11d().pack(_x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.acceleration.x, _x.acceleration.y, _x.acceleration.z, _x.yaw, _x.yaw_dot))
      buff.write(_get_struct_3d().pack(*self.kx))
      buff.write(_get_struct_3d().pack(*self.kv))
      _x = self
      buff.write(_get_struct_IB().pack(_x.trajectory_id, _x.trajectory_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Vector3()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.acceleration.x, _x.acceleration.y, _x.acceleration.z, _x.yaw, _x.yaw_dot,) = _get_struct_11d().unpack(str[start:end])
      start = end
      end += 24
      self.kx = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 24
      self.kv = _get_struct_3d().unpack(str[start:end])
      _x = self
      start = end
      end += 5
      (_x.trajectory_id, _x.trajectory_flag,) = _get_struct_IB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_11d().pack(_x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.acceleration.x, _x.acceleration.y, _x.acceleration.z, _x.yaw, _x.yaw_dot))
      buff.write(self.kx.tostring())
      buff.write(self.kv.tostring())
      _x = self
      buff.write(_get_struct_IB().pack(_x.trajectory_id, _x.trajectory_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Vector3()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.acceleration.x, _x.acceleration.y, _x.acceleration.z, _x.yaw, _x.yaw_dot,) = _get_struct_11d().unpack(str[start:end])
      start = end
      end += 24
      self.kx = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      start = end
      end += 24
      self.kv = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      _x = self
      start = end
      end += 5
      (_x.trajectory_id, _x.trajectory_flag,) = _get_struct_IB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_11d = None
def _get_struct_11d():
    global _struct_11d
    if _struct_11d is None:
        _struct_11d = struct.Struct("<11d")
    return _struct_11d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_IB = None
def _get_struct_IB():
    global _struct_IB
    if _struct_IB is None:
        _struct_IB = struct.Struct("<IB")
    return _struct_IB
