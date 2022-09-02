from bot.helper.ext_utils.bot_utils import MirrorStatus, get_readable_file_size, get_readable_time


class MegaDownloadStatus:
    def __init__(self, obj, listener):
        self.__obj = obj
        self.__uid = listener.uid
        self.message = listener.message
        self.__engine = "megasdkrestclient"
        self.__mode = self.__listener.mode

    def gid(self):
        return self.__obj.gid

    def processed_bytes(self):
        return self.__obj.downloaded_bytes

    def size_raw(self):
        return self.__obj.size

    def size(self):
        return get_readable_file_size(self.size_raw())

    def status(self):
        return MirrorStatus.STATUS_DOWNLOADING

    def name(self):
        return self.__obj.name

    def progress_raw(self):
        return self.__obj.progress

    def progress(self):
        return f'{round(self.progress_raw(), 2)}%'

    def speed_raw(self):
        """
        :return: Download speed in Bytes/Seconds
        """
        return self.__obj.download_speed

    def speed(self):
        return f'{get_readable_file_size(self.speed_raw())}/s'

    def eta(self):
        try:
            seconds = (self.size_raw() - self.processed_bytes()) / self.speed_raw()
            return f'{get_readable_time(seconds)}'
        except:
            return '-'

    def download(self):
        return self.__obj

    def engine(self):
        return self.__engine

    def source(self):
        reply_to = self.message.reply_to_message
        return reply_to.from_user.username or reply_to.from_user.id if reply_to and \
            not reply_to.from_user.is_bot else self.message.from_user.username \
                or self.message.from_user.id

    def mode(self):
        return self.__mode