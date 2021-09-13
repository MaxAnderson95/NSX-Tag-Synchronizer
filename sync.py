from nsx import nsx_manager
from util import compare_tags
from util import concat_tags
from args import getargs

args = getargs()

nsx_src = nsx_manager(args.nsx_host_source, args.user_source, args.password_source)

nsx_dest = nsx_manager(args.nsx_host_destination, args.user_destination, args.password_destination)

print("")

#get vms in source cluster
src_vms_with_tags = nsx_src.get_vms_with_tags()

#loop through each source vm with tags
for src_vm in src_vms_with_tags:
    #check for a matching vm in the destination manager
    dest_vm = nsx_dest.get_vm(src_vm["display_name"])
    if dest_vm:
        #Check if tags key is present at all (blank or otherwise)
        if 'tags' in dest_vm: 
            missing_tags = compare_tags(src_vm["tags"], dest_vm["tags"])
        else:
            missing_tags = src_vm["tags"]
        if missing_tags or 'tags' not in dest_vm:
            #If missing tags found or no tags key exists in dest, sync them
            print(f"Syncing new tags found for {dest_vm['display_name']}:")
            print(concat_tags(missing_tags))
            print("")
            nsx_dest.add_tags(dest_vm, missing_tags)
