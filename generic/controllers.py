from django.views.generic.base import View


class PageNumberView(View):
    def post(self, requset, *args, **kwargs):
        try:
            pn = requset.GET['page']
        except KeyError:
            pn = '1'

        self.success_url = self.success_url + '?page=' + pn

        return super(PageNumberView, self).post(requset, *args, **kwargs)
