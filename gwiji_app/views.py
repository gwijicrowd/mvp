from django.shortcuts import render
from .models import Projects, Campaigns, Posts, Comments, Profile,BoardQuestions, Notifications, Investments, Team
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
import json
from django.utils import timezone
from django.http import Http404

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '404.html', status=500)

@csrf_exempt
def verify_id(request):
    try: 
        if request.method == 'POST':
            id_type = request.POST.get('id_type')
            id_file = request.FILES.get('id_upload')
            print(id_type)
            print(id_file)
            profile = Profile.objects.get(user=request.user)
            profile.identification_doc = id_file
            profile.identification_type = id_type
            profile.verification_status = "Pending"
            profile.save()
    except:
        pass
    return render(request, 'index.html')

       


@csrf_exempt
def process_payment(request, id):
     if request.method == 'POST':
        try:
            amount = request.POST.get('amount')
            shares = request.POST.get('shares')
            sharesperdollar = request.POST.get('sharesperdollar')
            agreement_content = request.POST.get('agreementContent')
            profile = Profile.objects.get(user=request.user)
            campaign = get_object_or_404(Campaigns, pk=id)

            investment= Investments.objects.create(profile=profile, campaign=campaign, total_value_buying=amount, total_shares = shares, sharesperdollar_buying=sharesperdollar )
            campaign.current_raise += int(amount)
            campaign.save()

            try:
                text = f"{profile.display_name} from {profile.location} invested ${amount} in your '{campaign.title}' campaign🎊💰."
                notifications = Notifications.objects.create(profile=campaign.author, text=text)
                notifications.save()
            except:
                pass
            
            investment.save()
            # Return a JSON response
            return JsonResponse({'status': 'success', 'message': 'Payment processed successfully'})
        except:
             return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



@csrf_exempt  # Ensure that you import csrf_exempt from django.views.decorators.csrf
def create_campaign(request):
    if request.method == 'POST':
        # Retrieve data from the request
        company_logo = request.FILES.get('companyLogo')
        company_name = request.POST.get('companyName')
        company_tagline = request.POST.get('companyTagline')
        company_description = request.POST.get('companyDescription')
        company_website = request.POST.get('companyWebsite')
        is_company_incorporated = request.POST.get('isCompanyIncorporated')
        company_certificate = request.FILES.get('companyCertificate')
        company_location = request.POST.get('companyLocation')
        company_valuation = request.POST.get('companyValuation')
        company_valuation_report = request.POST.get('companyValuationReport')
        company_total_shares = request.POST.get('companyTotalShares')
        company_stage = request.POST.get('companyStage')
        company_category = request.POST.get('companyCategory')
        company_date_start = request.POST.get('companyDateStart')
        campaign_title = request.POST.get('campaignTitle')
        campaign_subtitle = request.POST.get('campaignSubtitle')
        campaign_target = request.POST.get('campaignTarget')
        campaign_duration = request.POST.get('campaignDuration')
        campaign_rewards = request.POST.get('campaignRewards')
        campaign_photo = request.FILES.get('campaignPhoto')
        campaign_board_story = request.POST.get('campaignBoardStory')
        campaign_board_challenges = request.POST.get('campaignBoardChallenges')
        campaign_board_unique = request.POST.get('campaignBoardUnique')
        campaign_board_impact = request.POST.get('campaignBoardImpact')
        campaign_board_goals = request.POST.get('campaignBoardGoals')
        campaign_board_market = request.POST.get('campaignBoardMarket')
        campaign_board_growth = request.POST.get('campaignBoardGrowth')
        campaign_board_team = request.POST.get('campaignBoardTeam')
        campaign_board_innovation = request.POST.get('campaignBoardInnovation')
        campaign_board_future = request.POST.get('campaignBoardFuture')
        pitch_deck = request.FILES.get('pitchDeck')
        prototype = request.FILES.get('prototype')
        financials = request.FILES.get('financials')
        market_research = request.FILES.get('marketResearch')
        operations = request.FILES.get('operations')
        team_member_1_name = request.POST.get('teamMember1Name')
        team_member_2_name = request.POST.get('teamMember2Name')
        team_member_3_name = request.POST.get('teamMember3Name')
        team_member_4_name = request.POST.get('teamMember4Name')

        shares_per_dollar = int(company_valuation)/int(company_total_shares)
        campaign_total_shares = (int(campaign_rewards)/100)*int(company_total_shares)
        target_raise = shares_per_dollar * int(campaign_total_shares)

        try: 
            profile = Profile.objects.get(user=request.user)
            project = Projects.objects.create(
                name=company_name, 
                tagline= company_tagline, 
                logo=company_logo, 
                owner=profile, 
                description=company_description, 
                category=company_category,
                website = company_website,
                prototype = prototype,
                incorporation_certificate = company_certificate,
                valuation = company_valuation,
                valuation_report = company_valuation_report,
                pitch_deck = pitch_deck,
                financials_doc = financials,
                market_research = market_research,
                operational_doc = operations,
                shareperdollar = 1.0,
                
                roadmap = company_stage,
                date_started = company_date_start,
                location = company_location,
                incorporated = is_company_incorporated.capitalize(),
                total_shares = company_total_shares
    
            )
            #teams
            project.teams.add(profile)
            if team_member_1_name:
                try:
                    team1 = get_object_or_404(Profile, username=team_member_1_name)
                    project.teams.add(team1)
                except:
                    pass
            if team_member_2_name:
                try:
                    team2 = get_object_or_404(Profile, username=team_member_2_name)
                    project.teams.add(team2)
                except:
                    pass
            if team_member_3_name:
                try:
                    team3 = get_object_or_404(Profile, username=team_member_3_name)
                    project.teams.add(team3)
                except:
                    pass
            if team_member_4_name:
                try:
                    team4 = get_object_or_404(Profile, username=team_member_4_name)
                    project.teams.add(team4)
                except:
                    pass
                
            project.save()
            campaign = Campaigns.objects.create(
                title = campaign_title,
                subtitle = campaign_subtitle,
                author = profile,
                project=project,
                campaign_picture = campaign_photo,
                pack_type = "A",
                target = target_raise,
                intented_target = campaign_target,
                date_end = datetime.now() + timedelta(days=int(campaign_duration)),
                campaign_board_story= campaign_board_story,
                campaign_board_challenges = campaign_board_challenges,
                campaign_board_unique=campaign_board_unique,
                campaign_board_impact=campaign_board_impact,
                campaign_board_goals=campaign_board_goals,
                campaign_board_market=campaign_board_market,
                campaign_board_growth=campaign_board_growth,
                campaign_board_team=campaign_board_team,
                campaign_board_innovation=campaign_board_innovation,
                campaign_board_future=campaign_board_future
            )
            campaign.save()
            # Return a success response
            return JsonResponse({'message': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'There was an issue creating campaign, please check all values again.'}, status=400)

@csrf_exempt
def post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        camp = request.POST.get('campaign')
        profile = Profile.objects.get(user=request.user)

        # Check if the campaign is provided and not 'none'
        if camp and camp != 'none':
            try:
                campaign = Campaigns.objects.get(title=camp)
            except Campaigns.DoesNotExist:
                # Handle the case where the campaign doesn't exist
                return JsonResponse({'error': 'Campaign not found'}, status=400)
        else:
            campaign = None  # Set it to None if not provided or 'none'

        # Check if an image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set it to None if not provided

        # Create the post with the provided or None values
        Posts.objects.create(profile=profile, campaign=campaign, post_image=image, post_text=text)

        return JsonResponse({'message': 'success'})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def discussion_post(request, id):
    if request.method == 'POST':
        text = request.POST.get('text')
        profile = Profile.objects.get(user=request.user)

        try:
            campaign = Campaigns.objects.get(id=id)
        except Campaigns.DoesNotExist:
            # Handle the case where the campaign doesn't exist
            campaign = None
            return JsonResponse({'error': 'Campaign not found'}, status=400)

        # Check if an image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set it to None if not provided
        # Create the post with the provided or None values
        Posts.objects.create(profile=profile, campaign=campaign, post_image=image, post_text=text)

        return JsonResponse({'message': 'success'})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)




@csrf_exempt
def save_profile(request):
    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        updated_bio = request.POST.get('bio')
        updated_location = request.POST.get('location')

        # Update the profile data
        user_profile.bio = updated_bio
        user_profile.location = updated_location

        # Handle image uploads if necessary
        if 'avatar' in request.FILES:
            user_profile.avatar = request.FILES['avatar']
        if 'cover' in request.FILES:
            user_profile.cover_photo = request.FILES['cover']

        user_profile.save()

        return JsonResponse({'message': 'Profile changes saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        posts = Posts.objects.all().order_by('-id')
        campaigns = Campaigns.objects.filter(status="Active")
        category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
        id_types = [choice[0] for choice in Profile.VERIFICATION_TYPE_CHOICES]
        profile = Profile.objects.get(user=request.user)
        followed_campaigns = profile.following.all
        my_campaigns = Campaigns.objects.filter(author = profile)

        for campaign in campaigns:
            current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
            if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
                campaign.status = "Ended"
                campaign.save()

        context = {
            'posts': posts,
            'campaigns': campaigns,
            'category_choices': category_choices,
            'profile': profile,
            'followed_campaigns': followed_campaigns,
            'my_campaigns': my_campaigns,
            'id_types': id_types
        }
        return render(request, 'browse.html', context)


    else:
        profile = None  # Initialize profile as None
        followed_campaigns = []
        projects = Projects.objects.all()
        campaigns = Campaigns.objects.filter(status="Active")
        
        for campaign in campaigns:
            # Calculate percentage_raised and add it to each campaign object
            campaign.percentage_raised = round((campaign.current_raise / campaign.target) * 100, 2)
            campaign.save()
        category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
        posts = Posts.objects.all().order_by('-id')[:5]
        no_of_startups = Projects.objects.count()
        no_of_investors = Profile.objects.count()
        result = Campaigns.objects.aggregate(total_crowdfunded=Sum('current_raise'))
        amount_crowdfunded = result['total_crowdfunded'] if result['total_crowdfunded'] is not None else 0
        
        for campaign in campaigns:
            current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
            if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
                campaign.status = "Ended"
                campaign.save()
                
        context = {
            'profile': profile,
            'projects': projects,
            'campaigns': campaigns,
            'category_choices': category_choices,
            'posts': posts,
            'no_of_startups': no_of_startups,
            'no_of_investors': no_of_investors,
            'amount_crowdfunded': amount_crowdfunded,
            'followed_campaigns': followed_campaigns
        }
    return render(request, 'index.html', context)


@csrf_exempt
def campaigns(request, id):
    campaign = get_object_or_404(Campaigns, pk=id)
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    project_stages = [choice[0] for choice in Projects.PROJECT_STAGES]
    current_stage = campaign.project.roadmap
    current_stage_position = project_stages.index(current_stage) + 1 if current_stage in project_stages else 0
    questions = BoardQuestions.objects.filter(campaign=campaign)
    posts = Posts.objects.filter(campaign=campaign)
    project = campaign.project
    pack = campaign.pack_type
    shareperdollar = project.shareperdollar
    valuation = project.valuation
    teams = project.teams.all()
    organizer = campaign.author
    today_date = datetime.now

    for camp in campaigns:
        current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
        if camp.current_raise >= camp.target or current_datetime >= camp.date_end:
            camp.status = "Ended"
            camp.save()
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        followed_campaigns = profile.following.all
    else:
        profile = None
        followed_campaigns = []
    
    
    # Define tier information for each pack
    tier_info = {
        'A': [50, 100, 200, 500, 1000],
        'B': [200, 500, 1000, 5000, 10000],
        'C': [500, 1000, 10000, 50000, 100000],
    }

   # Get the tier information based on the selected pack
    selected_pack_tiers = tier_info.get(pack, [])

    # Convert Decimal values to integers for shares_per_tier
    shares_per_tier = [int(tier * shareperdollar) for tier in selected_pack_tiers]

    # Create a list of tier dictionaries
    tier_info_list = []
    for tier_price, shares in zip(selected_pack_tiers, shares_per_tier):
        tier_info_list.append({
            'tier_price': tier_price,
            'shares': shares,
        })
    context = {
        'campaign': campaign,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'questions': questions,
        'posts': posts,
        'teams': teams,
        'project_stages': project_stages,
        'current_stage': current_stage,
        'current_stage_position': current_stage_position,
        'pack': pack,
        'shareperdollar': shareperdollar,
        'valuation': valuation,
        'selected_pack_tiers': selected_pack_tiers,
        'shares_per_tier': shares_per_tier,
        'tier_info_list': tier_info_list,
        'profile': profile,
        'followed_campaigns': followed_campaigns,
        'today_date': today_date
        

    }
    return render(request, 'campaigns.html', context)

@csrf_exempt
def follow_campaign(request, campaign_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        profile = Profile.objects.get(user=request.user)
        campaign = Campaigns.objects.get(id=campaign_id)
        author = campaign.author
        following = profile.following.all()
        if action:
            if campaign not in following:
                profile.following.add(campaign)
                try:
                    text = f"Someone from {profile.location} followed your '{campaign.title}' campaign🥳."
                    notifications = Notifications.objects.create(profile=author, text=text)
                    notifications.save()
                except:
                    pass
                message = f'♥ Following'
            else:
                profile.following.remove(campaign)
                message = f'♡ Follow'
        return JsonResponse({'status': 'success', 'message': message})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
def comment(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        post = Posts.objects.get(id=post_id)
        profile = Profile.objects.get(user=request.user)
        author = post.profile
        comment = Comments.objects.create(comment_text =text, comment_author=profile, comment_post=post)
        post.comments.add(comment)
        post.no_post_comments += 1
        post.save()
        try:
            text = f"Someone from {profile.location} commented on your post about '{post.campaign.title}' campaign 💌."
            notifications = Notifications.objects.create(profile=author, text=text)
            notifications.save()
        except:
            pass
        return JsonResponse({'status': 'success', 'message': post.no_post_comments})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



@csrf_exempt
def like_post(request, post_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        profile = Profile.objects.get(user=request.user)
        post = Posts.objects.get(id=post_id)
        author = post.profile
        likes = post.likes.all()
        if action:
            if profile not in likes:
                post.likes.add(profile)
                post.no_post_likes += 1
                post.save()
                try:
                    if post.campaign:
                        text = f"Someone from {profile.location} reacted to your post about '{post.campaign.title}' campaign ❤️."
                        notifications = Notifications.objects.create(profile=author, text=text)
                        notifications.save()

                except:
                    pass
                message = f'You are now liking post {post_id}'
            else:
                post.likes.remove(profile)
                if post.no_post_likes == 0:
                    pass
                else:
                    post.no_post_likes -= 1
                post.save()
                message = f'You have unliked post {post_id}'
        return JsonResponse({'status': 'success', 'message': post.no_post_likes})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
def filter_campaigns(request):
    filter_type = request.GET.get('filter_type')
    value = request.GET.get('value')

    # Perform the filtering based on the selected category
    if filter_type == 'category':
        filtered_campaigns = Campaigns.objects.filter(category=value)

    # Render the filtered campaigns as HTML
    html = render(request, 'filtered_campaigns.html', {'campaigns': filtered_campaigns})

    return JsonResponse({'html': html.content.decode('utf-8')})


@csrf_exempt
def browse(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    followed_campaigns = profile.following.all
    my_campaigns = Campaigns.objects.filter(author = profile)

    for campaign in campaigns:
        current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
        if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
            campaign.status = "Ended"
            campaign.save()

    

    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'followed_campaigns': followed_campaigns,
        'my_campaigns': my_campaigns
    }
    return render(request, 'browse.html', context)


@csrf_exempt
def feeds(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    followed_campaigns = profile.following.all
    my_campaigns = Campaigns.objects.filter(author = profile)

    for campaign in campaigns:
        current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
        if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
            campaign.status = "Ended"
            campaign.save()

    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'followed_campaigns': followed_campaigns,
        'my_campaigns': my_campaigns
    }
    return render(request, 'feeds.html', context)

@csrf_exempt
def following(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    followed_campaigns = profile.following.all
    my_campaigns = Campaigns.objects.filter(author = profile)

    context = {
        'posts': posts,
        'campaigns': campaigns,
        'profile': profile,
        'category_choices': category_choices,
        'followed_campaigns': followed_campaigns,
        'my_campaigns': my_campaigns
    }
    return render(request, 'following.html', context)

@csrf_exempt
def manage_campaigns(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    my_campaigns = Campaigns.objects.filter(author = profile)
    project_stages = [choice[0] for choice in Projects.PROJECT_STAGES]

    for campaign in campaigns:
        current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
        if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
            campaign.status = "Ended"
            campaign.save()
    
    
    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'my_campaigns': my_campaigns,
        'project_stages': project_stages
    }
    return render(request, 'manage_campaigns.html', context)

@csrf_exempt
def financials(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    my_campaigns = Campaigns.objects.filter(author = profile)

    investors_count = Investments.objects.filter(campaign__in=my_campaigns).count()
    investors = Investments.objects.filter(campaign__in=my_campaigns)

    investors_worth = 0
    investors_shares = 0
    investors_profile = []
    investors_profiles_count = 0
    for invest in investors:
        investors_worth += invest.total_value_buying
        investors_shares += invest.total_shares

        if invest.profile not in investors_profile:
            investors_profile.append(invest.profile)
            investors_profiles_count += 1

    all_investments = Investments.objects.all()
    my_investments = Investments.objects.filter(profile=profile)
    investments_count = my_investments.count()

    investments_worth = 0
    investments_shares = 0
    investments_companies = []
    investments_companies_count = 0

    for invest in my_investments:
        investments_worth += invest.total_value_buying
        investments_shares += invest.total_shares

        if invest.campaign.project not in investments_companies:
            investments_companies.append(invest.campaign.project)
            investments_companies_count += 1

    for investor in all_investments:
        investor.sharesperdollar_current = investor.campaign.project.shareperdollar
        investor.calculate()
        investor.save()

    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'my_campaigns': my_campaigns,
        'investors': investors,
        'my_investments': my_investments,
        'investments_count': investments_count,
        'investors_count': investors_count,
        'investments_worth': investments_worth,
        'investments_shares': investments_shares,
        'investments_companies_count': investments_companies_count,
        'investors_worth': investors_worth,
        'investors_shares': investors_shares,
        'investors_profiles_count': investors_profiles_count,

    }
    return render(request, 'financials.html', context)

@csrf_exempt
def notifications(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    notifications = Notifications.objects.filter(profile=profile).order_by('-id')
    my_campaigns = Campaigns.objects.filter(author = profile)

    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'notifications': notifications,
        'my_campaigns': my_campaigns
    }
    return render(request, 'notifications.html', context)

@csrf_exempt
def profile(request):
    posts = Posts.objects.all().order_by('-id')
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    profile = Profile.objects.get(user=request.user)
    my_posts = Posts.objects.filter(profile = profile).order_by('-id')
    my_projects = Projects.objects.filter(owner= profile)
    investments = Investments.objects.filter(profile=profile)
    investments_count = investments.count()

    for campaign in campaigns:
        current_datetime = timezone.now()  # Use Django's timezone.now() if using Django
        if campaign.current_raise >= campaign.target or current_datetime >= campaign.date_end:
            campaign.status = "Ended"
            campaign.save()
    
    unique_investments = []
    my_campaigns = Campaigns.objects.filter(author = profile)

    investors_count = 0 
    for camp in my_campaigns:
        investors_count += Investments.objects.filter(campaign=camp).count()

    for investment in investments:
        if investment not in unique_investments:
            unique_investments.append(investment)
    
    context = {
        'posts': posts,
        'campaigns': campaigns,
        'category_choices': category_choices,
        'profile': profile,
        'my_posts': my_posts,
        'my_projects': my_projects,
        'investments': investments,
        'investments_count': investments_count,
        'investors_count': investors_count,
        'my_campaigns': my_campaigns,
        'unique_investments': unique_investments

    }
    return render(request, 'profile.html', context)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists. '}, status=400)
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
            profile = Profile.objects.create(user=user, username=username, display_name=f"{first_name} {last_name}")
            auth.login(request, user)
            return JsonResponse({'message': 'success'})
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        usermail = User.objects.filter(email=email).first()
        user = auth.authenticate(username=usermail.username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'error': 'Invalid login credentials, please check your email adress and password.'}, status=400)
    return render(request, 'index.html')

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('index')



@csrf_exempt
def company(request):
    campaigns = Campaigns.objects.filter(status="Active")
    category_choices = [choice[0] for choice in Projects.CATEGORY_CHOICES]
    context = {
        'campaigns': campaigns,
        'category_choices': category_choices

        }
    return render(request, 'company.html', context)