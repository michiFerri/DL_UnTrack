from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/got10k_lmdb'
    settings.got10k_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/itb'
    settings.lasot_extension_subset_path_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasot_lmdb'
    settings.lasot_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasot'
    settings.network_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/nfs'
    settings.otb_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/otb'
    settings.prj_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack'
    settings.result_plot_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/output/test/result_plots'
    settings.results_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/output'
    settings.segmentation_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/output/test/segmentation_results'
    settings.tc128_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/trackingnet'
    settings.uav_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/uav'
    settings.vot18_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/vot2018'
    settings.vot22_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/vot2022'
    settings.vot_path = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

