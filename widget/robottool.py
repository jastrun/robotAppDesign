import roboticstoolbox as rtb



robot = rtb.models.DH.MYROBOT()
qt = rtb.tools.trajectory.jtraj(robot.qz, robot.qr, 50)
robot.plot(qt.q)