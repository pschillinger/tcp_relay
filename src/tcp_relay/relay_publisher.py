import rospy
import threading
import socket
import select
import pickle

class RelayPublisher(threading.Thread):

	def __init__(self, topic, msg_type, address, latch=False, queue_size=10):
		threading.Thread.__init__(self)
		self.setDaemon(True)

		self._pub = rospy.Publisher(topic, msg_type, latch=latch, queue_size=queue_size)
		self._address = address

		self.start()


	def run(self):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(self._address)
		server.listen(1)

		connections = list()

		while not rospy.is_shutdown():

			rlist, wlist, xlist = select.select([server] + connections, [], [])

			for s in rlist:

				if s is server:
					(conn, address) = s.accept()
					connections.append(conn)

				else:
					data = s.recv(8096)

					if data:
						msg = pickle.loads(data)
						self._pub.publish(msg)

					else:
						connections.remove(s)
						s.close()

		server.close()
		server.shutdown(socket.SHUT_RDWR)


