import random
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import Fortune


def fortune(request):
    """
    صفحه اصلی فال حافظ
    """
    all_fortunes = Fortune.objects.all()
    user_fortune = random.choice(all_fortunes) if all_fortunes else None
    context = {'user_fortune': user_fortune}
    return render(request, "fortunes/fortune.html", context)


def random_fortune(request):
    """
    API: برگردوندن فال تصادفی
    هر کاربر هر ۱۵ دقیقه فقط یک فال می‌تونه بگیره
    """
    now = datetime.datetime.now()
    last_request = request.session.get("last_fortune_time")

    if last_request:
        last_request_time = datetime.datetime.fromisoformat(last_request)
        diff = now - last_request_time
        if diff.total_seconds() < 15 * 60:  # ۱۵ دقیقه
            return JsonResponse({
                "error": "⏳ شما هر ۱۵ دقیقه فقط یک فال می‌توانید بگیرید. لطفاً بعداً دوباره امتحان کنید."
            })

    all_fortunes = Fortune.objects.all()
    user_fortune = random.choice(all_fortunes) if all_fortunes else None

    if user_fortune:
        data = {"title": user_fortune.title}
        # ذخیره زمان آخرین فال
        request.session["last_fortune_time"] = now.isoformat()
    else:
        data = {"error": "هیچ فالی موجود نیست."}

    return JsonResponse(data)
