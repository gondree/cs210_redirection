import os, hashlib
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends the message to a stream')
    parser.add_argument('msg', nargs='+', type=str, help='The message to write to a stream')
    args = parser.parse_args()

    msg = ' '.join(args.msg).encode('utf-8')

    h = hashlib.new('sha1')
    h.update(msg)
    digest = h.hexdigest()
    fd = int(digest, base=16) % 3

    if fd == 0:
        print(msg[::-1])
    else:
        os.write(fd, msg) 
        print()

