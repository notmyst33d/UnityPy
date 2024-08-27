from .Object import Object
from ..streams import EndianBinaryWriter

class BuildSettings(Object):
    def __init__(self, reader):
        super().__init__(reader=reader)
        self.version_tuple = self.version
        self.scenes = reader.read_string_array()

        # Tested with Unity 2020.3.25f
        if self.version_tuple >= (2020, 3,):
            # I have no idea which type of data
            # is stored in these arrays, it's
            # probably gonna crash when there is
            # actual data in these fields
            self.preloaded_plugins = reader.read_int_array()
            self.enabled_vr_devices = reader.read_int_array()
            self.build_tags = reader.read_int_array()

            self.guid = reader.read_bytes(16)
            self.has_pro_version = reader.read_boolean()
            self.is_no_watermark_build = reader.read_boolean()
            self.is_prototyping_build = reader.read_boolean()
            self.is_educational_build = reader.read_boolean()
            self.is_embedded = reader.read_boolean()
            self.is_trial = reader.read_boolean()
            self.has_publishing_rights = reader.read_boolean()
            self.has_shadows = reader.read_boolean()
            self.has_soft_shadows = reader.read_boolean()
            self.has_local_light_shadows = reader.read_boolean()
            self.has_advanced_version = reader.read_boolean()
            self.enable_dynamic_batching = reader.read_boolean()
            self.is_debug_build = reader.read_boolean()
            self.uses_on_mouse_events = reader.read_boolean()
            self.has_cluster_rendering = reader.read_boolean()
            self.unknown = reader.read_boolean()
            self.version = reader.read_aligned_string()
            self.auth_token = reader.read_aligned_string()
            self.graphics_apis = reader.read_int_array()
        else:
            self.has_render_texture = reader.read_boolean()
            self.has_pro_version = reader.read_boolean()
            self.has_publishing_rights = reader.read_boolean()
            self.has_shadows = reader.read_boolean()
            self.version = reader.read_aligned_string()

    def save(self, writer: EndianBinaryWriter = None):
        if writer is None:
            writer = EndianBinaryWriter(endian=self.reader.endian)

        super().save(writer)
        writer.write_string_array(self.scenes)

        # Tested with Unity 2020.3.25f
        if self.version_tuple >= (2020, 3,):
            # I have no idea which type of data
            # is stored in these arrays, it's
            # probably gonna crash when there is
            # actual data in these fields
            writer.write_int_array(self.preloaded_plugins, write_length=True)
            writer.write_int_array(self.enabled_vr_devices, write_length=True)
            writer.write_int_array(self.build_tags, write_length=True)

            writer.write(self.guid)
            writer.write_boolean(self.has_pro_version)
            writer.write_boolean(self.is_no_watermark_build)
            writer.write_boolean(self.is_prototyping_build)
            writer.write_boolean(self.is_educational_build)
            writer.write_boolean(self.is_embedded)
            writer.write_boolean(self.is_trial)
            writer.write_boolean(self.has_publishing_rights)
            writer.write_boolean(self.has_shadows)
            writer.write_boolean(self.has_soft_shadows)
            writer.write_boolean(self.has_local_light_shadows)
            writer.write_boolean(self.has_advanced_version)
            writer.write_boolean(self.enable_dynamic_batching)
            writer.write_boolean(self.is_debug_build)
            writer.write_boolean(self.uses_on_mouse_events)
            writer.write_boolean(self.has_cluster_rendering)
            writer.write_boolean(self.unknown)
            writer.write_aligned_string(self.version)
            writer.write_aligned_string(self.auth_token)
            writer.write_int_array(self.graphics_apis, write_length=True)
        else:
            writer.write_boolean(self.has_render_texture)
            writer.write_boolean(self.has_pro_version)
            writer.write_boolean(self.has_publishing_rights)
            writer.write_boolean(self.has_shadows)
            writer.write_aligned_string(self.version)

        self.set_raw_data(writer.bytes)