
Fork of original mockldap project, which is unmaintained (see below).
This fork contains modifications to improve compatibility with python-ldap
on Python 3. In this case, python-ldap stores all attribute values as
"bytes" and mockldap has been modified to do so too. Without these changes
it is tricky to put code written for python-ldap under unit test using
mockldap.

Besides these modifications, this project is unlikely to receive further
development.


Status
------

**This project is unmaintained**. It was originally spun off of
django-auth-ldap, which no longer requires it. If you have a use for it, feel
free to copy the code for your own purposes (it's only for testing, after all).

Documentation may still be available at https://mockldap.readthedocs.io/.
