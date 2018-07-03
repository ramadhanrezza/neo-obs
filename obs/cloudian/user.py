from .requestors import CloudianRequestor


class User(object):
    base_url = 'user'

    def __init__(self, requestor):
        self.requestor = requestor
        self.credentials = Credentials(requestor)

    def list(self, data=None, json=None, method='GET'):
        base_url = self.base_url + '/list'
        list_user = CloudianRequestor.request(self.requestor,
                                              url=base_url,
                                              data=data,
                                              json=json,
                                              method=method)

        return list_user

    def get(self, data=None, json=None, method='GET'):
        get_user = CloudianRequestor.request(self.requestor,
                                             url=self.base_url,
                                             data=data,
                                             json=json,
                                             method=method)

        return get_user

    def create(self, data=None, json=None, method='PUT'):
        create_user = CloudianRequestor.request(self.requestor,
                                                url=self.base_url,
                                                data=data,
                                                json=json,
                                                method=method)

        return create_user

    def update(self, data=None, json=None, method='POST'):
        update_user = CloudianRequestor.request(self.requestor,
                                                url=self.base_url,
                                                data=data,
                                                json=json,
                                                method=method)

        return update_user

    def delete(self, data=None, json=None, method='DELETE'):
        delete_user = CloudianRequestor.request(self.requestor,
                                                url=self.base_url,
                                                data=data,
                                                json=json,
                                                method=method)

        return delete_user


class Credentials(object):
    def __init__(self, requestor):
        self.requestor = requestor

    def get(self, data=None, json=None, method='GET'):
        credentials = CloudianRequestor.request(self.requestor,
                                                url=User.base_url + '/credentials',
                                                data=data,
                                                json=json,
                                                method=method)

        return credentials
