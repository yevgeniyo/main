#!/usr/bin/env python

#TEST_0 = "tempest.api.compute.volumes.test_volumes_list.VolumesTestJSON.test_volume_list"
#TEST_1 = "tempest.api.compute.volumes.test_volume_snapshots.VolumesSnapshotsTestJSON.test_volume_snapshot_create_get_list_delete"
##TEST_2 = "tempest.api.volume.test_volumes_actions.VolumesV1ActionsTest.test_attach_detach_volume_to_instance"
#TEST_2 = "tempest.api.volume.test_volumes_actions.VolumesV1ActionsTest.test_volume_bootable"
#TEST_3 = "tempest.api.volume.test_volumes_actions.VolumesV1ActionsTest.test_volume_upload"
#TEST_4 = "tempest.api.volume.test_volumes_actions.VolumesV2ActionsTest.test_volume_bootable"
#TEST_5 = "tempest.api.volume.test_volumes_snapshots.VolumesV2SnapshotTestJSON.test_volume_from_snapshot"


TEST_1 = "testr run tempest.api.compute.volumes.test_scaleio_compute.VolumesTestJSON.test_volume_list"
TEST_2 = "tempest.api.compute.servers.test_delete_server.DeleteServersTestJSON.test_delete_server_while_in_attached_volume"
TEST_3 = "tempest.api.volume.test_volumes_extend.VolumesV2ExtendTest.test_volume_extend"
TEST_4 = "tempest.api.volume.test_volumes_get.VolumesV1GetTest.test_volume_create_get_update_delete_from_image"  #(change before vol size)
TEST_5 = "tempest.api.volume.test_volumes_snapshots.VolumesV1SnapshotTestJSON.test_snapshot_create_get_list_update_delete"
TEST_6 = "tempest.api.volume.test_volumes_snapshots.VolumesV1SnapshotTestJSON.test_volume_from_snapshot"
TEST_7 = "tempest.api.volume.test_volumes_actions.VolumesV1ActionsTest.test_volume_upload"
TEST_8 = "tempest.api.volume.test_volumes_get.VolumesV2GetTest.test_volume_create_get_update_delete_as_clone"
TEST_9 = "tempest.api.volume.test_volumes_snapshots.VolumesV1SnapshotTestJSON.test_snapshot_create_get_list_update_delete"
TEST_10 = "tempest.api.compute.volumes.test_volumes_get.VolumesGetTestJSON.test_volume_create_get_delete"
TEST_11 = "tempest.api.compute.servers.test_delete_server.DeleteServersTestJSON.test_delete_server_while_in_attached_volume"
TEST_12 = "tempest.api.compute.volumes.test_scaleio_compute.VolumesTestJSON.test_volume_list"
TEST_13 = "tempest.api.volume.test_volumes_extend.VolumesV2ExtendTest.test_volume_extend"
TEST_14 = "tempest.api.volume.admin.test_volumes_actions.VolumesActionsV1Test.test_volume_force_delete_when_volume_is_error"
TEST_15 = "tempest.api.volume.test_volumes_actions.VolumesV1ActionsTest.test_volume_bootable"
TEST_16 = "tempest.api.volume.test_volumes_actions.VolumesV2ActionsTest.test_volume_upload"
TEST_17 = "tempest.api.volume.test_volumes_get.VolumesV2GetTest._volume_create_get_update_delete"
TEST_18 = "tempest.api.volume.test_volumes_get.VolumesV2GetTest.test_volume_create_get_update_delete_from_image"
TEST_19 = "tempest.api.volume.test_volumes_get.VolumesV2GetTest.test_volume_create_get_update_delete_as_clone"

TEST_20 = "tempest.api.volume.admin.test_volumes_backup.VolumesBackupsV2Test"

#Negative:
TEST_21 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_get_nonexistent_volume_id"
TEST_22 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_delete_nonexistent_volume_id"
TEST_23 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_invalid_size"
TEST_24 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_out_passing_size"
TEST_25 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_size_zero"
TEST_26 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_size_negative"
TEST_27 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_nonexistent_volume_type"
TEST_28 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_nonexistent_snapshot_id"
TEST_29 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_create_volume_with_nonexistent_source_volid"
TEST_30 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_extend_with_size_smaller_than_original_size"
TEST_31 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_extend_with_non_number_size"
TEST_32 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_extend_with_None_size"
TEST_33 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_extend_with_nonexistent_volume_id"
TEST_34 = "tempest.api.volume.test_volumes_negative.VolumesV2NegativeTest.test_volume_extend_without_passing_volume_id"
