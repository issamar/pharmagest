
from django.shortcuts import redirect
from django.contrib.auth.models import User
from datetime import datetime, timezone
from mainpage.models import UserPayementStat

def Time_to_pay(view_func):
    def wrapper_func(request, *args, **kwargs):
        userrname = request.user
        get_userrname_id = User.objects.filter(username = userrname).values_list('pk', flat=True)
        get_userrname = User.objects.get(pk=get_userrname_id[0])
        signup_date = get_userrname.date_joined
        date_now = datetime.now(timezone.utc)
        user_proof = list(UserPayementStat.objects.values_list('user_name', flat=True))
        day_in_site = (date_now.day - signup_date.day)
        print(day_in_site, flush=True)
        if day_in_site > 1:
            if str(userrname) in user_proof:

                img_proof = UserPayementStat.objects.get(user_name = userrname)
                if img_proof is None:
                    return redirect('user_proof')
                else:
                    return view_func(request, *args, **kwargs)
            else:
                return redirect('user_proof')
        if day_in_site <=1:
            return view_func(request, *args, **kwargs)
    return wrapper_func