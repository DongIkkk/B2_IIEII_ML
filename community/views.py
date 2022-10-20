from django.shortcuts import render, redirect
from community.models import FileUpload, YoloResult
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from yolo_code import detect



# Create your views here.


@login_required
def fileUpload(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'fileupload.html') 
    elif request.method == 'POST':
        title = request.POST.get('title')
        imgfile = request.FILES['file']
        user = request.user

        FileUpload.objects.create(user=user, title=title, imgfile=imgfile)
       
        last_save = FileUpload.objects.last() #가장 마지막에 저장된 파일 정보
        idx = last_save.id
        
        try:
            error = detect.get_img(idx)
            return redirect('community:file_result')
        except:
            delete_file = FileUpload.objects.get(id=idx)
            delete_file.delete()
            return render(request,'error.html')
    



@login_required
def file_result(request):
    files = YoloResult.objects.all().order_by('-id')

    context = {
        'files':files
    }

    return render(request, 'file_result.html', context)




@login_required
def detail_image_info(request, file_id):
    
    file = get_object_or_404(FileUpload, id=file_id)

    context = {
        'file':file
    }

    return render(request, 'detail_image_info.html', context)