import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import BetaSignup


def index(request):
    return render(request, 'core/index.html')

def problem(request):
    return render(request, 'core/problem.html')

def solution(request):
    return render(request, 'core/solution.html')

def features(request):
    return render(request, 'core/features.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def faq(request):
    return render(request, 'core/faq.html')

def beta(request):
    return render(request, 'core/beta.html')


@csrf_exempt
@require_POST
def beta_signup(request):
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        business_name = data.get('business_name', '').strip()
        contact = data.get('contact', '').strip()
        business_type = data.get('business_type', '').strip()
        message = data.get('message', '').strip()

        if not name or not business_name or not contact or not business_type:
            return JsonResponse({'status': 'error', 'message': 'გთხოვთ შეავსოთ ყველა სავალდებულო ველი.'}, status=400)

        BetaSignup.objects.create(
            name=name, business_name=business_name,
            contact=contact, business_type=business_type, message=message,
        )

        # Send email notification
        subject = f"ახალი Beta რეგისტრაცია | Tasky AI — {business_name}"
        body = f"ახალი ბიზნესი დარეგისტრირდა Beta პროგრამაში!\n\nსახელი: {name}\nბიზნესის სახელი: {business_name}\nსაკონტაქტო: {contact}\nბიზნესის ტიპი: {business_type}\nშეტყობინება: {message}"
        
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <style>
            body {{ margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
            .email-bg {{ background-color: #06080f; padding: 40px 20px; width: 100%; box-sizing: border-box; }}
            .wrapper {{ max-width: 580px; margin: 0 auto; }}
            .logo {{ text-align: center; margin-bottom: 30px; font-size: 24px; font-weight: 800; letter-spacing: -0.5px; color: #ffffff; }}
            .logo span.blue {{ color: #3b82f6; }}
            .logo span.cyan {{ color: #06b6d4; }}
            .card {{ background-color: #12172b; border: 1px solid #1e2a4a; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
            .card-header {{ padding: 30px 30px 0; }}
            .badge {{ display: inline-block; background-color: rgba(59,130,246,0.15); color: #3b82f6; border: 1px solid rgba(59,130,246,0.3); padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; }}
            h2 {{ margin: 0; font-size: 22px; font-weight: 700; color: #ffffff; line-height: 1.3; }}
            .intro {{ color: #8b9cc0; font-size: 15px; margin-top: 8px; line-height: 1.5; }}
            .card-body {{ padding: 30px; }}
            .data-group {{ margin-bottom: 24px; }}
            .data-group:last-child {{ margin-bottom: 0; }}
            .data-label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #556388; font-weight: 600; margin-bottom: 6px; }}
            .data-value {{ font-size: 16px; color: #edf2f7; font-weight: 500; background-color: #0c1020; border: 1px solid #1e2a4a; padding: 14px 16px; border-radius: 10px; }}
            .data-value a {{ color: #06b6d4; text-decoration: none; }}
            .data-value a:hover {{ text-decoration: underline; }}
            .msg-value {{ line-height: 1.6; white-space: pre-wrap; }}
            .empty-msg {{ color: #556388; font-style: italic; }}
            .footer {{ text-align: center; margin-top: 30px; color: #556388; font-size: 13px; line-height: 1.5; }}
            .footer a {{ color: #8b9cc0; text-decoration: none; border-bottom: 1px solid #1e2a4a; }}
          </style>
        </head>
        <body>
          <div class="email-bg">
            <div class="wrapper">
              <div class="logo">
                <span style="display:inline-block; margin-right:8px; padding:2px 8px; background:linear-gradient(135deg, #3b82f6, #06b6d4); color:#fff; border-radius:6px; font-size:20px;">T</span>
                Tasky<span class="blue">A</span><span class="cyan">I</span>
              </div>
              
              <div class="card">
                <div class="card-header">
                  <div class="badge">ახალი მოთხოვნა</div>
                  <h2>Beta პროგრამის რეგისტრაცია</h2>
                  <div class="intro">პლატფორმაზე დაფიქსირდა ახალი ბიზნესის მონაცემები.</div>
                </div>
                
                <div class="card-body">
                  <div class="data-group">
                    <div class="data-label">ბიზნესის სახელი</div>
                    <div class="data-value">{business_name}</div>
                  </div>
                  
                  <div class="data-group">
                    <div class="data-label">საკონტაქტო პირი</div>
                    <div class="data-value">{name}</div>
                  </div>
                  
                  <div class="data-group">
                    <div class="data-label">საკონტაქტო ინფორმაცია</div>
                    <div class="data-value"><a href="mailto:{contact}">{contact}</a></div>
                  </div>
                  
                  <div class="data-group">
                    <div class="data-label">ბიზნესის ტიპი</div>
                    <div class="data-value">{business_type}</div>
                  </div>
                  
                  <div class="data-group">
                    <div class="data-label">შეტყობინება</div>
                    <div class="data-value msg-value">{message if message else '<span class="empty-msg">არ არის მითითებული</span>'}</div>
                  </div>
                </div>
              </div>
              
              <div class="footer">
                Tasky AI — ციფრული თანამშრომელი შენი ბიზნესისთვის<br>
                ეს შეტყობინება გენერირებულია ავტომატურად.
              </div>
            </div>
          </div>
        </body>
        </html>
        """
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
                html_message=html_message
            )
        except Exception as e:
            print(f"Failed to send email: {e}")

        return JsonResponse({'status': 'success', 'message': 'მადლობა! მოთხოვნა მიღებულია.'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'არასწორი მონაცემები.'}, status=400)
    except Exception:
        return JsonResponse({'status': 'error', 'message': 'სერვერის შეცდომა. სცადეთ მოგვიანებით.'}, status=500)
