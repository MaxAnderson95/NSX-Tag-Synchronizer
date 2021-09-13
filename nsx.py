import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#Disable warnings for insecure HTTPs
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)    

class nsx_manager:
    def __init__(self, address, username, password):
        self.address = address
        self.base_url = f"https://{address}"

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'j_username': username, 'j_password': password}

        s = requests.Session()
        r = s.post(self.base_url + '/api/session/create', headers = headers, data = data, verify = False)
        if r.status_code != 200:
            raise Exception(f"Failed to connect to NSX manager {address}. HTTP status code {r.status_code}")
        else:
            print(f"Connected to NSX manager {address}.")

        self.session = s
        self.x_xsrf_token = r.headers["X-XSRF-TOKEN"]

    def __send_req(self, method, path, data = None):
        s = self.session
        headers = {'X-XSRF-TOKEN': self.x_xsrf_token}
        r = s.request(method, self.base_url + path, headers = headers, json = data, verify = False)
        return r

    def get_vms(self):
        return self.__send_req('GET', '/api/v1/fabric/virtual-machines').json()["results"]

    def get_vm(self, name):
        vms = self.get_vms()

        for vm in vms:
            if vm["display_name"] == name:
                return vm
        pass

    def get_vms_with_tags(self):
        vms = self.get_vms()
        vms_with_tags = []
        for vm in vms:
            if 'tags' in vm:
                vms_with_tags.append(vm)
        return vms_with_tags

    def add_tags(self, vm, tags):
        data = {
            'external_id': vm["external_id"],
            'tags': tags
        }

        r = self.__send_req('POST','/api/v1/fabric/virtual-machines?action=add_tags',data)
        return r

    def clear_tags(self, vm):
        data = {
            'external_id': vm["external_id"],
            'tags': []
        }

        r = self.__send_req('POST','/api/v1/fabric/virtual-machines?action=update_tags',data)
        return r

    def remove_tags(self, vm, tags):
        data = {
            'external_id': vm["external_id"],
            'tags': tags
        }

        r = self.__send_req('POST','/api/v1/fabric/virtual-machines?action=remove_tags',data)
        return r