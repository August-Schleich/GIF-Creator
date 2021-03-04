import imageio
import os

clip = os.path.abspath('IMG_0223.MOV')

def gif_maker(input_path,target_format):
    output_path = os.path.splitext(input_path)[0] + target_format

    print(f'converting {input_path} \n to {output_path}')

    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path,fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frames {frames}')
    print('Done!')
    writer.close()






















