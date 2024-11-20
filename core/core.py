import cv2
import os


def png_to_text(img, height=200):
    # height 不能高于250
    img_height, img_width, c = img.shape
    width = int(3 * height * img_width // img_height)
    img = cv2.resize(img, (width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    chars = 'MNHQ$OC?7>!:-;./_'
    len1 = len(chars)
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[int(255 * img[i][j] // 256 // len1)]
        result += '\n'
    return result


# 读取视频
def read_video(video_path):
    # 读取视频
    cap = cv2.VideoCapture(video_path)
    # 视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 视频总帧数
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 视频尺寸
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 视频时长
    duration = frame_count / fps
    # 视频帧率
    print('fps:', fps)
    # 视频总帧数
    print('frame_count:', frame_count)
    # 视频尺寸
    print('width:', width)
    print('height:', height)
    # 视频时长
    print('duration:', duration)
    frame_list = []
    # 读取视频帧
    for i in range(frame_count):
        ret, frame = cap.read()
        text = png_to_text(frame)
        path = video_path.split('.')[0] + 'video_frames'
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, f'{i}.txt'), 'w') as f:
            f.write(text)
        frame_list.append(text)
    cap.release()


if __name__ == '__main__':
    read_video('3.mp4')
