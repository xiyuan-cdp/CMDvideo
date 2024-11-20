import os
import sys
import time

first = True


def play_video(path: str):
    """
    播放视频
    :param path: 视频包路径
    :return:
    """
    global first
    len1 = 0
    for i in range(len(os.listdir(path))):
        with open(os.path.join(path, f'{i}.txt'), 'r') as f:
            frame = f.read()
        if first:
            # 首次打印内容
            first_print(frame)
            first = False
        else:
            # 更新屏幕内容
            update_screen(frame, len1)
        len1 = frame.count('\n')
        # 等待0.02秒
        time.sleep(0.023)




def update_screen(new_content, line):
    """
    更新屏幕内容
    只适用于window，其它系统还没测试
    :param new_content: 新的内容
    :param line: 之前的行数
    """
    sys.stdout.write(f"\033[{line}F\033[K" + new_content)
    sys.stdout.flush()


def first_print(text):
    """
    首次打印内容
    :param text:
    :return:
    """
    os.system('cls')
    sys.stdout.write("\r{0}".format(text))
    sys.stdout.flush()


if __name__ == '__main__':
    start = time.time()
    play_video('3video_frames')
    end = time.time()
    print(f'耗时：{end - start}秒')