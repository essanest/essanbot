
# token_analyzer.py

import random

def analyze_token(token_data):
    """
    تحلیل توکن بر اساس داده‌ها
    :param token_data: dict
    :return: dict - نتایج امتیازدهی و هشدارها
    """

    score = 0
    reasons = []

    # تحلیل قیمت اولیه و حجم
    if token_data.get('price') and token_data.get('price') > 0:
        score += 10
    else:
        reasons.append("قیمت اولیه نامعتبر یا صفر است.")

    if token_data.get('volume_24h') and token_data['volume_24h'] > 100000:
        score += 20
    else:
        reasons.append("حجم معاملات ۲۴ساعته پایین است.")

    # تحلیل نهنگ‌ها و تعداد دارندگان
    if token_data.get('holders') and token_data['holders'] > 200:
        score += 20
    else:
        reasons.append("تعداد دارندگان کم است.")

    if token_data.get('whale_alert'):
        score += 30
    else:
        reasons.append("هنوز تحرک نهنگ‌ها دیده نشده.")

    # تحلیل نقدینگی قفل شده یا ریسک فیک بودن
    if token_data.get('locked_liquidity') and token_data['locked_liquidity']:
        score += 10
    else:
        reasons.append("نقدینگی قفل شده وجود ندارد.")

    # احتمال فیک بودن
    is_fake = False
    if token_data.get('creator_balance', 0) > 0.6:
        is_fake = True
        reasons.append("بیش از ۶۰٪ توکن در اختیار سازنده است.")

    # نمره تصادفی برای تنوع تست (در نسخه واقعی حذف شود)
    score += random.randint(0, 10)

    result = {
        'score': min(score, 100),
        'warnings': reasons,
        'is_fake': is_fake
    }

    return result
