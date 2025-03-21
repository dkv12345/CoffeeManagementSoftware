import json
import os
class JsonFileFactory:
    def write_data(self,arr_data,filename):
        """
        Hàm này dùng để parse object thành jsonstring
        :param arr_data: mảng đối tượng
        :param filename:nơi lưu trữ jsonstring cho object
        :return: True nếu thành công
        """
        json_string=json.dumps([item.__dict__ for item in arr_data],
                               default=str,indent=4,ensure_ascii=False)
        json_file=open(filename,'w',encoding='utf-8')
        json_file.write(json_string)
        json_file.close()
    def read_data(self,filename,ClassName):
        """
        Hàm đọc jsonstring và phục hồi lại mô hình lớp ClassName
        với ClassName là tên lớp được chỉ định phục hồi OOP
        :param filename:
        :param ClassName:
        :return:
        """
        if os.path.isfile(filename)==False:
            return []
        file=open(filename,'r',encoding='utf-8')
        arr_data=json.loads(file.read(),object_hook=lambda cls:ClassName(**cls))
        file.close()
        return arr_data