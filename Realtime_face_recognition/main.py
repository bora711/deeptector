from real_time_face_recognition import stream

camera_source = 0  # can be also the path of a clip
## 모델경로
pb_path = r".\Face_Recognition3\pb_model.pb"
node_dict = {'input': 'input:0',
             'keep_prob': 'keep_prob:0',
             'phase_train': 'phase_train:0',
             'embeddings': 'embeddings:0',
             }

## 회원 DB 경로
ref_dir = r".\database"
stream(pb_path, node_dict, ref_dir, camera_source=camera_source, resolution="720", to_write=False, save_dir=None)


