from fastapi import File,UploadFile
from typing import List

@app.post('/upfile1/')
async def up_f1(request:Request,upload_list:List[UploadFile]=File(...)):
    # 获取文件名称列表
    file_names=[dd.filename for dd in upload_list]

    # 获取文件大小列表
    file_sizes=[len(ds.read())/1024 for ds in [dd.file for dd in upload_list]]

    # 获取文件类型列表
    file_types=[dd.content_type for dd in upload_list]

    # 获取文件对象列表
    filesss = [dd for dd in upload_list]

    # 根据文件个数进行遍历，使用列表索引
    for ss in range(len(file_names)):

        # 指定文件保存路径（使用源文件名称），当前路径下的file目录下
        pth = 'file\\{}'.format(file_names[ss])

        # 读取文件对象内容，阻塞，等待文件上传完成
        fx = await filesss[ss].read()

        # 根据文件路径打开，保存文件
        with open(pth,'wb') as f:
            f.write(fx)

    return templates.TemplateResponse(
        'f.html',
        {
            "request":request,
            "file_names":file_names,
            "file_sizes":file_sizes,
            "file_types":file_types
            })