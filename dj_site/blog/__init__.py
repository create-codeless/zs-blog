
from shortuuid import ShortUUID
from random import choice
default_app_config = 'blog.apps.DbConfig'


class NewUUID(ShortUUID):
    """
    固定长度为12, 使用时instance.random
    """

    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        super().__init__(alphabet)

    @property
    def _length(self):
        return 12

