from tljh.hooks import hookimpl
from tljh.user import ensure_group
import sh

@hookimpl
def tljh_extra_user_conda_packages():
    return ['voila']

@hookimpl
def tljh_config_post_install(config):
    """
    Configure /srv/sharing_folder and change configs/mods
    """
    ### mkdir -p /srv/sharing_folder
    ### sudo chown  root:jupyterhub-users /srv/sharing_folder
    ### sudo chmod 777 /srv/sharing_folder
    ### sudo chmod g+s /srv/sharing_folder
    ### sudo ln -s /srv/scratch /etc/skel/sharing_folder
    sh.mkdir('/srv/scratch', '-p')
    # jupyterhub-users doesn't get created until a user logs in
    # make sure it's created before changing permissions on directory
    ensure_group('jupyterhub-users') 
    sh.chown('root:jupyterhub-users', '/srv/sharing_folder')
    sh.chmod('777', '/srv/sharing_folder')
    sh.chmod('g+s', '/srv/sharing_folder')
    sh.ln('-s', '/srv/scratch', '/etc/skel/sharing_folder')

    
    
    
