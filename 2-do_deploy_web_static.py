#!/usr/bin/python3
"""usmanjabbar.com"""
from fabric.api import env, run, put
web01, web02 = '35.196.94.233', '54.160.230.10'
env.hosts = [web01, web02]


def do_deploy(archive_path):
    """
    -----------------
    METHOD: DO_DEPLOY
    -----------------
    DESCRIPTION:
        This method distributes and
        deploys an archive of web_static
        files
    ARGS:
        - Takes in a string with the path
        to the archive file
    NOTES:
        - If the archive_path doesn't exist,
        returns False
    """
    from os.path import isfile

    # Check if that file actually exists
    if not isfile(archive_path):
        return False

    try:
        # Extract the file name from the var 'archive_path'
        archive = archive_path.split('/')[-1]

        # Upload, uncompress and delete the archive from the web servers
        put(archive_path, '/tmp/')
        out = '/data/web_static/releases/{}/'.format(archive.split('.')[0])
        run('mkdir -p {}'.format(out))
        run('tar -xzf /tmp/{} -C {}'.format(archive, out))
        run('rm -rf /tmp/{}'.format(archive))
        run('mv {}* {}'.format(out + 'web_static/', out))
        run('rm -rf {}'.format(out + 'web_static/'))

        # Del symbolic link 'current' and link extracted folder to current
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(out))

        # All good, return True
        print('New version deployed!')
        return True

    except Exception as e:
        return False
