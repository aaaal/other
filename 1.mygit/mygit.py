import os
import re
import sys


def get_remote_url(args):
    if len(args) > 1 and args[1] == 'clone':
        info = args[2]
        return get_remote_url_from_line(info)
    else:
        git_config_path = './.git/config'
        try:
            with open(git_config_path) as git_file:
                git_info = git_file.read()
                lines = git_info.split('\n')
                for i in range(len(lines)):
                    if lines[i] == '[remote "origin"]':
                        info = lines[i + 1]
                        return get_remote_url_from_line(info)
        except FileNotFoundError:
            return


def get_remote_url_from_line(line):
    pattern = r'(.+)@(.+):(.+)'
    group = re.search(pattern, line)
    return group[2]


def get_identity_file(hostname):
    homedir = os.environ['HOME']
    ssh_config_path = homedir + '/.ssh/config'
    if hostname:
        try:
            with open(ssh_config_path) as config_file:
                config = config_file.read()
                blocks = config.split('\n\n')
                for block in blocks:
                    lines = block.split('\n')
                    host_name = lines[0].split(' ')[1]
                    if host_name == hostname:
                        for i in range(len(lines)):
                            words = lines[i].split(' ')
                            for word in words:
                                if word == 'IdentityFile':
                                    return words[1]
        except FileNotFoundError:
            return
    else:
        return


def build_param(args):
    param = ''
    for i in range(len(args)):
        if i > 0:
            param = param + ' ' + args[i]
    return param


def build_cmd(id_rsa, param, args):
    if id_rsa:
        if len(args) > 1:
            second = args[1]
            if second == 'clone' or second == 'push' or second == 'pull':
                return "GIT_SSH_COMMAND='ssh -i " + id_rsa + "' git" + param
    return 'git' + param


git_param = build_param(sys.argv)
host = get_remote_url(sys.argv)
identity_file = get_identity_file(host)
if identity_file:
    print(build_cmd(identity_file, git_param, sys.argv))
else:
    print('git' + git_param)
