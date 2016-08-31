import rospy
import threading
import socket
import pickle

class RelaySubscriber(object):

	def __init__(self, topic, msg_type, address):
		self._sub = rospy.Subscriber(topic, msg_type, self._msg_cb)
		
		r = rospy.Rate(1)
		while not rospy.is_shutdown():
			try:
				self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self._client.connect(address)
				break
			except socket.error:
				rospy.logwarn('Waiting for socket %s...' % str(address))
				r.sleep()


	def _msg_cb(self, msg):
		data = pickle.dumps(msg)
		self._client.sendall(data)
