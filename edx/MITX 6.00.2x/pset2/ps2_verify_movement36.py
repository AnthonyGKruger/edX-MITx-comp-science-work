3
m�X$  �               @   s   ddd�Z dS )皙�����?c             C   sd   ddl }|dd�}| |d�}|jddd|�}x*|j� |j� k rV|j�  |j||g� q.W |j�  dS )zO
    Runs a simulation of a single robot of type robot_type in a 5x5 room.
    �    N�   �   )�ps2_visualizeZRobotVisualizationZgetNumCleanedTilesZgetNumTilesZupdatePositionAndClean�update�done)Z
robot_typeZ	room_typeZdelayr   ZroomZrobotZanim� r   �ps2_verify_movement36.py�testRobotMovement
   s    

r
   N)r   )r
   r   r   r   r	   �<module>
   s    