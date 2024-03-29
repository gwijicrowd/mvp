from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator

class ScaleField(models.IntegerField):
    SCALE_CHOICES = [(i, str(i)) for i in range(1, 11)]
    choices = SCALE_CHOICES
    validators = [
        MinValueValidator(1),
        MaxValueValidator(10)
    ]

class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    dp = models.ImageField(upload_to='team_member_dp', blank=True)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    linkedin = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    VERIFIED = 'Verified'
    PENDING = 'Pending'
    NOTVERIFIED = 'NotVerified'

    NATIONAL_ID = "National ID Card"
    PASSPORT = "International Passport"
    DRIVERS_LICENSE = 'Drivers License'
    NONE = 'None'
   

    VERIFICATION_STATUS_CHOICES = (
        (VERIFIED, 'Verified'),
        (NOTVERIFIED, 'NotVerified'),
        (PENDING, 'Pending')
    )

    VERIFICATION_TYPE_CHOICES= (
        (NATIONAL_ID, 'National ID Card'),
        (PASSPORT, 'International Passport'),
        (DRIVERS_LICENSE, 'Drivers License'),
        (NONE, 'None')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_status = models.CharField(max_length=100, choices=VERIFICATION_STATUS_CHOICES, default=NOTVERIFIED)
    display_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    identification_type = models.CharField(max_length=100, choices=VERIFICATION_TYPE_CHOICES, default=NONE)
    identification_doc = models.ImageField(upload_to='profile_identifications', blank=True, default='')
    cover_photo = models.ImageField(upload_to='profile_cover', blank=True)
    bio = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    following = models.ManyToManyField('Campaigns', related_name='followed_campaigns', blank=True)
    date_joined = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username}"



class Projects(models.Model):
    IDEA_CONCEPTION = 'Idea Conception'

    PROJECT_STAGES = [
        ('Idea Conception', 'Idea Conception'),
        ('Market Research', 'Market Research'),
        ('Business Plan Creation', 'Business Plan Creation'),
        ('Prototyping', 'Prototyping'),
        ('MVP Development', 'MVP Development'),
        ('Initial Customer Acquisition', 'Initial Customer Acquisition'),
        ('Seed Funding Preparation', 'Seed Funding Preparation'),
        ('Pitching to Investors', 'Pitching to Investors'),
        ('Seed Funding Secured', 'Seed Funding Secured'),
        ('Scaling Operations', 'Scaling Operations'),
    ]

    TECH_AND_INNOVATIONS = 'Tech and Innovations'
    CREATIVE_WORKS = "Creative Works"
    FASHION_AND_WEARABLES = "Fashion and Wearables"
    HEALTH_AND_FITNESS = "Health and Fitness"
    ENERGY_AND_GREENTECH = "Energy and Green Tech"


    CATEGORY_CHOICES = (
        (TECH_AND_INNOVATIONS, 'Tech and Innovations'),
        (CREATIVE_WORKS, "Creative Works"),
        (FASHION_AND_WEARABLES, "Fashion and Wearables"),
        (HEALTH_AND_FITNESS, "Health and Fitness"),
        (ENERGY_AND_GREENTECH, "Energy and Green Tech")
    )
    
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=150, blank=True)
    logo = models.ImageField(upload_to='project_logos', blank=True) 
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='project_owner', default='1')
    description = models.TextField(max_length=400, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=TECH_AND_INNOVATIONS)
    website = models.CharField(max_length=100, default='gwiji.io')
    incorporated = models.BooleanField(default=False)
    incorporation_certificate =  models.FileField(upload_to='incorporation_certificates', default='', blank=True)
    valuation = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    valuation_report =  models.FileField(upload_to='valuation_reports', default='', blank=True)
    total_shares = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    prototype = models.FileField(upload_to='prototypes', default='', blank=True)
    pitch_deck = models.FileField(upload_to='pitch_decks', default='', blank=True)
    financials_doc = models.FileField(upload_to='financials_doc', default='', blank=True)
    market_research = models.FileField(upload_to='market_research_doc', default='', blank=True)
    operational_doc = models.FileField(upload_to='market_research_doc', default='', blank=True)
    shareperdollar = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    
    roadmap = models.CharField(max_length=50, choices=PROJECT_STAGES, default=IDEA_CONCEPTION)
    teams = models.ManyToManyField(Profile, related_name='team_members', blank=True)
    date_started = models.DateTimeField(blank=True, default=datetime.now)
    location = models.CharField(max_length=150, blank=True)
    


    def __str__(self):
        return f"{self.name}"
    

class Campaigns(models.Model):

    A = "A"
    B = "B"
    C = "C"
    
    PACK_CHOICES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C')
    )

    REVIEW = "In Review"
    ACTIVE = "Active"
    ENDED = "Ended"
    
    STATUS_CHOICES = (
        (REVIEW, 'In Review'),
        (ACTIVE, 'Active'),
        (ENDED, 'Ended'),
    )

   
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=REVIEW)
    subtitle = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project')
    campaign_picture = models.ImageField(upload_to='campaign_pictures', blank=True)
    pack_type = models.CharField(max_length=100, choices=PACK_CHOICES, default=A)
    current_raise = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    percentage_raised = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    intented_target = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    target = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    date_start = models.DateTimeField(default=datetime.now)
    date_end = models.DateTimeField()
    investments = models.ManyToManyField('Investments', related_name='investments', blank=True)
    campaign_board_story = models.TextField(default='', blank=True)
    campaign_board_challenges = models.TextField(default='', blank=True)
    campaign_board_unique = models.TextField(default='', blank=True)
    campaign_board_impact = models.TextField(default='', blank=True)
    campaign_board_goals = models.TextField(default='', blank=True)
    campaign_board_market = models.TextField(default='', blank=True)
    campaign_board_growth = models.TextField(default='', blank=True)
    campaign_board_team = models.TextField(default='', blank=True)
    campaign_board_innovation = models.TextField(default='', blank=True)
    campaign_board_future = models.TextField(default='', blank=True)
    
    def __str__(self):
        return f"{self.title}"
    

class Posts(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE, related_name='campaigns', blank=True, null=True)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images', blank=True)
    likes = models.ManyToManyField(Profile, related_name='post_likes', blank=True)
    comments = models.ManyToManyField('Comments', related_name='post_comments', blank=True)
    no_post_likes = models.IntegerField(default=0)
    no_post_views = models.IntegerField(default=0)
    no_post_comments = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.post_text}"


class Comments(models.Model):
    comment_text = models.TextField()
    comment_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_author')
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment_post')
    comment_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.comment_text}"
    

class BoardQuestions(models.Model):
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE, related_name='board_campaigns', blank=True)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}"
    

class Notifications(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notification')
    text = models.TextField()
    read = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.text}"
    
class Investments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE, related_name='invested_campaign')
    total_value_buying = models.IntegerField(default=0)
    total_value_current = models.IntegerField(default=0)
    total_shares = models.IntegerField(default=0)
    sharesperdollar_buying = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    sharesperdollar_current = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    date = models.DateTimeField(default=datetime.now)
    document = models.FileField(upload_to='investment_ddocument', default='', blank=True)

    def __str__(self):
        return f"{self.campaign}"
    

    def calculate(self):
        self.total_value_current = self.sharesperdollar_current * self.total_shares
        self.save()