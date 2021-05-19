import numpy as np

from stanford_quad.sim.procedural_generation.box_pybullet import BoxPybullet

class Floor:

    def __init__(self, p, pos, orientation, size, color):
        """
         Floor create BoxPybullet attached to the ground, it can attach/spawn objects on it's surface.
        :param p:
        :param pos:
        :param orientation:
        :param size:
        :param color:
        """
        self.p = p
        self.pos = pos
        self.orientation = orientation
        self.size = size
        self.color = color
        self.uid = None

    def create(self):
        floor_obj = BoxPybullet(self.p, self.pos, self.orientation, self.size, self.color, False).create()
        self.uid = floor_obj

        return floor_obj

    def get_half_x_size(self):
        return self.size[0]

    def get_half_y_size(self):
        return self.size[1]

    def get_half_z_size(self):
        return self.size[2]

    def get_full_x_size(self):
        return self.size[0] * 2

    def get_full_y_size(self):
        return self.size[1] * 2

    def get_full_z_size(self):
        return self.size[2] * 2

    def put_on(self, object_uid, floor_x_pos, floor_y_pos, half_height_object):
        """
        Place an object on the floor based on the relative floor position.
        :param int object_uid: Must be a valid object in pybullet scene.
        :param float floor_x_pos: relative to top right corner of the floor. Must be between 0 and 1!
        :param float floor_y_pos: relative to top right corner of the floor. Must be between 0 and 1!
        :param float object_height: TODO: find it automatically in the future.
        """
        # Floor relative pos to world pos
        object_world_x_pos = self.pos[0] - self.get_half_x_size() + floor_x_pos * self.get_full_x_size()
        object_world_y_pos = self.pos[1] - self.get_half_y_size() + floor_y_pos * self.get_full_y_size()
        object_world_z_pos = self.get_half_z_size() + half_height_object
        new_object_pos = [object_world_x_pos, object_world_y_pos, object_world_z_pos]

        # get original object orientation
        _, object_orn = self.p.getBasePositionAndOrientation(object_uid)
        self.p.resetBasePositionAndOrientation(object_uid, new_object_pos, object_orn)