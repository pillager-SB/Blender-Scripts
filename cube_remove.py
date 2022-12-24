bl_info = {
    "name": "Cube Remove",
    "author": "pillager <pillager@bk.ru>",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "category": "Mesh",
    "location": "3D Viewport",
    "description": "Remove Zero Cube",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

import bpy
from time import sleep
from math import pi


class MESH_REMOVE_OT_cube_remove(bpy.types.Operator):
    '''Как увидишь его - убей!'''
    bl_idname = 'mesh.cube_remove'
    bl_label = 'Cube Annihilation'
    bl_options = {'UNDO', 'REGISTER'}

    @classmethod
    def poll(cls, context):
        return 'Cube' in bpy.data.meshes

    def execute(self, context):
        def rotate_object_on_z(self, context):
            mesh = bpy.data.meshes['Cube']
            frame = bpy.context.scene.frame_current_final
            try:
                bpy.data.objects['Cube'].rotation_euler[2] = frame / 6 * pi
                bpy.data.objects['Cube'].scale[0] = 1 / (frame / 10 + 1)
                bpy.data.objects['Cube'].scale[1] = 1 / (frame / 10 + 1)
                bpy.data.objects['Cube'].scale[2] = 1 / (frame / 10 + 1)
                if frame == 60:
                    bpy.data.meshes.remove(mesh)
                    bpy.ops.screen.animation_cancel()
                    bpy.ops.screen.animation_set(0)
            except:
                ...

        bpy.ops.screen.animation_play()
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_pre.append(rotate_object_on_z)

        return {'FINISHED'}


class VIEW3D_PT_cube_remove(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'No Cube'
    bl_label = 'Cube Annihilation'

    def draw(self, context):
        self.layout.operator('mesh.cube_remove',
                             text='Cube',
                             icon='CANCEL')


class_lst = [MESH_REMOVE_OT_cube_remove, VIEW3D_PT_cube_remove]


def register():
    [bpy.utils.register_class(i) for i in class_lst]


def unregister():
    [bpy.utils.unregister_class(i) for i in class_lst]
