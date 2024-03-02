# coding:utf-8

import argparse

import itertools as its


def run_default(length, filename):
    global words
    '''
    words='ha'
    
    if numonly == True:
        words="1234567890"
    else:
        words="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    '''
    words = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    r = its.product(words, repeat=length)
    dic = open(filename, 'a')
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()


def run_numonly(length, filename):
    global words
    words = "1234567890"
    r = its.product(words, repeat=length)
    dic = open(filename, 'a')
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()


def run_letteronly(length, filename):
    global words
    words = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    r = its.product(words, repeat=length)
    dic = open(filename, 'a')
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()


if __name__ == "__main__":
    choices = {"default":run_default, "numonly":run_numonly, "letteronly":run_letteronly}
    parser = argparse.ArgumentParser(description='快速生成密码字典')
    parser.add_argument('model', choices=choices, help='选择哪个模式运行')
    parser.add_argument('--length', metavar='length', type=int, default=3, help="密码字典内密码的长度")
    parser.add_argument('-filename', metavar='filename', type=str, default='password.txt', help="密码字典文件昵称")
    # parser.add_argument('-numonly',metavar='numonly',type=bool,default=False,help="是否只含有数字")
    args = parser.parse_args()
    func = choices[args.model]
    func(args.length, args.filename)
    
    
