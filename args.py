import argparse

def get_arg_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-hS', '--nsx_host_source', type=str, required=True,
                            help='NSX host to pull tags from')
    arg_parser.add_argument('-uS', '--user_source', type=str, default="admin", required=True,
                            help='User to authenticate as to the source host')
    arg_parser.add_argument('-pS', '--password_source', type=str, required=True,
                            help='Password to authenticate with to the source host')
    arg_parser.add_argument('-hD', '--nsx_host_destination', type=str, required=True,
                            help='NSX host to replicate tags to')
    arg_parser.add_argument('-uD', '--user_destination', type=str, default="admin", required=True,
                            help='User to authenticate as to the source host')
    arg_parser.add_argument('-pD', '--password_destination', type=str, required=True,
                            help='Password to authenticate with to the source host')
    
    return arg_parser

def getargs():
    parser = get_arg_parser()
    args = parser.parse_args()
    return args