_base_ = ['./base_torchscript.py']

ir_config = dict(
    output_names=['dets', 'labels', 'masks'],
    dynamic_axes={
        'input': {
            0: 'batch',
            2: 'height',
            3: 'width'
        },
        'dets': {
            0: 'batch',
            1: 'num_dets',
        },
        'labels': {
            0: 'batch',
            1: 'num_dets',
        },
        'masks': {
            0: 'batch',
            1: 'num_dets',
            2: 'height',
            3: 'width'
        },
    })
codebase_config = dict(post_processing=dict(export_postprocess_mask=False))
