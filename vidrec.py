#! /usr/bin/env python
import sys
import argparse
import cv2


def main():
    args = parse_args()
    print(args.file)
    print(args.width)
    print(args.height)
    print(args.color)
    print(args.codec)
    print(args.fps)
    record_video()
    return 0


def record_video(filename='output.avi', width=640, height=480, color=True,
                 fps=20, codec='MJPG'):

    # TODO: Add ability to select the camera
    # Open video
    cap = cv2.VideoCapture(1)

    # Define the codec and create the VideoWriterobject
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is True:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return 0


def parse_args():
    parser = argparse.ArgumentParser(description='Record video from a webcam.')
    parser.add_argument('file', type=str, help='Path to file to be created')
    # TODO: Add allowable options instead (VGA, QVGA etc.)
    parser.add_argument('-sw', '--width', nargs='?', default=640, type=int,
                        help='Video width', dest='width')
    parser.add_argument('-sh', '--height', nargs='?', default=480, type=int,
                        help='Video height', dest='height')
    # TODO: Have y/n as tuple of options
    parser.add_argument('-c', '--color', nargs='?', default=True, type=bool,
                        help='Record in color', dest='color')
    # TODO: Add options
    parser.add_argument('-cc', '--codec', nargs='?', default='MJPG', type=str,
                        help='Codec to use', dest='codec')
    parser.add_argument('-f', '--fps', nargs='?', default=20, type=int,
                        help='Frames per second', dest='fps')
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    # main should return 0 for success, something else for error.
    sys.exit(main())
