from mongrel2.config import *


main = Server(
    uuid="f400bf85-4538-4f7a-8908-67e313d515c2",
    access_log="/logs/access.log",
    error_log="/logs/error.log",
    chroot="./",
    default_host="localhost",
    name="test",
    pid_file="/run/mongrel2.pid",
    port=6767,
    hosts = [
        Host(name="localhost", routes={
            r'/dev/null/(.*)': Dir(base='tests/', index_file='index.html',
                             default_ctype='text/plain')
        })
    ]
)

sub = Server(
    uuid="e3ce7982-086f-4374-adde-bee320d509e6",
    access_log="/logs/access.log",
    error_log="/logs/error.log",
    chroot="./",
    default_host="sub",
    name="sub",
    pid_file="/run/mongrel2.pid",
    port=6767,
    hosts = [
        Host(name="sub", routes={
            r'/dev/null/(.*)': Dir(base='tests/', index_file='index.html',
                             default_ctype='text/plain')
        })
    ]
)

foo = Server(
    uuid="2355e656-fac6-41c8-9cba-4977b937cb94",
    access_log="/logs/access.log",
    error_log="/logs/error.log",
    chroot="./",
    default_host="foo",
    name="sub",
    pid_file="/run/mongrel2.pid",
    port=6767,
    hosts = [
        Host(name="foo", routes={
            r'/dev/null/(.*)': Dir(base='tests/', index_file='index.html',
                             default_ctype='text/plain')
        })
    ]
)

commit([main, foo, sub])


