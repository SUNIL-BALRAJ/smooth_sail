from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
import os
import time
import pickle
import matplotlib.pyplot as plt
import io
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
import json
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from keras.models import load_model
from .models import AnalysisResult
from .models import TelegramAnalysis
from ultralytics import YOLO
from IPython import display
display.clear_output()
import ultralytics
from transformers import BertTokenizer
flagged_keywords = ["baby Dogecoin", "doge meme token", "ran up", "Shiba Inu", "ranked 176", "mid cap", "Doge will go to one dollar", "next Bull Run", "chance to run at least like 10x", "older tokens", "crypto gaming tokens", "50 2000 acts in the next Bull Run", "earning passive rewards", "web 3 gaming node owner", "earning 25 every day without doing anything", "opportunity is huge", "baby doll Shogun", "20x is doable", "risk reward", "buying crypto gaming tokens", "crypto will not be broken", "bypassed", "ground shattering", "digital currency", "profitable", "Bitcoin Sheba and ethereum", "truer words", "highly profitable", "Sensational cryptocurrencies", "millionaire", "huge fluctuations", "volatile", "evolving constantly", "opportunities and drawbacks", "positive and negative aspects", "trend in the broader cryptocurrency Market", "positive developments", "promising year", "pessimistic scenario", "top five mobile cryptocurrency earning apps for ios", "make money with NFTs", "buy for $20 and then sell a week later for like $2000", "minted or got the NFT for $250, and eleven days later, he sold it for $1200", "huge profit", "quick profit", "blow up to become highly profitable", "minting an NFT and selling it right away", "whitelisted people can mint an NFT", "public minting period", "Tron Wars", "Awesome Apes", "normal people", "influencer NFTs", "Logan Paul", "Paris Hilton", "Gary Vee", "Avenged Sevenfold", "experience", "goals", "reputation", "good or bad reputation", "student who sold his selfies as NFTs", "time-lapse college projects", "trustworthy founders", "investing in the right NFT project", "believe in", "long term investments", "make a big profit", "investing in things that I believe in", "analyze NFT projects", "invest in the right NFT project", "guaranteed profits", "surefire method", "foolproof strategy", "never fail", "100% success rate", "risk-free", "unlimited gains", "secret formula", "exclusive insider information", "market manipulation", "manipulate prices", "insider tips", "unbeatable strategy", "confidential details", "hidden patterns", "never-before-seen method", "automatic profits", "set it and forget it", "magic software", "algorithmic trading", "profit-pulling machine", "money-making software", "autopilot earnings", "secret trading technique", "surefire signals", "never lose", "no-risk strategy", "exclusive formula", "guaranteed success", "foolproof method", "hidden strategies", "profit of 345", "easily get 200", "good special profit", "bonus of $100", "Protective Prot", "IC is a protector", "50% deposit bonus", "magic software", "automatic profits", "unlimited gains", "exclusive insider information", "manipulate prices", "insider tips", "unbeatable strategy", "hidden patterns", "set it and forget it", "money-making software", "autopilot earnings", "surefire signals", "no-risk strategy", "exclusive formula", "guaranteed success", "foolproof method", "hidden strategies", "profit of 13 $9", "join the Telegram channel for this setting", "very good profit", "profit is made here", "unique strategy", "live proof", "95% results", "follow the strategy", "follow on Instagram", "expert option", "create an account", "promo code", "50% opposite bonus", "make $200", "bonus of $1", "get $300", "link in the description", "subscribe to the channel", "follow on Instagram", "exclusive insights", "secret technique", "hidden knowledge", "guaranteed profits", "insider advantage", "proprietary formula", "exclusive access", "guaranteed crypto profits", "instant crypto gains", "exclusive crypto strategy", "secret crypto method", "quick crypto riches", "massive crypto returns", "surefire crypto investment", "insider crypto tips", "risk-free crypto trading", "sky-high crypto growth", "overnight crypto success", "hidden crypto opportunity", "next big crypto winner", "explosive crypto growth", "unbeatable crypto results", "never-fail crypto system", "100% crypto success rate", "proven crypto formula", "zero-risk crypto profit", "foolproof crypto plan", "limited-time crypto offer", "can't lose crypto trade", "guaranteed crypto success", "game-changing crypto strategy", "crypto millionaire maker", "unlock the crypto secret", "rare crypto opportunity", "guaranteed crypto breakthrough", "predict crypto market trends", "exclusive crypto insights", "revolutionary crypto method", "predict the future of crypto", "unlimited crypto potential", "bulletproof crypto strategy", "guaranteed crypto riches", "top-secret crypto technique", "golden ticket crypto investment", "guaranteed crypto victory", "future-proof crypto gains", "ultimate crypto profit formula", "exclusive crypto trading secrets", "guaranteed crypto performance", "instant crypto success", "exclusive crypto profit opportunity", "hidden crypto advantage", "crypto profit explosion", "risk-free crypto gains", "unstoppable crypto growth", "massive crypto profits", "time-tested crypto strategy", "crypto insider knowledge", "foolproof crypto approach", "proven crypto success", "zero-loss crypto formula", "can't-miss crypto opportunity", "guaranteed crypto results", "revolutionize your crypto finances", "never-fail crypto approach", "exponential crypto gains", "undiscovered crypto gem", "guaranteed crypto returns", "secret crypto formula", "exclusive crypto profit formula", "foolproof crypto method", "unbeatable crypto gains", "life-changing crypto opportunity", "limited-time crypto deal", "can't-fail crypto strategy", "guaranteed crypto wealth", "game-changing crypto solution", "next big crypto breakout", "unprecedented crypto growth", "predictive crypto power", "exclusive crypto secret", "guaranteed crypto breakthrough", "unlimited crypto success", "golden crypto opportunity", "guaranteed crypto prosperity", "future-proof crypto strategy", "instant crypto profits", "exclusive crypto formula", "proven crypto techniques", "risk-free crypto profits", "massive crypto success", "hidden crypto secrets", "ultimate crypto profit potential", "fail-proof crypto method", "unstoppable crypto returns", "crypto insider methods", "guaranteed crypto advantage", "exclusive crypto insights", "exponential crypto growth", "zero-risk crypto gains", "unbeatable crypto success", "life-changing crypto results", "never-before-revealed crypto strategy", "revolutionary crypto approach", "predict crypto market movements", "undiscovered crypto opportunity", "guaranteed crypto strategy", "future-proof crypto profit", "top-secret crypto method", "guaranteed crypto victory", "game-changing crypto method", "surefire crypto profit", "exclusive crypto profit secrets", "hidden crypto potential", "risk-free crypto strategy", "unstoppable crypto profit", "massive crypto returns", "time-tested crypto techniques", "crypto insider secrets", "foolproof crypto solution", "proven crypto approaches", "zero-loss crypto strategy", "can't-miss crypto chance", "guaranteed crypto returns", "revolutionize your crypto success", "never-fail crypto solution", "exponential crypto profits", "undiscovered crypto treasure", "guaranteed crypto breakthrough", "guaranteed returns", "instant profits", "secret method", "exclusive offer", "quick gains", "massive returns", "surefire strategy", "insider tips", "risk-free investment", "sky-high growth", "overnight success", "hidden opportunity", "next big winner", "explosive growth", "unbeatable results", "never-fail system", "100% success rate", "proven formula", "zero-risk profit", "foolproof plan", "life-changing earnings", "limited-time offer", "can't lose", "guaranteed success", "game-changing strategy", "millionaire maker", "unlock the secret", "rare opportunity", "guaranteed breakthrough", "predict the future", "exclusive access", "never-before-seen", "revolutionary method", "predict market trends", "unlimited potential", "bulletproof strategy", "guaranteed riches", "top-secret technique", "golden ticket", "guaranteed victory", "future-proof investment", "zero effort, maximum gains", "ultimate profit formula", "exclusive insights", "guaranteed wealth", "fail-proof system", "next big thing", "surefire winner", "insider trading secrets", "guaranteed performance", "instant success", "exclusive profit method", "hidden advantage", "profit explosion", "risk-free gains", "unstoppable growth", "massive profits", "time-tested strategy", "insider knowledge", "foolproof approach", "proven success", "zero-loss formula", "can't-miss opportunity", "guaranteed results", "revolutionize your finances", "never-fail approach", "exponential gains", "undiscovered gem", "guaranteed returns", "secret formula", "exclusive profit opportunity", "foolproof method", "unbeatable gains", "life-changing opportunity", "limited-time deal", "can't-fail strategy", "guaranteed wealth", "game-changing solution", "next big breakout", "unprecedented growth", "predictive power", "exclusive secret", "guaranteed breakthrough", "unlimited success", "golden opportunity", "guaranteed prosperity", "future-proof strategy", "instant profits", "exclusive formula", "proven techniques", "risk-free profits", "massive success", "hidden secrets", "ultimate profit potential", "fail-proof method", "unstoppable returns", "insider methods", "guaranteed advantage", "exclusive insights", "exponential growth", "zero-risk gains", "unbeatable success", "life-changing results", "never-before-revealed strategy", "revolutionary approach", "predict market movements", "undiscovered opportunity", "guaranteed strategy", "future-proof profit", "top-secret method", "guaranteed victory", "game-changing method", "surefire profit", "exclusive profit secrets", "hidden potential", "risk-free strategy", "unstoppable profit", "massive returns", "time-tested techniques", "insider secrets", "foolproof solution", "proven approaches", "zero-loss strategy", "can't-miss chance", "guaranteed returns", "revolutionize your success", "never-fail solution", "exponential profits", "undiscovered treasure", "guaranteed breakthrough", "next Dogecoin", "guaranteed meme coin gains", "instant meme coin profits", "exclusive meme coin strategy", "secret meme coin method", "quick meme coin riches", "massive meme coin returns", "surefire meme coin investment", "insider meme coin tips", "sky-high meme coin growth", "overnight meme coin success", "hidden meme coin opportunity", "next big meme coin winner", "explosive meme coin growth", "unbeatable meme coin results", "never-fail meme coin system", "100% meme coin success rate", "proven meme coin formula", "zero-risk meme coin profit", "foolproof meme coin plan", "limited-time meme coin offer", "can't lose meme coin trade", "guaranteed meme coin success", "game-changing meme coin strategy", "meme coin millionaire maker", "unlock the meme coin secret", "rare meme coin opportunity", "guaranteed meme coin breakthrough", "predict meme coin trends", "exclusive meme coin insights", "revolutionary meme coin method", "predict the future of meme coins", "unlimited meme coin potential", "bulletproof meme coin strategy", "guaranteed meme coin riches", "top-secret meme coin technique", "golden ticket meme coin investment", "guaranteed meme coin victory", "future-proof meme coin gains", "ultimate meme coin profit formula", "exclusive meme coin trading secrets", "guaranteed meme coin performance", "instant meme coin success", "exclusive meme coin profit opportunity", "hidden meme coin advantage", "meme coin profit explosion", "risk-free meme coin gains", "unstoppable meme coin growth", "massive meme coin profits", "time-tested meme coin strategy", "meme coin insider knowledge", "foolproof meme coin approach", "proven meme coin success", "zero-loss meme coin formula", "can't-miss meme coin opportunity", "guaranteed meme coin results", "revolutionize your meme coin finances", "never-fail meme coin approach", "exponential meme coin gains", "undiscovered meme coin gem", "guaranteed meme coin returns", "secret meme coin formula", "exclusive meme coin profit formula", "foolproof meme coin method", "unbeatable meme coin gains", "life-changing meme coin opportunity", "limited-time meme coin deal", "can't-fail meme coin strategy", "guaranteed meme coin wealth", "game-changing meme coin solution", "next big meme coin breakout", "unprecedented meme coin growth", "predictive meme coin power", "exclusive meme coin secret", "guaranteed meme coin breakthrough", "unlimited meme coin success", "golden meme coin opportunity", "guaranteed meme coin prosperity", "future-proof meme coin strategy", "instant meme coin profits", "exclusive meme coin formula", "proven meme coin techniques", "risk-free meme coin profits", "massive meme coin success", "hidden meme coin secrets", "ultimate meme coin profit potential", "fail-proof meme coin method", "unstoppable meme coin returns", "meme coin insider methods", "guaranteed meme coin advantage", "exclusive meme coin insights", "exponential meme coin growth", "zero-risk meme coin gains", "unbeatable meme coin success", "life-changing meme coin results", "never-before-revealed meme coin strategy", "revolutionary meme coin approach", "predict meme coin market movements", "undiscovered meme coin opportunity", "guaranteed meme coin strategy", "future-proof meme coin profit", "top-secret meme coin method", "guaranteed meme coin victory", "game-changing meme coin method", "surefire meme coin profit", "exclusive meme coin profit secrets", "hidden meme coin potential", "risk-free meme coin strategy", "unstoppable meme coin profit", "massive meme coin returns", "time-tested meme coin techniques", "meme coin insider secrets", "foolproof meme coin solution", "proven meme coin approaches", "zero-loss meme coin strategy", "can't-miss meme coin chance", "guaranteed meme coin returns", "revolutionize your meme coin success", "never-fail meme coin solution", "exponential meme coin profits", "undiscovered meme coin treasure", "guaranteed meme coin breakthrough"]
sebi_registered_apps = ["Zerodha Broking Limited", "Angel Broking Limited", "5PAISA Capital Limited", "ICICI Securities Limited", "Motilal Oswal Financial Services Limited", "Sharekhan Limited", "Kotak Securities Limited", "HDFC Securities Limited", "IIFL Securities Limited", "Edelweiss Broking Limited", "Axis Securities Limited", "Tradebulls Securities (P) Limited", "Dhani Stocks Limited", "SMC Global Securities Limited", "Religare Broking Limited", "IDBI Capital Markets & Securities Limited", "Reliance Securities Limited", "SBICAP Securities Limited", "Karvy Stock Broking Limited", "Anugrah Stock & Broking Private Limited", "Indianivesh Shares and Securities Private Limited", "RKSV Securities India Private Limited", "Arcadia Share & Stock Brokers Private Limited", "Alice Blue Financial Services Limited", "Fyers Securities Private Limited", "Action Financial Services (India) Limited", "Modex International Securities Limited", "Aditya Birla Money Limited", "Samco Securities Limited", "Geojit Financial Services Limited", "Astha Credit & Securities (P) Limited", "Profitmart Securities Private Limited", "Conard Securities Private Limited", "Sumpoorna Portfolio Limited", "Vikson Securities Private Limited", "Nirmal Bang Securities Private Limited", "Ventura Securities Limited", "Anand Rathi Share and Stock Brokers Limited", "BMA Wealth Creators Limited", "Finvasia Securities Private Limited", "Dealmoney Securities Private Limited", "Globe Capital Market Limited", "SMIFS Limited", "Swastika Investmart Limited", "Goodwill Wealth Management Private Limited", "YES Securities (India) Limited", "Nextbillion Technology Private Limited", "Navia Markets Limited", "Choice Equity Broking Private Limited", "Yuvraj Securities", "SHCIL Services Limited", "Zerodha Securities Private Limited", "Integrated Enterprises (India) Private Limited", "Astitva Capital Market Private Limited", "Monarch Networth Capital Limited", "Shri Parasram Holdings Private Limited", "Quantum Global Securities Limited", "Master Capital Services Limited", "Reflection Investments", "LKP Securities Limited", "Prabhudas Lilladher Private Limited", "VNS Finance & Capital Services Limited", "Shriram Insight Share Brokers Limited", "Bonanza Portfolio Limited", "Motilal Oswal Capital Markets Private Limited", "JM Financial Services Limited", "Karmic Stock Broking Private Limited", "Zebu Share and Wealth Managements Private Limited", "Alankit Imaginations Limited", "Stock Holding Corporation of India Limited", "Prudent Broking Services Private Limited", "South Asian Stocks Limited", "Maxgrowth Capital Private Limited", "Ashlar Securities Private Limited", "Acumen Capital Market (India) Limited", "NJ Invest India Private Limited", "HEM Finlease Private Limited", "BOB Capital Markets Limited", "Arihant Capital Markets Limited", "Abhipra Capital Limited", "Fairwealth Securities Limited", "Mehta Equities Limited", "LFS Broking Private Limited", "Century Finvest Private Limited", "ISS Enterprise Limited", "Marwadi Shares and Finance Limited", "Elite Wealth Advisors Limited", "Raghunandan Capital Private Limited", "Escorts Securities Limited", "Comfort Securities Limited", "Paytm Money Limited", "Mandot Securities Private Limited", "IFCI Financial Services Limited", "ICICI Web Trade Limited", "Nine Star Broking Private Limited", "Latin Manharlal Securities Private Limited", "Wealth India Financial Services Limited", "Lohia Securities Limited", "Adwealth Stock Broking Private Limited", "Mansukh Securities and Finance Limited", "Aum Capital Market Private Limited", "Anush Shares and Securities Private Limited", "Pune E Stock Broking Private Limited", "Badjate Stock and Shares Private Limited", "KR Choksey Shares and Securities Private Limited", "Findoc Investmart Private Limited", "Karuna Financial Services Private Limited", "Zuari Finserv Limited", "GCL Securities Private Limited", "Sunlight Broking LLP", "CD Equisearch Private Limited", "Aasma Securities Private Limited", "Kotak Mahindra Bank Limited", "Wealthstreet Advisors Private Limited", "Kedia Shares and Stocks Brokers Limited", "NKB Securities", "Ambalal Shares and Stocks Private Limited", "Signature Global Securities Private Limited", "Prognosis Securities Private Limited", "Garg Securities Private Limited", "CIL Securities Limited", "Coimbatore Capital Limited", "Aditya Ajay Share Brokers Private Limited", "OJ Financial Services Limited", "DP Tradeking Private Limited", "Dynamic Equities Private Limited", "Farsight Securities Limited", "ISF Securities Limited", "R Wadiwala Securities Private Limited", "Enrich Financial Solution Private Limited", "Multiplex Capital Limited", "Progressive Share Brokers Private Limited", "Shilpa Stock Broker Private Limited", "Nirmal Bang Equities Private Limited", "Fair Intermediate Investments Private Limited", "AS Stock Broking and Management Private Limited", "Patel Wealth Advisors Private Limited", "Stampede Capital Limited", "Pravin Ratilal Share and Stock Brokers Limited", "Crown Consultants Private Limited", "Abhira Securities Limited", "Mittal Securities Private Limited", "Jhaveri Securities Limited", "Sara Securities Private Limited", "Jyoti Portfolio Private Limited", "Rudra Shares and Stock Brokers Limited", "KK Securities Limited", "BN Rathi Securities Limited", "Khandwala Securities Limited", "Rajsons Securities Limited"]
sebi_alert_apps=[]
# Initialize the tokenizer once
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
import requests
from .sms import send_sms
from sklearn.ensemble import RandomForestClassifier
import joblib



def index(request):
  context = {
    'segment': 'index'
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/tables.html", context)

# Components
@login_required(login_url='/accounts/login/')
def bc_button(request):
  context = {
    'parent': 'basic_components',
    'segment': 'button'
  }
  return render(request, "pages/components/bc_button.html", context)

@login_required(login_url='/accounts/login/')
def bc_badges(request):
  context = {
    'parent': 'basic_components',
    'segment': 'badges'
  }
  return render(request, "pages/components/bc_badges.html", context)

@login_required(login_url='/accounts/login/')
def bc_breadcrumb_pagination(request):
  context = {
    'parent': 'basic_components',
    'segment': 'breadcrumbs_&_pagination'
  }
  return render(request, "pages/components/bc_breadcrumb-pagination.html", context)

@login_required(login_url='/accounts/login/')
def bc_collapse(request):
  context = {
    'parent': 'basic_components',
    'segment': 'collapse'
  }
  return render(request, "pages/components/bc_collapse.html", context)

@login_required(login_url='/accounts/login/')
def bc_tabs(request):
  context = {
    'parent': 'basic_components',
    'segment': 'navs_&_tabs'
  }
  return render(request, "pages/components/bc_tabs.html", context)

@login_required(login_url='/accounts/login/')
def bc_typography(request):
  context = {
    'parent': 'basic_components',
    'segment': 'typography'
  }
  return render(request, "pages/components/bc_typography.html", context)

@login_required(login_url='/accounts/login/')
def icon_feather(request):
  context = {
    'parent': 'basic_components',
    'segment': 'feather_icon'
  }
  return render(request, "pages/components/icon-feather.html", context)


# Forms and Tables
@login_required(login_url='/accounts/login/')
def form_elements(request):
  context = {
    'parent': 'form_components',
    'segment': 'form_elements'
  }
  return render(request, 'pages/form_elements.html', context)

@login_required(login_url='/accounts/login/')
def basic_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'basic_tables'
  }
  return render(request, 'pages/tbl_bootstrap.html', context)

# Chart and Maps
@login_required(login_url='/accounts/login/')
def morris_chart(request):
  context = {
    'parent': 'chart',
    'segment': 'morris_chart'
  }
  return render(request, 'pages/chart-morris.html', context)

@login_required(login_url='/accounts/login/')
def google_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'google_maps'
  }
  return render(request, 'pages/map-google.html', context)

# Authentication
class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

@login_required(login_url='/accounts/login/')
def sample_page1(request):
  context = {
    'segment': 'segement_page1',
  }
  return render(request, 'pages/segment_page1.html', context)

@login_required(login_url='/accounts/login/')
def sample_page2(request):
  context = {
    'segment': 'segment_page2',
  }
  return render(request, 'pages/segment_page2.html', context)

@login_required(login_url='/accounts/login/')
def horizontal(request):
  context = {
    'segment': 'horizontal',
  }
  return render(request, 'pages/horizontal.html', context)

@login_required(login_url='/accounts/login/')
def failure(request):
  context = {
    'segment': 'failure',
  }
  return render(request, 'pages/failure.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    misleading_results = AnalysisResult.objects.filter(conclusion='misleading')
    return render(request, 'pages/profile.html', {'misleading_results': misleading_results})

@login_required(login_url='/accounts/login/')
def misleading_telegram(request):
    misleading_results = TelegramAnalysis.objects.filter(conclusion='Potentially Misleading')
    return render(request, 'pages/misleading_telegram.html', {'misleading_results': misleading_results})

@login_required(login_url='/accounts/login/')
def telegram(request):
    import math
    last_uploaded_text = None
    if request.method == 'POST':
      
      while True:
        print("running")
        base_url = 'https://api.thingspeak.com/channels/2375718/feeds.json?api_key=ATHYX1B78TCPT7W6&results=2'
        params = {'results': 1}
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json() 

        # Extract the 'feeds' values
        input = data.get('feeds', [])

        # Extract the desired values into a list
        if input:
            feed_values = [
                input[0]['entry_id'],
                float(input[0]['field1'].strip()) if input[0]['field1'].strip() != 'NaN' else 0.0,
                float(input[0]['field2']) if input[0]['field2'].strip() != 'NaN' else 0.0,
                int(input[0]['field3']) if input[0]['field3'].strip() != 'NaN' else 0,
                int(input[0]['field4']) if input[0]['field4'].strip() != 'NaN' else 0,
                int(input[0]['field5']) if input[0]['field5'].strip() != 'NaN' else 0,
                int(input[0]['field6']) if input[0]['field6'].strip() != 'NaN' else 0
                
            ]

            print(feed_values)
        
        else:
            print("No 'feeds' data found.")
        inp=feed_values[0:3]
        inputrf=[]
        inputrf.append(inp)
        model = joblib.load(r'home\my_random_forest.joblib')
        a = model.predict(inputrf)
        print(f'Prediction is {a}')

        import pickle
        if feed_values[3]>10:
          alert="Alert"
          reason="High Vibrations"
        elif feed_values[2]>30:
          alert="Alert"
          reason="High Temperature"
        elif feed_values[2]<10:
          alert="Alert"
          reason="Low Temperature" 
        if feed_values[3]>10 or feed_values[2]>30 or feed_values[2]<10: 
          send_sms()
          import openai
          # Set your OpenAI GPT-3 API key
          api_key = "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"
          # Generate explanation using GPT-3 API
          prompt="parameter abnormal :"+reason + "/n" + "The main motive is to predict dislodgement of cable belt conveyer by sensing and analysing parameters like temperature, vibration, moisture, accelerometer and give some suggestions or preventive, corrective measures. I have given the parameter which is abnormal based on our sensor data. please give me suggestion or preventive corrective measure for futher steps. for eg if we sense that the vibration is very high the reason would maybe because of high load at that point, decrease in tension, dislocation of pulleys etc. so you can suggest corrective measures."  
          openai.api_key = api_key
          response = openai.Completion.create(
              engine="text-davinci-003",
              prompt=prompt,
              max_tokens=250,
              stop=None,
              temperature=0.7
          )
          
          measure = response.choices[0].text.strip()
          print(measure)
          break
        time.sleep(5)
      

      analysis_result = TelegramAnalysis(
            alert_status=alert,
            location="Segment1",
            reason=reason,
            measure=measure

        )
      analysis_result.save()   
      last_uploaded_text= TelegramAnalysis.objects.latest('uploaded_at')
      #from django.http import HttpResponse
      #from home.mlprocess import continuous_inference  # Import the continuous process function from ml_process.py
      #continuous_inference()  # Start the continuous process (for demo purposes; in production, consider background tasks)

    return render(request, 'pages/telegram.html',  {'latest_analysis_result': last_uploaded_text})
   

@login_required(login_url='/accounts/login/')
def youtube(request):
    c=AnalysisResult.objects.count()
    last_uploaded_text = None
    
    if request.method == 'POST':
      video_url = request.POST.get('video_url')
      name = request.POST.get('name')
      import re
      from pytube import YouTube
      import requests
      from googleapiclient.discovery import build
      import googleapiclient.discovery
      from youtube_transcript_api import YouTubeTranscriptApi
      import googleapiclient.discovery
      from furl import furl
        
      def retrive(VIDEO_URL):
        API_SERVICE_NAME = "youtube"
        API_VERSION = "v3"
        #API_KEY = 'AIzaSyCXNzM3NLzWJUyt0hR3abfN2Q88c0qntcY'
        API_KEY = 'AIzaSyDBpdf8DFfNPAH6Ls64gFwu1jJLC6kzLFI'
        def extract_video_id(youtube_url):
            video_id_match = re.search(r"v=([a-zA-Z0-9_-]+)", youtube_url)
            if video_id_match:
                return video_id_match.group(1)
            else:
                return None

        video_id = extract_video_id(VIDEO_URL)

        # Channel ID retrieval
        video_info_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={API_KEY}&part=snippet"
        response = requests.get(video_info_url)
        video_info = response.json()

        if 'items' in video_info and len(video_info['items']) > 0:
            channel_id = video_info['items'][0]['snippet']['channelId']
        else:
            channel_id = None

        # Transcript retrieval
        #tx = YouTubeTranscriptApi.get_transcript(video_id)
        #outls = [i['text'] for i in tx]

        # Video comments retrieval
        MAX_COMMENTS = 10 * 100

        def get_video_id(VIDEO_URL):
            if len(VIDEO_URL):
                f = furl(VIDEO_URL)
                if len(f.args) and 'v' in list(f.args.keys()):
                    return f.args['v']
            return None

        video_id = get_video_id(VIDEO_URL)

        def get_youtube_client():
            return googleapiclient.discovery.build(
                API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

        def get_comments_by_video(video_id, nextPageToken=None):
            request = get_youtube_client().commentThreads().list(
                part="snippet,replies",
                videoId=video_id,
                maxResults=100,
                pageToken=nextPageToken
            )
            return request.execute()

        def get_all_comments(video_id, max_comments):
            comments_list = []
            nextPageToken = None

            while True:
                comments = get_comments_by_video(video_id, nextPageToken)
                comments_list.extend(comments['items'])

                if len(comments_list) >= max_comments or 'nextPageToken' not in comments:
                    break

                nextPageToken = comments['nextPageToken']
            return comments_list

        video_comments = get_all_comments(video_id, MAX_COMMENTS)
        comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in video_comments]

        def get_channel_info(channel_id):
            youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

            request = youtube.channels().list(
                part="snippet",
                id=channel_id
            )
            response = request.execute()

            if "items" in response:
                channel = response["items"][0]
                channel_title = channel["snippet"]["title"]
                channel_description = channel["snippet"]["description"]
                return channel_title, channel_description
            else:
                return None, None

        channel_title, channel_description = get_channel_info(channel_id)

        # Video description retrieval
        def get_video_info(VIDEO_URL):
            video_id = VIDEO_URL.split("v=")[-1]

            youtube = build('youtube', 'v3', developerKey=API_KEY)
            video_response = youtube.videos().list(
                part="snippet",
                id=video_id
            ).execute()
            print(video_response)
            if 'items' in video_response:
                video_info = video_response['items'][0]['snippet']
                video_title = video_info['title']
                video_description = video_info['description']
                return video_title, video_description
            else:
                return None, None

        video_title, video_description = get_video_info(VIDEO_URL)

        return video_id, channel_id, comments, channel_title, channel_description, video_title, video_description
      
      video_id, channel_id, comments, channel_title, channel_description, video_title, video_description = retrive(video_url)  
      print(video_description)
      def remove_emojis(text):
        emoji_pattern = re.compile("["
                                  u"\U0001F600-\U0001F64F"  # emoticons
                                  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                  u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                  u"\U0001F700-\U0001F77F"  # alchemical symbols
                                  u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                  u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                  u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                  u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                                  u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                  u"\U00002702-\U000027B0"  # Dingbats
                                  u"\U000024C2-\U0001F251"
                                  "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
      video_description = remove_emojis(video_description)
      comments_cleaned=[]
      for i in comments:
         comments_cleaned.append(remove_emojis(i))
      outl="" ;count=0 
      # for i in outls:
      #    outl+" "+i
      #    count+=1
      #    if count==20:
      #       break



      #------------------------------------------------------------------------------------------------------------------------
      #DESCRIPTION ANALYSIS
      from transformers import BertForSequenceClassification, BertTokenizer
      model = BertForSequenceClassification.from_pretrained("home\desc_model")
      #tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
      import pandas as pd
      import torch
      inputs = tokenizer.encode_plus(
        video_description,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
      )

      input_ids = inputs["input_ids"]
      attention_mask = inputs["attention_mask"]

      with torch.no_grad():
          outputs = model(input_ids, attention_mask=attention_mask)

      logits = outputs.logits
      predicted_description = torch.argmax(logits, dim=1).item()
      class_probs_description = torch.softmax(logits, dim=1)[0].tolist()
      print("description")
      print("Predicted class:", predicted_description)
      print("Class probabilities:", class_probs_description)
      if predicted_description==1:
        description_score=class_probs_description[1]*10
      else:  
        description_score=class_probs_description[0]*10
      print()



      #-----------------------------------------------------------------------------------------------------------------
      #Comments Sentimental analysis
      print(len(comments))
      model_2 = BertForSequenceClassification.from_pretrained("home\senti_model")
      def classify_comment(comment,model_2):
        inputs = tokenizer.encode_plus(
          comment,
          add_special_tokens=True,
          max_length=128,
          padding="max_length",
          truncation=True,
          return_tensors="pt"
        )

        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        with torch.no_grad():
            outputs = model_2(input_ids, attention_mask=attention_mask)

        logits = outputs.logits
        comment_class = torch.argmax(logits, dim=1).item()
        comment_probs = torch.softmax(logits, dim=1)[0].tolist()
        return(comment_class)
      if len(comments)<100:
         n=len(comments)
      else:
         n=100
      comment_pred=[]   
      for i in range(n):
         comment_pred.append(classify_comment(comments[i],model_2))      
      print(comments_cleaned[0])
      print("Comments")
      print(comment_pred) 
      comments_score=(comment_pred.count(1)/len(comment_pred))*10    



      #------------------------------------------------------------------------------------------------------------
      # # Transcript
      # import re
      # from nltk.tokenize import word_tokenize
      # from nltk.corpus import stopwords
      # from gensim.models import KeyedVectors
      # from nltk.corpus import wordnet
      # from nltk.wsd import lesk 
      # def preprocess(text):
      #     text = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation and convert to lowercase
      #     tokens = word_tokenize(text)  # Tokenize
      #     filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
      #     return ' '.join(filtered_tokens)

      # # Apply preprocessing
      # preprocessed_transcripts = preprocess(outl)
      # transcript_words = preprocessed_transcripts.split()

      # keyword_frequency = {}
      # for i, word in enumerate(transcript_words):
      #   if word in flagged_keywords:
      #       if word in keyword_frequency:
      #               keyword_frequency[word] += 1
      #       else:
      #               keyword_frequency[word] = 1


      #   context_window = transcript_words[i:i+3]
      #   keyword=context_window[0]
      #   for j in range(len(context_window)):
      #       if keyword in flagged_keywords:
      #               if keyword in keyword_frequency:
      #                         keyword_frequency[keyword] += 1
      #               else:
      #                         keyword_frequency[keyword] = 1
      #       if j<len(context_window)-1:
      #         keyword=keyword+" "+context_window[j+1]
      # print(keyword_frequency)        
  


      
      #-----------------------------------------------------------------------------------------------------------
      #PROMOTION
      import openai
      # Set your OpenAI GPT-3 API key
      api_key = "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"
      # Generate explanation using GPT-3 API
      prompt=video_description+"/n"+"in this description can you please find for which app he is telling about or promoting. Exclude the social media apps. he would be promoting some finance related apps asking to create an account or download it. check if there is something like that? "  
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=250,
          stop=None,
          temperature=0.7
      )
      
      promotion = response.choices[0].text.strip()
    





      #------------------------------------------------------------------------------------------------------------------
      #CHATGPT App name analysis
      import openai
      # Set your OpenAI GPT-3 API key
      api_key = "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"
      # Generate explanation using GPT-3 API
      prompt=video_description+"/n"+"in this description can you please find for which app he is telling about or promoting. If he is promoting just tell only the app name or tell no. Exclude the social media apps. give only one word. just the required answer"  
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=250,
          stop=None,
          temperature=0.7
      )
      
      name = response.choices[0].text.strip()
      if name=="no" or name=="No":
         app_result=0
      if name in sebi_registered_apps:
         app_result=1
      elif name in sebi_alert_apps:
         app_result=2
      else:
         app_result=3 
      print(app_result)
      print()     

      



      #------------------------------------------------------------------------------------------------------------
      #Chatgpt video report
      import openai
      # Set your OpenAI GPT-3 API key
      api_key = "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"
      # Generate explanation using GPT-3 API
      prompt=video_description+"/n"+"I gave you the description of the youtube video related to finance which is may be highly misleading . if he promises high returns dicussing option strategies, using apps like binomo or quotex then it is highly misleading. Catch the quotex or binomo. give your analysis on the description i gave and find any misleading claim is present or it is only educational. analyse carefully?"  
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=250,
          stop=None,
          temperature=0.7
      )
      video_report = response.choices[0].text.strip()
      print(video_report)





      #-----------------------------------------------------------------------------------------------------------
      #Overall Report
      from googleapiclient.discovery import build


      def get_channel_videos(api_key, channel_id, max_results=10):
          youtube = build('youtube', 'v3', developerKey=api_key)

          videos = []
          nextPageToken = None

          while len(videos) < max_results:
              request = youtube.search().list(
                  part="id",
                  channelId=channel_id,
                  maxResults=5,
                  order="date",
                  pageToken=nextPageToken
              )
              response = request.execute()

              video_ids = [item['id']['videoId'] for item in response['items']]
              video_info_request = youtube.videos().list(
                  part="snippet",
                  id=",".join(video_ids)
              )
              video_info_response = video_info_request.execute()

              videos.extend(video_info_response['items'])

              nextPageToken = response.get('nextPageToken')
              if not nextPageToken:
                  break

          video_titles = []
          video_descriptions = []

          for video in videos[:max_results]:
              video_title = video['snippet']['title']
              video_description = video['snippet']['description']
              video_titles.append(video_title)
              video_descriptions.append(video_description)

          return video_titles, video_descriptions
      API_KEY = 'AIzaSyCXNzM3NLzWJUyt0hR3abfN2Q88c0qntcY'
      titles, descriptions = get_channel_videos(API_KEY, channel_id, max_results=10)
      ov=""
      for i in range(5):
         ov=ov+titles[i]
         ov=ov+descriptions[i]
         ov=ov+"\n"

      import openai
      # Set your OpenAI GPT-3 API key
      api_key = "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"
      # Generate explanation using GPT-3 API
      prompt=ov+"/n"+"I gave you the description, title of few videos of a youtube channel related to finance. Analyse and tell me what the influencer is expressing. Is the content ok. if the influencer is talking about forex trading and proving strategy in apps like binomo or quotex then it is highly misleading. if he also mentions any crypto meme coins,high returns it is also misleading. do not care about disclaimer. even if there is diclaimer it is misleading content only."  
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=250,
          stop=None,
          temperature=0.7
      )
      overall_report = response.choices[0].text.strip()
      if (description_score+comments_score)//2>5:
         conclu="legit"
      else:
         conclu="misleading"   

      #----------------------------------------------------------------------------------------------------------------
      analysis_result = AnalysisResult(
            name=name,
            video_url=video_url,
            channel_name=channel_title,
            transcript_score=5,
            comments_score=comments_score,
            description_score=description_score,
            about_score=app_result,
            promotion=promotion,
            overall_score=(description_score+comments_score)//2,
            video_report=video_report,
            overall_report=overall_report,
            conclusion=conclu
        )
      analysis_result.save()   
      last_uploaded_text= AnalysisResult.objects.latest('uploaded_at')

    return render(request, 'pages/youtube.html', {'latest_analysis_result': last_uploaded_text})



