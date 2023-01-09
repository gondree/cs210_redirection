import os, hashlib
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends the message to a stream')
    parser.add_argument('msg', nargs='+', type=str, help='The message to write to a stream')
    parser.add_argument('--switch', action='store_true', default=False,
                        help='Alterate sending args to stdin/stdout')
    args = parser.parse_args()

    if args.switch:
        for idx, msg in enumerate(args.msg):
             os.write((idx % 2)+1, msg.encode('utf-8'))
        os.write(1, b'\n')
        exit()

    msg = ' '.join(args.msg).encode('utf-8')

    h = hashlib.new('sha1')
    h.update(msg)
    digest = h.hexdigest()
    fd = int(digest, base=16) % 3

    if fd == 0:
        print(msg[::-1].decode('utf-8'))
    else:
        os.write(fd, msg + b'\n')

