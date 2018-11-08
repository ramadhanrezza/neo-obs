from obs.libs.s3 import login as login_lib
from obs.libs.utils import log_utils


def list_object(session=None, bucket=None):
    if not session:
        session = login_lib.get_client_session()

    list_object = session.list_objects(Bucket=bucket)
    
    try:
        return list_object.get('Contents')
    except Exception as e:
        log_utils.log_err(e)
        exit()


def get_object(session=None, bucket=None, key=None, gettype=None):
    """
    Get object function include several variable
    session = session from where it called from
    bucket = your bucket name
    key = your object file name
    gettype = your type of object result None|acl|tagging|torrent
    """
    if not session:
        session = login_lib.get_client_session()

    if gettype is None:
        detail_object = session.get_object(Bucket=bucket, Key=key)
    elif gettype == 'acl':
        detail_object = session.get_object_acl(Bucket=bucket, Key=key)
    elif gettype == 'tagging':
        detail_object = session.get_object_tagging(Bucket=bucket, Key=key)
    elif gettype == 'torrent':
        detail_object = session.get_object_torrent(Bucket=bucket, Key=key)

    return detail_object


def put_object(session=None, bucket=None, key=None, acl=None, tagging=None):
    if not session:
        session = login_lib.get_client_session()

    object = None
    if acl is None and tagging is None:
        # put_object
        object = session.put_object(Bucket=bucket, Key=key)
    elif acl is not None and tagging is None:
        # put object acl
        object = session.put_object_acl(Bucket=bucket, Key=key, ACL=acl)
    elif acl is None and tagging is None:
        # put object tagging
        object = session.put_object_tagging(Bucket=bucket, Key=key, Tagging=tagging)
    else:
        # put object acl tagging
        object = session.put_object(Bucket=bucket, Key=key, ACL=acl, Tagging=tagging)

    return object
