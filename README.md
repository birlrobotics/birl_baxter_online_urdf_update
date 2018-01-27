# Overview
This package is for online updating baxter's URDF(fig1). Due to the reason that baxter will reset its URDF when restart it every time. So in our case, we installed a FT sensor(fig2) in baxter's arm which means we need update its urdf with FT sensor otherwise the pose of gripper can not be retrived accurately.

# Reference
[Gripper Customization](http://sdk.rethinkrobotics.com/wiki/Gripper_Customization)
# How to use it
 Get your computer's current time with this bash command
` $ date +'secs:%s   nsecs:%N'`
 Publish the URDFConfiguration message to the /robot/urdf topic. From a baxter.sh shell: 
 `$ rostopic pub -l /robot/urdf baxter_core_msgs/URDFConfiguration -f ***.yaml`
Now, to view our masterpiece in RViz: 
`$ rosrun rviz rviz`

Baxter URDF without FT sensor
![Fig1](https://github.com/birlrobotics/birl_baxter_online_urdf_update/blob/master/media/baxter_no_ft_sensor.png)

Baxter URDF with FT sensor
![Fig2](https://github.com/birlrobotics/birl_baxter_online_urdf_update/blob/master/media/baxter_with_ft_sensor.png)
