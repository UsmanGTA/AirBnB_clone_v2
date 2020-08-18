#!/usr/bin/python3
"""UsmanJabbar.COM"""
from fabric.api import env, run, put, local
from datetime import datetime as time
env.hosts = ['35.196.94.233', '54.160.230.10']


def do_pack():
    """
    ---------------
    METHOD: DO_PACK
    ---------------
    DESCRIPTION:
        Creates a tar compressed file
        locally containing the content
        from /web_static/ and returns the
        path of where the compressed file
        has been stored.
    NOTES:
        - Output tar files are stored inside
        the versions/ directory.
        - Output file would be called
        "web_static_" + "current time" + ".tgz"
        - If the compression fails, None's returned.
    """
    file = "web_static_" + time.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static/'.format(file))
        return("versions/{}".format(file))

    except:
        return None


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

    except:
        return False


def deploy():
    """Deploys code on the server"""

    file_path = do_pack()
    if not file_path:
        return False
    status = do_deploy(file_path)
    return status
