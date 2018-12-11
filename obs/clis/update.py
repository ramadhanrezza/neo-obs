from obs.clis.base import Base
from obs.libs.utils import orchestration, log_utils, cli_utils, prompt, ncurses, yaml_utils
from tabulate import tabulate

import os


class Update(Base):
    '''
    Usage:
        update [-i] [-f PATH]
        update [-t TEMPLATE] [-i]
        update user

    Options:
        -h --help                           Print usage
        -f PATH --file=PATH                 Set neo-obs manifest file
        -t TEMPLATE --template TEMPLATE     Create obs.yml, TEMPLATE is ENUM(user)
        -i --interactive                    Interactive form with ncurses mode

    Commands:
        user

    Tips!
        obs update -t user         update cloudian user
    
    Run 'obs update COMMAND --help' for more information on a command.
    '''
    def execute(self):
        set_file = self.args["--file"]
        default_file = orchestration.check_manifest_file()

        if set_file:
            if os.path.exists(set_file):
                default_file = set_file
            else:
                log_utils.log_err("{} file is not exists!".format(set_file))
                exit()

        if not default_file:
            log_utils.log_err("Can't find obs.yml manifest file!")
            exit()

        deploy_init = yaml_utils.file_parser(default_file)
        try:
            orchestration.do_update(deploy_init)
        except Exception as e:
            log_utils.log_err("Deploying Stack failed...")
            exit()