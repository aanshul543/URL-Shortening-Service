from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import generics, status
from .models import Url
from .serializers import UrlSerializer

def Base62Conversion(id):
    alphaNum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = 62
    converted = ""
    while id > 0:
        converted += alphaNum[id % base]
        id //= base
    if len(converted) == 0:
        return "0"
    return converted[::-1]

def GetURL(url):
    baseUrl = "http://127.0.0.1:8000/"
    return baseUrl + url

class CreateView(generics.CreateAPIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        longurl = request.data["long"]
        if longurl:
            existing = Url.objects.filter(long=longurl).first()
            if existing:
                return JsonResponse({"Success": GetURL(existing.short)}, status=status.HTTP_200_OK)
            else:
                cnt = Url.objects.count()
                print(cnt)
                if cnt != 0:
                    id = Url.objects.latest('id').id
                    id += 1
                else:
                    id = 1
                shorturl = Base62Conversion(id)
                request.data.update({"long": longurl, "short": shorturl})
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                if not serializer.is_valid(raise_exception=False):
                    return JsonResponse({"Fail": "Data not valid."}, status=status.HTTP_400_BAD_REQUEST)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return JsonResponse({"Success": GetURL(shorturl)}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return JsonResponse({"Fail": "Data not valid."}, status=status.HTTP_400_BAD_REQUEST)

def RedirectURL(request, shorturl):
    short = shorturl.title()
    obj = Url.objects.filter(short=short).first()
    if obj:
        return HttpResponseRedirect(redirect_to=obj.long)
    else:
        return JsonResponse({"message": "Bad Request"})