import swiftclient
from keystoneclient.v2_0 import client
import hmac
from hashlib import sha1
from time import time
import config as cfg

class ObjectStore:
      def __init__(self):
           keystone = client.Client(username=cfg.SWIFT_USER, password=cfg.SWIFT_PASS, tenant_name=cfg.TENANT_NAME, auth_url=cfg.KEYSTONE_AUTH_URL)
           self.tenant_id = keystone.auth_tenant_id
           print self.tenant_id
           self.swift = swiftclient.client.Connection(auth_version=cfg.KEYSTONE_AUTH_VERSION,
                                                user=cfg.SWIFT_USER,
                                                key=cfg.SWIFT_PASS,
                                                tenant_name=cfg.TENANT_NAME,
                                                authurl=cfg.KEYSTONE_AUTH_URL)
           resp = self.swift.__dict__
           for k,v in resp.items():
               print "%s - %s" %(k,v)
      def list_containers(self,swift):
          resp, containers = swift.get_account()
          for container in containers:
              for k,v in container.items():
                  print '%s -- %s' %(k,v)

      def put_object(self,container,name,obj):
          etag = self.swift.put_object(container,name,obj)
          print etag
 
      def get_account_stats(self):
          response = self.swift.head_container('appdata-container')
          print response
          print type(response)
          for k,v in response.items():
               print "%s - %s" %(k,v)
      
      def get_temp_url(self, container,obj, expire_after):
          method = 'GET'
          expires = int(time() + expire_after*60)
          path = '/v1/AUTH_%s/%s/%s' %(self.tenant_id, container,obj)
          key = 'secret'
          hmac_body = '%s\n%s\n%s' %(method, expires, path)
          sig = hmac.new(key, hmac_body, sha1).hexdigest()
          s = 'http://10.1.10.130:8080{path}?temp_url_sig={sig}&temp_url_expires={expires}'
          url = s.format(path=path,sig=sig,expires=expires)
          print url
          return url

if __name__ == '__main__':
    sw = ObjectStore()
    swift = sw.swift
    sw.list_containers(swift)
    sw.get_account_stats()
    sw.get_temp_url_for_object('test_container1','user-guide.pdf', 60)
