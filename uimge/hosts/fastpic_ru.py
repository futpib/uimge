# -*- coding: utf-8 -*-
import base
class Host( base.BaseHost ):
    dev_mode = False

    short_key = 'fp'
    long_key = 'fastpic'
    host='fastpic.ru'
    max_file_size = 5*(1024*1024) #5Mb

    action = 'http://fastpic.ru/upload?api=1'
    form = {
            "method":"file",
            'check_thumb':'no',
            'uploading':'1',
            }
    user_agent = "FPUploader"
    # form = {
    #         'url':'url',
    #         'thumb_text':'',
    #         'check_thumb':'no',
    #         'orig_resize':'640',
    #         'orig_rotate':'0',
    #         'submit':'Загрузить',
    #         'uploading':'1',
    #         }

    def as_file(self, _file):
        return {'file1': _file }
    def postload(self ):
        url = self.findall( r'<thumbpath>http://(i\d).fastpic.ru/thumb/(\d{4}/\d{4,5}/.+?).jpeg</thumbpath>', self.response.body )[0]
        self.img_url = 'http://%s.fastpic.ru/big/%s%s'%(url[0],url[1], self.get_filename( splitext=True)[1] )
        self.img_thumb_url = 'http://%s.fastpic.ru/thumb/%s.jpeg'%url

if __name__ == '__main__':
    h= Host()
    h.test_file()
    h.test_url()
