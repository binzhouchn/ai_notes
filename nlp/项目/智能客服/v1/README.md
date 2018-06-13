## 智能客服第一版更新 20180612

1. 替换site-package中的ChatterBot-0.8.7-py3.5.egg（如果已经安装chatterbot的话），没有安装就把该文件放进去

2. 将robotpath.pth放到site-package下面

3. \__main__文件放在任何位置都行，启动flask5000端口，直接./start_robot.sh,然后可以用postman工具发送post请求发送报文


注:<br>
其他机器上部署的时候注意有些路径需要替换，<br>
robotpath.pth<br>
sn_config文件夹下的robot_config.py, robot_logging.conf<br>
任意位置chatterbot_robot文件夹下的start_robot.sh和robot_main.py中的端口地址<br>

note:<br>
sn_开头的为增加代码，修改代码中会加入本人作者标记
